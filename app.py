from quart import Quart
from routes.twilio import twilio_bp
from routes.health import health_bp
from utils.provider import add_container_hook

from framework.logger.providers import get_logger


logger = get_logger(__name__)

app = Quart(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(twilio_bp)

add_container_hook(app)

if __name__ == '__main__':
    app.run(debug=True, port='5091')
