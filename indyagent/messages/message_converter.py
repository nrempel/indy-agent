from .message_types import MessageTypes

from .connections.connection_invitation import ConnectionInvitationSchema
from .connections.connection_request import ConnectionRequestSchema
from .connections.connection_response import ConnectionResponseSchema

from .credentials.credential_offer import CredentialOfferSchema
from .credentials.credential_request import CredentialRequestSchema
from .credentials.credential import CredentialSchema

from .proofs.proof_request import ProofRequestSchema
from .proofs.proof import ProofSchema

from .routing.forward import ForwardSchema

from .connections.connection_invitation import ConnectionInvitation


class MessageParseError(Exception):
    pass


class MessageConverter:
    """
    Message converter for serializing and deserializing content
    messages to and from json to their respective object types
    """

    @classmethod
    def object_to_message(cls, obj):
        """
        Given a dict describing a message, this method
        returns an instance of the related message class.
        """

        print(obj["@type"])
        print(MessageTypes.CONNECTION_INVITATION.value)
        print(type(obj["@type"]))

        try:

            # Connection Messages
            if obj["@type"] == MessageTypes.CONNECTION_INVITATION.value:
                message_schema = ConnectionInvitationSchema()
            elif obj["@type"] == MessageTypes.CONNECTION_REQUEST.value:
                message_schema = ConnectionRequestSchema()
            elif obj["@type"] == MessageTypes.CONNECTION_RESPONSE.value:
                message_schema = ConnectionResponseSchema()

            # Credential Messages
            elif obj["@type"] == MessageTypes.CREDENTIAL.value:
                message_schema = CredentialOfferSchema()
            elif obj["@type"] == MessageTypes.CREDENTIAL_OFFER.value:
                message_schema = CredentialRequestSchema()
            elif obj["@type"] == MessageTypes.CREDENTIAL_REQUEST.value:
                message_schema = CredentialSchema()

            # Proof Messages
            elif obj["@type"] == MessageTypes.PROOF.value:
                message_schema = ProofRequestSchema()
            elif obj["@type"] == MessageTypes.PROOF_REQUEST.value:
                message_schema = ProofSchema()

            # Routing Messages
            elif obj["@type"] == MessageTypes.PROOF_REQUEST.value:
                message_schema = ForwardSchema()

            else:
                raise MessageParseError(f"Unrecognized message type {obj['@type']}")

        except KeyError:
            raise MessageParseError("Message is badly formatted.")

        return message_schema.load(obj)

