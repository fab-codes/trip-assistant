from src.agents.choose_destination_place_agent.agent import ChooseDestinationPlaceAgent
from src.graph.states.general_state import GeneralState
from src.utils.logger import get_logger

logger = get_logger(__name__)

async def choose_destination_place_node(state: GeneralState) -> dict:
    agent = ChooseDestinationPlaceAgent()

    return await agent.process(state)