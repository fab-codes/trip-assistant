from langgraph.graph import MessagesState

from trip_assistant.types.flight_option import FlightOption

class GeneralState(MessagesState):
    ideal_destination_description: str

    destination_place: str
    start_place: str
    
    start_date: str
    end_date: str
    
    itinerary: str
    
    flight_options: list[FlightOption]