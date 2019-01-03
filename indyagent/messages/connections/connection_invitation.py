"""
Represents an invitation message for establishing connection.
"""

from ..agent_message import AgentMessage
from ..message_types import MessageType


class ConnectionInvitation(AgentMessage):
    def type(self) -> str:
        return MessageType.CONNECTION_INVITATION

