from Signal.city_signal import CitySignal
from Signal.highway_signal import HighwaySignal
from Controller.controller import SignalController
from app_logger import logger

logger.info(f"Traffic Simulation started...")

controller=SignalController
no_vehicle= int(input("Enter Number of vehicles:"))

CitySignal=CitySignal(no_vehicle)
HighwaySignal=HighwaySignal(no_vehicle)

controller.operate(CitySignal)
controller.operate(HighwaySignal)

logger.info("Simulation completed")