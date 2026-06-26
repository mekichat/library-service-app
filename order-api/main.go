// @title 📦 Order Service API

// @version 1.0

// @description A production-grade microservice for managing orders in a distributed library system.
// @description
// @description Services:
// @description - 📘 Book Service (FastAPI + MySQL)
// @description - 📦 Order Service (Go + PostgreSQL)
// @description
// @description Features:
// @description - Clean REST architecture
// @description - Full CRUD operations
// @description - PostgreSQL persistence using GORM
// @description - Docker & Kubernetes ready
// @description - Swagger API testing
// @description

// @contact.name Library System Team
// @contact.email mekuriategegne@gmail.com

// @License.name YH Akademin
// @BasePath /
package main

import (
	"time"

	database "github.com/mekichat/order-api/databse"

	"github.com/mekichat/order-api/handlers"

	"github.com/gin-gonic/gin"

	"github.com/gin-contrib/cors"

	swaggerFiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"

	_ "github.com/mekichat/order-api/docs"
)

func main() {

	database.Connect()

	router := gin.Default()

	router.Use(cors.New(cors.Config{
		AllowOrigins:     []string{"http://localhost:3000", "http://localhost:3001", "http://localhost:5173"},
		AllowMethods:     []string{"GET", "POST", "PUT", "DELETE"},
		AllowHeaders:     []string{"Content-Type"},
		AllowCredentials: true,
		MaxAge:           12 * time.Hour,
	}))

	// routes

	// OpenAPI JSON
	router.GET("/swagger/doc.json", ginSwagger.WrapHandler(swaggerFiles.Handler))

	// Custom Swagger UI (an AWS-style portal)
	router.Static("/swagger-ui", "./swagger-ui")

	router.GET("/orders", handlers.GetOrders)
	router.GET("/orders/:id", handlers.GetOrderByID)
	router.POST("/orders", handlers.CreateOrder)
	router.PUT("/orders/:id", handlers.UpdateOrder)
	router.DELETE("/orders/:id", handlers.DeleteOrder)

	router.Run(":8080")

}
