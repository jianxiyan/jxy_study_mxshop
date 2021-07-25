package middlewares

import (
	"mxshop_api/user-web/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func IsAdminAuth() gin.HandlerFunc {
	return func(c *gin.Context) {
		claims, _ := c.Get("claims")
		currentUser := claims.(*models.CustomClaims)

		if currentUser.AuthorityId != 2 {
			c.JSON(http.StatusForbidden, map[string]string{
				"msg": "无权限",
			})
			c.Abort()
			return
		}
		c.Next()
	}
}
