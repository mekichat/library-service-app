package services

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

type Book struct {
	ID     int     `json:"id"`
	Title  string  `json:"title"`
	Author string  `json:"author"`
	Price  float64 `json:"price"`
}

func getBookServiceURL() string {
	url := os.Getenv("BOOK_SERVICE_URL")
	if url == "" {
		return "http://localhost:8000"
	}
	return url
}

func GetBookByID(id int) (*Book, error) {
	url := fmt.Sprintf("%s/books/%d", getBookServiceURL(), id)

	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode == 404 {
		return nil, nil // book not found
	}

	if resp.StatusCode != 200 {
		return nil, fmt.Errorf("book service error: %d", resp.StatusCode)
	}

	var book Book
	err = json.NewDecoder(resp.Body).Decode(&book)
	if err != nil {
		return nil, err
	}

	return &book, nil
}
