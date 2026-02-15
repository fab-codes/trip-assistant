from trip_assistant.agents.choose_destination_place_agent.agent import ChooseDestinationPlaceAgent
from trip_assistant.graph.states.general_state import GeneralState
from trip_assistant.utils.logger import get_logger

logger = get_logger(__name__)

async def choose_destination_place_node(state: GeneralState) -> dict:
    agent = ChooseDestinationPlaceAgent()

    return await agent.process(state)