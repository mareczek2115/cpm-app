from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Event, CpmNode
from typing import List
from fastapi.staticfiles import StaticFiles
from graphviz import Digraph
import uuid
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    'http://localhost:5173',
    'http://127.0.0.1:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS'],
    allow_headers=['*']
)


@app.get("/")
async def root():
    return {"message": "siemanko"}


@app.post("/api/cpm")
def post_cpm(events: List[Event]):
    result = calculate_cpm(events)
    return result

def calculate_cpm(events: List[Event]):
    nodes: List[CpmNode] = []
    for event in events:
        node = CpmNode(**event.model_dump())
        nodes.append(node)


    #add successors
    for node in nodes:
        if len(node.predecessors) != 0:
            for predecessor in node.predecessors:
                nodes[predecessor].successors.append(node.id)

    #add finish node
    finish_event = Event(id=len(nodes), name="finish", duration=0, predecessors = [])
    finish_node = CpmNode(**finish_event.model_dump())

    for node in nodes:
        if len(node.successors) == 0:
            node.successors.append(finish_node.id)
            finish_node.predecessors.append(node.id)
    
    nodes.append(finish_node)

    #calculate step ahead
    for node in nodes:
        if len(node.predecessors) != 0:
            max_prev_early_finish = nodes[node.predecessors[0]].early_finish
            for predecessor in node.predecessors:
                if nodes[predecessor].early_finish > max_prev_early_finish:
                    max_prev_early_finish = nodes[predecessor].early_finish

        else:
            max_prev_early_finish = 0
        
        node.early_start = max_prev_early_finish
        node.early_finish = node.early_start + node.duration


    #calculate step back
    for node in reversed(nodes):
        if len(node.successors) != 0:
            min_next_late_start = nodes[node.successors[0]].late_start
            for successor in node.successors:
                if nodes[successor].late_start < min_next_late_start:
                    min_next_late_start = nodes[successor].late_start

        else:
            #that means that we are in finish node
            min_next_late_start = node.early_finish

        node.late_finish = min_next_late_start
        node.late_start = max(node.late_finish - node.duration, 0)
        
    #delete finish node
    nodes.pop()

    #calculate reserve
    for node in nodes:
        node.reserve = max(node.late_start - node.early_start, 0)

    # for node in nodes:
    #     print(node)

    critical_path = []

    edges = []

    for node in nodes:
        if node.reserve == 0:
            critical_path.append(node.id)
        
        if len(node.predecessors) != 0:
            for predecessor in node.predecessors:
                
                if node.reserve == 0 and nodes[predecessor].reserve == 0:
                    edge_tuple = (predecessor, node.id, '#43a61c')
                    edges.append(edge_tuple)
                else:
                    edge_tuple = (predecessor, node.id, 'black')
                    edges.append(edge_tuple)


    # print(critical_path)

    dict_nodes = [node.dict(exclude={"successors"}) for node in nodes]
    # print(dict_nodes)

    image_url = generate_graph(dict_nodes, edges)
    print(image_url)
    return {"nodes": dict_nodes, "image_url":image_url}



def generate_graph(nodes_data, edges):
    dot = Digraph(comment='cpm-graph', format='png')
    dot.attr(rankdir='LR') 
    dot.attr(dpi="900")

    for i, node in enumerate(nodes_data):
        label = f"""<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="2">
            <TR>
                <TD>{node.get('early_start', '')}</TD>
                <TD>{node.get('duration', '')}</TD>
                <TD>{node.get('early_finish', '')}</TD>
            </TR>
            <TR>
                <TD COLSPAN="3"><B>{node.get('name', '')}</B></TD>
            </TR>
            <TR>
                <TD>{node.get('late_start', '')}</TD>
                <TD>{node.get('reserve', '')}</TD>
                <TD>{node.get('late_finish', '')}</TD>
            </TR>

        </TABLE>
        >"""
        dot.node(str(i), label=label, shape='none')


    for start, end, color in edges:
        dot.edge(str(start), str(end), color=color)

    u = uuid.uuid4()
    path = os.path.join('static', f'{u}')
    dot.render(path)
    full_url = 'http://localhost:8000/' +'static/' +f'{u}.png'
    return full_url
