package global

import (
	"mxshop_api/user-web/config"
	"mxshop_api/user-web/proto"
)

var (
	//全局配置
	ServerConfig *config.ServerConfig
	//全局proto客户端链接
	UserSrvClient proto.UserClient
)
