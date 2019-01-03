"""
Represents an invitation message for establishing connection.
"""

from marshmallow import Schema, fields

from ..agent_message import AgentMessage
from ..message_types import MessageType
from ..validators import must_not_be_blank

from ...models.agent_endpoint import AgentEndpoint, AgentEndpointSchema


class ConnectionInvitation(AgentMessage):
    def __init__(self, endpoint: AgentEndpoint, image_url: str, connection_key: str):
        self.endpoint = endpoint
        self.image_url = image_url
        self.connection_key = connection_key

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageType.CONNECTION_INVITATION


class ConnectionInvitationSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    endpoint = fields.Nested(AgentEndpointSchema, validate=must_not_be_blank)
    image_url = fields.Str()
    connection_key = fields.Str()
