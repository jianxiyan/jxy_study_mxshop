package initialize

import (
	"fmt"
	"mxshop_api/user-web/global"
	"mxshop_api/user-web/proto"

	"go.uber.org/zap"
	"google.golang.org/grpc"
)

func InitSrvConn() {
	consulInfo := global.ServerConfig.UserSrvInfo
	userConn, err := grpc.Dial(
		fmt.Sprintf("%s:%d", consulInfo.Host, consulInfo.Port),
		grpc.WithInsecure(),
	)
	if err != nil {
		zap.S().Fatal("[InitSrvConn] 链接【用户服务失败】")
	}
	userSrvClient := proto.NewUserClient(userConn)
	global.UserSrvClient = userSrvClient

}
