from langchain_google_genai import ChatGoogleGenerativeAI
from src.agents.base_agent import BaseAgent
from src.config import AppConfig
from src.graph.states.general_state import GeneralState
from src.utils.logger import get_logger
from langchain_core.messages import SystemMessage, HumanMessage

logger = get_logger(__name__)

class ChooseDestinationPlaceAgent(BaseAgent):
    def __init__(self):
        llm = ChatGoogleGenerativeAI(
            model=AppConfig.GOOGLE_MODEL_ID,
            temperature=1.0,
            max_tokens=None,
            timeout=None,
        )

        sys_msg = SystemMessage(
            content="You are an expert travel organizer. Choose the ideal destination based on the user's description."
        )

        super().__init__(llm, "ChooseDestinationPlaceAgent", sys_msg)

    async def process(self, state: GeneralState) -> dict:
        try:
            human_msg = HumanMessage(content=state["ideal_destination_description"])

            messages = [self.sys_message, human_msg]

            result = await self.llm.ainvoke(messages)

            logger.info("Choose destination place completed")

            return {
                "destination_place": result.content,
                "messages": [human_msg, result]
            }

        except Exception as e:
            logger.error(f"Error in choose destination place: {e}")
            raise