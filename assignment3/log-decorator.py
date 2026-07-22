import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        pos = list(args) if args else "none"
        key = dict(kwargs) if kwargs else "none"

        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {pos}")
        logger.info(f"keyword parameters: {key}")
        logger.info(f"return: {result}")

        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")
    return None

@logger_decorator
def many_positional(*args):
    return True

@logger_decorator
def many_keywords(**kwargs):
    return logger_decorator

hello_world()
many_positional(1, 2, 3)
many_keywords(a=10, b=20)
