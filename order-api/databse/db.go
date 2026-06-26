package database

import (
	"fmt"
	"log"
	"os"
	"time"

	"github.com/joho/godotenv"
	"github.com/mekichat/order-api/models"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var DB *gorm.DB

func Connect() {

	var database *gorm.DB

	err := godotenv.Load("../.env")
	if err != nil {
		log.Println("No .env file found, using system env")
	}

	dsn := os.Getenv("DB_DSN")

	if dsn == "" {
		log.Fatal("DB_DSN not set")
	}

	for i := 0; i < 20; i++ {

		database, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})

		if err == nil {
			fmt.Println("Connected to PostgreSQL")
			DB = database

			DB.AutoMigrate(&models.Order{})

			return
		}

		fmt.Println("Waiting for PostgreSQL...")
		time.Sleep(3 * time.Second)
	}

	panic("failed to connect database after multiple retries")
}
