import logging
import sys

def setup_logger(name="SmokeDetectorX", log_level=logging.INFO):
    """
    Provides robust logging for edge operation without needing an attached console.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Stream Handler (stdout)
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File Handler (persistent logs)
    try:
        fh = logging.FileHandler('/var/log/smoke_detector_x.log')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    except PermissionError:
        print("Warning: Cannot write to /var/log/. Falling back to local file.")
        fh = logging.FileHandler('smoke_detector.local.log')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
