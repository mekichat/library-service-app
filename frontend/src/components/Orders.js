import React, { useEffect, useState } from "react";

export default function Orders() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/orders")
      .then(res => res.json())
      .then(data => {
        setOrders(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div className="container-fluid">

      {/* Header */}
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h3 className="fw-bold">📦 Orders</h3>

        <button className="btn btn-success">
          + Create Order
        </button>
      </div>

      {/* Loading state */}
      {loading && (
        <div className="text-center text-muted">
          Loading orders...
        </div>
      )}

      {/* Empty state */}
      {!loading && orders.length === 0 && (
        <div className="alert alert-info">
          No orders found
        </div>
      )}

      {/* Orders Table */}
      {!loading && orders.length > 0 && (
        <div className="card shadow-sm border-0">

          <div className="card-body">

            <table className="table table-hover align-middle">

              <thead className="table-dark">
                <tr>
                  <th>ID</th>
                  <th>Book ID</th>
                  <th>Quantity</th>
                  <th>Status</th>
                </tr>
              </thead>

              <tbody>
                {orders.map(order => (
                  <tr key={order.id}>

                    <td>#{order.id}</td>
                    <td>{order.book_id}</td>
                    <td>{order.quantity}</td>

                    {/* Fake status (you can later connect real DB field) */}
                    <td>
                      <span className="badge bg-success">
                        Completed
                      </span>
                    </td>

                  </tr>
                ))}
              </tbody>

            </table>

          </div>

        </div>
      )}

    </div>
  );
}