from flask import Flask
from middleware.logging_middleware import register_logging
from routers.logs import log_bp
from routers.login import login_bp
from routers.logs import default_bp

app = Flask(__name__)
app.register_blueprint(log_bp, url_prefix="/api")
app.register_blueprint(login_bp, url_prefix="/api")
app.register_blueprint(default_bp, url_prefix="/api")

register_logging(app)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
