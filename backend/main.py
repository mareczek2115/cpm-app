from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Event, CpmNode
from typing import List

app = FastAPI()

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
    calculate_cpm(events)
    return {"status": "ok"}

def calculate_cpm(events: List[Event]):
    nodes = []
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
        node.late_start = node.late_finish - node.duration
        
    #delete finish node
    nodes.pop()

    #calculate reserve
    for node in nodes:
        node.reserve = node.late_start - node.early_start

    for node in nodes:
        print(node)

    critical_path = []

    for node in nodes:
        if node.reserve == 0:
            critical_path.append(node.id)

    print(critical_path)