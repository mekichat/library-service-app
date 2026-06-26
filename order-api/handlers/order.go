package handlers

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
	database "github.com/mekichat/order-api/databse"
	"github.com/mekichat/order-api/models"
	"github.com/mekichat/order-api/services"
)

// GetOrders godoc
// @Summary Get all orders
// @Description Returns a list of all orders in the system
// @Tags Orders
// @Produce json
// @Success 200 {array} models.Order
// @Failure 500 {object} map[string]string
// @Router /orders [get]
func GetOrders(c *gin.Context) {
	var orders []models.Order
	database.DB.Find(&orders)
	c.JSON(http.StatusOK, orders)
}

// CreateOrder godoc
// @Summary Create a new order
// @Description Creates an order for a specific book with quantity. This will store the order in the database.
// @Tags Orders
// @Accept json
// @Produce json
// @Param order body models.Order true "Order payload"
// @Success 201 {object} models.Order "Order created successfully"
// @Failure 400 {object} map[string]string "Invalid request payload"
// @Failure 500 {object} map[string]string "Internal server error"
// @Router /orders [post]
func CreateOrder(c *gin.Context) {

	var order models.Order

	// 1. Bind input
	if err := c.ShouldBindJSON(&order); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	// DEBUG HERE (temporary)
	book, err := services.GetBookByID(order.BookID)
	fmt.Println("BOOK:", book)
	fmt.Println("ERROR:", err)

	// 2. Validate book_id
	if order.BookID <= 0 {
		c.JSON(400, gin.H{"error": "invalid book_id"})
		return
	}

	// Validate Quantity
	if order.Quantity <= 0 {
		c.JSON(400, gin.H{
			"error": "quantity must be greater than 0",
		})
		return
	}

	//book, err := services.GetBookByID(order.BookID)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "book service unreachable"})
		return
	}

	if book == nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "book does not exist"})
		return
	}

	// 3. Save order in DB
	if err := database.DB.Create(&order).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "could not create order"})
		return
	}

	c.JSON(http.StatusCreated, order)
}

// GetOrderByID godoc
// @Summary Get order by ID
// @Description Fetch a single order using its unique ID
// @Tags Orders
// @Produce json
// @Param id path int true "Order ID"
// @Success 200 {object} models.Order
// @Failure 404 {object} map[string]string "Order not found"
// @Router /orders/{id} [get]
func GetOrderByID(c *gin.Context) {

	id := c.Param("id")

	var order models.Order

	result := database.DB.First(&order, id)

	if result.Error != nil {
		c.JSON(http.StatusNotFound, gin.H{
			"error": "Order not found",
		})
		return
	}

	c.JSON(http.StatusOK, order)
}

// UpdateOrder godoc
// @Summary Update an existing order
// @Description Updates book_id or quantity of an existing order
// @Tags Orders
// @Accept json
// @Produce json
// @Param id path int true "Order ID"
// @Param order body models.Order true "Updated order data"
// @Success 200 {object} models.Order
// @Failure 404 {object} map[string]string "Order not found"
// @Failure 400 {object} map[string]string "Invalid input"
// @Router /orders/{id} [put]
func UpdateOrder(c *gin.Context) {
	id := c.Param("id")

	var order models.Order

	if err := database.DB.First(&order, id).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Order not found"})
		return
	}

	if err := c.ShouldBindJSON(&order); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	database.DB.Save(&order)
	c.JSON(http.StatusOK, order)
}

// DeleteOrder godoc
// @Summary Delete an order
// @Description Permanently deletes an order by ID
// @Tags Orders
// @Produce json
// @Param id path int true "Order ID"
// @Success 200 {object} map[string]string "Order deleted successfully"
// @Failure 404 {object} map[string]string "Order not found"
// @Router /orders/{id} [delete]
func DeleteOrder(c *gin.Context) {
	id := c.Param("id")

	database.DB.Delete(&models.Order{}, id)

	c.JSON(http.StatusOK, gin.H{"message": "deleted"})
}
