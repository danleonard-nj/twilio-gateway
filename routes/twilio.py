from quart import Blueprint, request

from framework.handlers.response_handler_async import response_handler
from framework.auth.wrappers.azure_ad_wrappers import azure_ad_authorization

from clients.twilio_client import TwilioClient

twilio_bp = Blueprint('twilio_bp', __name__)


@twilio_bp.route('/api/twilio/message', methods=['POST'], endpoint='send_message')
@response_handler
@azure_ad_authorization(scheme='send')
async def send_message(container):
    client: TwilioClient = container.resolve(TwilioClient)

    body = await request.get_json()

    if not body:
        raise Exception('request body cannot be null')

    if not body.get('recipient'):
        raise Exception('recipient cannot be null')

    if not body.get('message'):
        raise Exception('message cannot be null')

    result = client.send_message(
        recipient=body.get('recipient'),
        message=body.get('message'))

    return result
