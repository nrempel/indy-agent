from abc import ABC, abstractproperty

from .message_types import MessageType


class AgentMessage(ABC):
    @abstractproperty
    def type(self) -> str:
        pass
