
# middlewares/auth.py
from flask import request, jsonify


def register_auth_middleware(app, secret_token: str):
    """
    注册鉴权中间件：
    - 校验 Authorization 或 X-Token 请求头
    - token 不匹配则终止请求
    """
    @app.before_request
    def auth_check():
        token = request.headers.get(
            "Authorization") or request.headers.get("X-Token")
        if token != secret_token:
            return jsonify({"error": "Unauthorized"}), 401
