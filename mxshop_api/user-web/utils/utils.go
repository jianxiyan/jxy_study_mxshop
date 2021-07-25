package utils

const ENV = "MXSHOP_DEBUG"

//判断是否是测试环境
func GetEnvInfo() bool {
	// viper.AutomaticEnv()
	// return viper.GetBool(ENV)
	return true
	//重启ide才生效
}
