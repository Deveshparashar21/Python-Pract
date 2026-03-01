from app_logger import logger

class SignalController:
    def operate(signal):
        logger.info(f"signal Controller started for {signal.signal_type()}")
        time=signal.green_time()
        logger.info(f"{signal.signal_type()} --> Green for {time} seconds..")
        logger.info(f"Signal Controller operation completed")