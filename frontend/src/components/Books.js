import React, { useEffect, useState } from "react";

export default function Books() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/books/")
      .then(res => res.json())
      .then(data => {
        setBooks(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div className="container-fluid">

      {/* Header */}
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h3 className="fw-bold">📚 Books</h3>

        <button className="btn btn-primary">
          + Add Book
        </button>
      </div>

      {/* Loading state */}
      {loading && (
        <div className="text-center text-muted">
          Loading books...
        </div>
      )}

      {/* Empty state */}
      {!loading && books.length === 0 && (
        <div className="alert alert-info">
          No books available
        </div>
      )}

      {/* Books Grid */}
      <div className="row g-3">

        {books.map(book => (
          <div className="col-md-4" key={book.id}>
            <div className="card shadow-sm border-0 h-100 card-hover">

              <div className="card-body">

                <h5 className="card-title text-primary">
                  {book.title}
                </h5>

                <p className="text-muted mb-1">
                  Author: {book.author}
                </p>

                <div className="d-flex justify-content-between align-items-center mt-3">
                  <span className="badge bg-success">
                    ${book.price}
                  </span>

                  <button className="btn btn-sm btn-outline-primary">
                    View
                  </button>
                </div>

              </div>

            </div>
          </div>
        ))}

      </div>
    </div>
  );
}