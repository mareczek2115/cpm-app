# CPM App – Critical Path Method Web Tool

A web application for logistics and project planning that calculates and visualizes the critical path based on input events, their durations, and dependencies.

## Technologies Used

- Frontend: Vue.js  
- Backend: FastAPI  
- Visualization: Graphviz  
- Communication: REST API

## How to start

```bash
git clone https://github.com/mareczek2115/cpm-app.git
```

### Frontend

```bash
cd cpm-app/frontend
npm install
npm run dev
```
### Backend
Install Graphviz engine 12.2.1, during installation add to ENV PATH
https://graphviz.org/download/

```bash
cd cpm-app/backend
pip install uv
uv sync
.venv\Scripts\activate
fastapi dev main.py
```
