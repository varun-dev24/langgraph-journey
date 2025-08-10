from typing import TypedDict
from langgraph.graph import StateGraph
from IPython.display import display, Image

class AgentState(TypedDict):
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """ Simple node that adds a greeting message """

    state["message"] = f"Hello {state['message']}!, how are you?"
    return state

graph = StateGraph(AgentState)

graph.add_node("greeting", greeting_node)

graph.set_entry_point("greeting")
graph.set_finish_point("greeting")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))