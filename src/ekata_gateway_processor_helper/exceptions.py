from typing import Dict, List


class GatewayProcessorException(Exception):
    def __init__(self, message: str = 'Unknown error occurred') -> None:
        self.message = message

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}({self.message!r})"


class InvalidProjectException(GatewayProcessorException):
    pass


class InvalidAPIKeyException(GatewayProcessorException):
    pass


class NoEnabledCurrencyException(GatewayProcessorException):
    pass


class InvalidArgumentsException(Exception):
    def __init__(self, arguments: List[Dict[str, str]] = []) -> None:
        self.arguments = arguments

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}({self.arguments!r}"
