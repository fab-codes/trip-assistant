from langchain_google_genai import ChatGoogleGenerativeAI
from trip_assistant.agents.base_agent import BaseAgent
from trip_assistant.config import AppConfig
from trip_assistant.graph.states.general_state import GeneralState
from trip_assistant.utils.logger import get_logger
from langchain_core.messages import SystemMessage, HumanMessage

logger = get_logger(__name__)

class CreateItineraryAgent(BaseAgent):
    def __init__(self):
        llm = ChatGoogleGenerativeAI(
            model=AppConfig.GOOGLE_MODEL_ID,
            temperature=1.0,
            max_tokens=None,
            timeout=None,
        )

        sys_msg = SystemMessage(
            content="You are an expert travel organizer. Create a correct itinerary travel plan based on the user's ideal " \
                    "journey with the passed destination."
        )

        super().__init__(llm, "CreateItineraryAgent", sys_msg)

    async def process(self, state: GeneralState) -> dict:
        try:
            human_msg = HumanMessage(content=state["destination_place"])

            result = await self.agent.ainvoke({"messages": [human_msg]})

            ai_msg = result["messages"][-1]

            logger.info("📝 Itinerary creation completed")

            return {
                "itinerary": ai_msg.content,
                "messages": [human_msg, ai_msg]
            }

        except Exception as e:
            logger.error(f"Error in create itinerary: {e}")
            raise