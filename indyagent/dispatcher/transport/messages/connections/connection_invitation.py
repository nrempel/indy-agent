from ..agent_message import AgentMessage
from ..message_types import MessageType


class ConnectionInvitation(AgentMessage):
    def type(self):
        return MessageType.CONNECTION_INVITATION
