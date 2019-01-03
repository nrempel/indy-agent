"""
A credential offer content message.
"""

from marshmallow import Schema, fields

from ..agent_message import AgentMessage
from ..message_types import MessageType


class CredentialOffer(AgentMessage):
    def __init__(self, offer_json: str):
        self.offer_json = offer_json

    def type(self):
        return MessageType.CREDENTIAL_OFFER


class CredentialOfferSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    offer_json = fields.Str()
