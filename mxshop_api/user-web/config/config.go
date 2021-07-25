package config

// 用户服务配置
type UserSrvConfig struct {
	Host string `mapstructure:"host" json:"host"`
	Port int    `mapstructure:"port" json:"port"`
	Name string `mapstructure:"name" json:"name"`
}

type ConsulConfig struct {
	Host string `mapstructure:"host" json:"host"`
	Port int    `mapstructure:"port" json:"port"`
}

// token配置
type JWTConfig struct {
	SigningKey string `mapstructure:"key" json:"key"`
}

type RedisConfig struct {
	Host   string `mapstructure:"host" json:"host"`
	Port   int    `mapstructure:"port" json:"port"`
	Expire int    `mapstructure:"expire" json:"expire"`
}

// 短信配置
type AliSmsConfig struct {
	ApiKey     string `mapstructure:"key" json:"key"`
	ApiSecrect string `mapstructure:"secrect" json:"secrect"`
}

type ServerConfig struct {
	Name        string        `mapstructure:"name" json:"name"`
	Host        string        `mapstructure:"host" json:"host"`
	Tags        string        `mapstructure:"tags" json:"tags"`
	Port        int           `mapstructure:"port" json:"port"`
	Env         string        `mapstructure:"env" json:"env"`
	UserSrvInfo UserSrvConfig `mapstructure:"user_srv" json:"user_srv"`
	ConsulInfo  ConsulConfig  `mapstructure:"consul" json:"consul"`
	JWTInfo     JWTConfig     `mapstructure:"jwt" json:"jwt"`
	RedisInfo   RedisConfig   `mapstructure:"redis" json:"redis"`
	AliSmsInfo  AliSmsConfig  `mapstructure:"sms" json:"sms"`
}
