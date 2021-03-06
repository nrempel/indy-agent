"""
A credential offer content message.
"""

from marshmallow import Schema, fields, post_load

from ..agent_message import AgentMessage
from ..message_types import MessageTypes


class CredentialOffer(AgentMessage):
    def __init__(self, offer_json: str):
        self.offer_json = offer_json

    def _type(self):
        return MessageTypes.CREDENTIAL_OFFER.value


class CredentialOfferSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    offer_json = fields.Str()

    @post_load
    def make_model(self, data: dict) -> CredentialOffer:
        return CredentialOffer(**data)
