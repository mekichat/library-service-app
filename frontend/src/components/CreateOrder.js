import React, { useState } from "react";

export default function CreateOrder() {
  const [form, setForm] = useState({
    book_id: "",
    quantity: ""
  });

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setMessage("");
    setError("");

    try {
      const response = await fetch("/orders", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          book_id: Number(form.book_id),
          quantity: Number(form.quantity)
        })
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.error || "Failed to create order");
        return;
      }

      setMessage("🎉 Order created successfully!");

      setForm({
        book_id: "",
        quantity: ""
      });

    } catch (err) {
      setError("⚠ Cannot reach Order Service");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container-fluid">

      {/* Header */}
      <div className="mb-4">
        <h3 className="fw-bold">➕ Create Order</h3>
        <p className="text-muted">Place a new order for a book</p>
      </div>

      {/* Alerts */}
      {message && (
        <div className="alert alert-success">
          {message}
        </div>
      )}

      {error && (
        <div className="alert alert-danger">
          {error}
        </div>
      )}

      {/* Form Card */}
      <div className="card shadow-sm border-0">
        <div className="card-body">

          <form onSubmit={handleSubmit} className="row g-3">

            <div className="col-md-6">
              <label className="form-label">Book ID</label>
              <input
                className="form-control"
                value={form.book_id}
                onChange={(e) =>
                  setForm({ ...form, book_id: e.target.value })
                }
                placeholder="Enter Book ID"
                required
              />
            </div>

            <div className="col-md-6">
              <label className="form-label">Quantity</label>
              <input
                className="form-control"
                value={form.quantity}
                onChange={(e) =>
                  setForm({ ...form, quantity: e.target.value })
                }
                placeholder="Enter Quantity"
                required
              />
            </div>

            <div className="col-12">
              <button
                className="btn btn-primary w-100"
                disabled={loading}
              >
                {loading ? "Creating Order..." : "Create Order"}
              </button>
            </div>

          </form>

        </div>
      </div>

    </div>
  );
} 