package models

type Order struct {
	ID       int `json:"id" gorm:"primaryKey"`
	BookID   int `json:"book_id" binding:"required"`
	Quantity int `json:"quantity" binding:"required,min=1"`
}
