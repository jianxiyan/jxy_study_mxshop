package initialize

import (
	"fmt"

	"github.com/spf13/viper"
	"go.uber.org/zap"

	"mxshop_api/user-web/global"
	"mxshop_api/user-web/utils"
)

func InitConfig() {
	//根据环境来判断使用那个配置文件
	debug := utils.GetEnvInfo()
	configFilePrefix := "config"
	configFileName := fmt.Sprintf("user-web/%s-pro.yaml", configFilePrefix)
	if !debug {
		configFileName = fmt.Sprintf("user-web/%s-debug.yaml", configFilePrefix)
	}

	v := viper.New()
	//文件的路径设置
	v.SetConfigFile(configFileName)
	if err := v.ReadInConfig(); err != nil {
		zap.S().Errorf("配置信息读取失败：%v", err.Error())
		panic(err)
	}
	//这个对象如何在其他文件中使用 - 全局变量
	if err := v.Unmarshal(&global.ServerConfig); err != nil {
		zap.S().Errorf("配置信息反序列化失败：%v", err.Error())
		panic(err)
	}
	zap.S().Infof("配置信息：%v", global.ServerConfig)
}
