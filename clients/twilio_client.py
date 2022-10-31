from twilio.rest.api.v2010.account.message import MessageInstance
from twilio.rest import Client

from framework.configuration.configuration import Configuration


class TwilioClient:
    def __init__(self, container):
        configuration = container.resolve(Configuration)

        self._client = Client(
            configuration.twilio.get('account_sid'),
            configuration.twilio.get('auth_token'))
        self._sender = configuration.twilio.get('sender')

    def send_message(self, recipient: str, message: str) -> MessageInstance:
        response: MessageInstance = self._client.messages.create(
            to=recipient,
            from_=self._sender,
            body=message)

        return response._properties
