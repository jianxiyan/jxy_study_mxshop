package global

import (
	ut "github.com/go-playground/universal-translator"

	"mxshop_api/user-web/config"
	"mxshop_api/user-web/proto"
)

var (
	//全局配置
	ServerConfig *config.ServerConfig
	//全局proto客户端链接
	UserSrvClient proto.UserClient
	//全局表单验证器
	Trans ut.Translator
)
