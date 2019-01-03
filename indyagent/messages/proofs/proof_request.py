"""
A proof request content message.
"""

from marshmallow import Schema, fields

from ..agent_message import AgentMessage
from ..message_types import MessageType


class ProofRequest(AgentMessage):
    def __init__(self, proof_request_json: str):
        self.proof_request_json = proof_request_json

    def type(self):
        return MessageType.PROOF_REQUEST


class ProofRequestSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type")
    proof_request_json = fields.Str()
