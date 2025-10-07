from flask import Flask
from middleware.logging_middleware import register_logging
from middleware.auth_middleware import register_auth_middleware
from middleware.warp_middlerware import register_wrap_middleware

from routers.logs import logs_bp
import logging

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.WARNING)  # 只显示 >= WARNING 的日志（隐藏 404 等 INFO）

app = Flask(__name__)
app.register_blueprint(logs_bp, url_prefix="/api/logs")

register_logging(app)
register_wrap_middleware(app)
register_auth_middleware(app, "secret_token")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
