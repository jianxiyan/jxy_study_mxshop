import argparse
import os
import signal
import sys
from concurrent import futures
from functools import partial

import grpc
from loguru import logger

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, BASE_DIR)

from user_srv.proto import user_pb2_grpc
from user_srv.handler.user import UserServicer



def on_exit(signo, frame, service_id):
    logger.info(f"注销成功{service_id}")
    sys.exit(0)


def serve():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        nargs="?",
                        type=str,
                        default="127.0.0.1",
                        help="binding ip"
                        )
    parser.add_argument("--port",
                        nargs="?",
                        type=int,
                        default=8091,
                        help="the listening prot"
                        )
    args = parser.parse_args()

    logger.add("logs/user_srv_{time}.log")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # 注册用户服务
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)

    # 注册健康检查

    server.add_insecure_port(f'{args.ip}:{args.port}')

    import uuid
    service_id = str(uuid.uuid1())

    # 主进程退出信号监听
    """
        windows下支持的信号是有限的：
            SIGINT ctrl+c终端
            SIGTHRM kill发出的软件终止
    """
    signal.signal(signal.SIGINT, partial(on_exit, service_id=service_id))
    signal.signal(signal.SIGTERM, partial(on_exit, service_id=service_id))

    logger.info(f'启动服务：{args.ip}:{args.port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    # logger.basicConfig()
    serve()
