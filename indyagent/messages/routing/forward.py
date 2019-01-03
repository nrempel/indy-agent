"""
Represents a forward message.
"""

from marshmallow import Schema, fields

from ..agent_message import AgentMessage
from ..message_types import MessageType


class Forward(AgentMessage):
    def __init__(self, to: str, msg: str):
        self.to = to
        self.msg = msg

    def type(self):
        return MessageType.FORWARD


class ForwardSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    to = fields.Str()
    msg = fields.Str()
