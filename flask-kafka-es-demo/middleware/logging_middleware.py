import logging
import os
from flask import request, g
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
        logging.info(
            f"🔹 Request: {request.method} {request.path} from {request.remote_addr}")
        if request.is_json:
            logging.info(f"🔸 Payload: {request.get_json()}")

    @app.after_request
    def log_response(response):
        duration = time.time() - g.start_time
        logging.info(
            f"✅ Response: {response.status_code} | Duration: {duration:.3f}s\n")
        return response
