
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin
# 使用peewee的链接池，使用ReconnectMixin来防止出现链接断开查询失败
class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass

NACOS = {
    "Host": "192.168.0.104",
    "port": 8848,
    "NameSpace": "c1872978-d51c-4188-a497-4e0cd20b97d5",
    "User": "root",
    "Password": "123456",
    "DataId": "user-srv.json",
    "Group": "dev"
}

data = {
    "name":"user-srv",
    "tags":["imooc", "bobby", "python", "srv"],
    "mysql":{
        "db":"mxshop_user_srv",
        "host":"127.0.0.1",
        "port":3306,
        "user":"root",
        "password":"jianxiyan."
    },
    "consul":{
        "host":"192.168.0.104",
        "port":8500
    }
}

DB = ReconnectMysqlDatabase(data["mysql"]["db"], host=data["mysql"]["host"], port=data["mysql"]["port"],
                            user=data["mysql"]["user"], password=data["mysql"]["password"])