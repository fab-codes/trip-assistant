from src.graph.compile_graph import compile_graph
from src.graph.states.general_state import GeneralState
from src.utils.logger import get_logger

logger = get_logger(__name__)

async def start_network(data: str) -> dict:
    app = compile_graph()

    result: GeneralState = await app.ainvoke({"ideal_destination_description": data}, {"configurable": {"thread_id": "1"}})

    logger.info('Graph final result')
    logger.info(result)

    return {"final_destination": result["destination_place"]}

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_network("Mi piacerebbe andare in un posto con montagne e mare"))