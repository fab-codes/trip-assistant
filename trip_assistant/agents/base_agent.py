from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from trip_assistant.utils.logger import get_logger
from langchain_core.messages import SystemMessage

logger = get_logger(__name__)

class BaseAgent(ABC):
    """
    Base class for all agents
    """
    def __init__(self, llm, agent_name: str, sys_message: Optional[SystemMessage] = None):
        self.llm = llm
        self.agent_name = agent_name
        self.sys_message = sys_message
        logger.info(f"🤖 Initialized {agent_name}")
    
    @abstractmethod
    async def process(self, data: Any) -> Dict[str, Any]:
        """Main processing method to be implemented by all agents"""
        pass
