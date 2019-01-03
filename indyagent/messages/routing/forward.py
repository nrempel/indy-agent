from ..agent_message import AgentMessage
from ..message_types import MessageType


class Forward(AgentMessage):
    def type(self):
        return MessageType.FORWARD
