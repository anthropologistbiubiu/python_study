import logging
import os
from flask import request, g, jsonify
import time


def register_logging(app):
    # 创建 logs/access.log 文件
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "access.log")

    # 设置日志格式与输出到文件
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_path, encoding='utf-8'),
            logging.StreamHandler()  # 同时输出到控制台
        ]
    )

    @app.before_request
    def start_timer():
        g.start_time = time.time()
        g.error = None
        logging.info(
            f"🔹 Request: {request.method} {request.path} from {request.remote_addr}")
        if request.is_json:
            logging.info(f"🔸 Payload: {request.get_json(silent=True)}")

    @app.after_request
    def log_response(response):
        # 只记录正常流程（未出错的响应）
        duration = time.time() - g.get("start_time", time.time())
        try:
            response_data = response.get_data(as_text=True)
        except Exception:
            response_data = "<binary>"
        logging.info(
            f"✅ Response: {response.status_code} | Path: {request.path} | "
            f"Duration: {duration:.3f}s | Response: {response_data}"
        )
        return response

    @app.teardown_request
    def log_exception(exception):
        if exception:
            duration = time.time() - g.get("start_time", time.time())
            logging.error(
                f"❌ Exception: {exception} | Path: {request.path} | "
                f"Duration: {duration:.3f}s from {request.remote_addr}",
                exc_info=True
            )

    @app.errorhandler(Exception)
    def handle_exception(e):
        # 统一返回错误响应，同时确保被 after/teardown 记录
        response = jsonify({"error": str(e)})
        response.status_code = 500
        return response
