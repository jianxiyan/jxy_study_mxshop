import json

import nacos
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin
from loguru import logger


# 使用peewee的链接池，使用ReconnectMixin来防止出现链接断开查询失败
class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


NACOS = {
    "Host": "127.0.0.1",
    "Port": 8848,
    "NameSpace": "b4cd33c6-8ff7-469b-af93-bc720c62c216",
    "User": "nacos",
    "Password": "nacos",
    "DataId": "user-srv.json",
    "Group": "dev"
}

client = nacos.NacosClient(f'{NACOS["Host"]:{NACOS["Port"]}}', namespace=NACOS["NameSpace"],
                           username=NACOS["User"],
                           password=NACOS["Password"])

data = client.get_config(NACOS["DataId"], NACOS["Group"])
data = json.loads(data)
logger.info(data)

def update_cfg(args):
    print("配置产生变化")
    print(args)

# data = {
#     "name":"user-srv",
#     "tags":["imooc", "bobby", "python", "srv"],
#     "mysql":{
#         "db":"mxshop_user_srv",
#         "host":"127.0.0.1",
#         "port":3306,
#         "user":"root",
#         "password":"jianxiyan."
#     },
#     "consul":{
#         "host":"127.0.0.1",
#         "port":8500
#     }
# }

# consul的配置
CONSUL_HOST = data["consul"]["host"]
CONSUL_PORT = data["consul"]["port"]

# 服务相关的配置
SERVICE_NAME = data["name"]
SERVICE_TAGS = data["tags"]

DB = ReconnectMysqlDatabase(data["mysql"]["db"], host=data["mysql"]["host"], port=data["mysql"]["port"],
                            user=data["mysql"]["user"], password=data["mysql"]["password"])