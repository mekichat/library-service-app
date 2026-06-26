import React from "react";
import { Link, useLocation } from "react-router-dom";

export default function DashboardLayout({ children }) {
  const location = useLocation();

  const isActive = (path) => location.pathname === path;

  return (
    <div className="d-flex" style={{ minHeight: "100vh" }}>

      {/* Sidebar */}
      <div
        className="bg-dark text-white p-3 shadow"
        style={{ width: "240px" }}
      >
        <h4 className="text-center mb-4 fw-bold">
          📚 Library System
        </h4>

        <div className="nav flex-column gap-2">

          <Link
            to="/books"
            className={`nav-link rounded px-3 py-2 ${
              isActive("/books") ? "bg-primary text-white" : "text-white"
            }`}
          >
            📚 Books
          </Link>

          <Link
            to="/orders"
            className={`nav-link rounded px-3 py-2 ${
              isActive("/orders") ? "bg-primary text-white" : "text-white"
            }`}
          >
            📦 Orders
          </Link>

          <Link
            to="/create-order"
            className={`nav-link rounded px-3 py-2 ${
              isActive("/create-order") ? "bg-primary text-white" : "text-white"
            }`}
          >
            ➕ Create Order
          </Link>

        </div>
      </div>

      {/* Main Content */}
      <div className="flex-grow-1 bg-light">

        {/* Top Navbar */}
        <div className="bg-white shadow-sm px-4 py-3 d-flex justify-content-between align-items-center">
          <h5 className="mb-0 fw-bold text-secondary">
            Dashboard
          </h5>

          <div className="d-flex align-items-center gap-3">
            <span className="text-muted">Admin</span>
            <div className="bg-dark text-white rounded-circle d-flex align-items-center justify-content-center"
                 style={{ width: "35px", height: "35px" }}>
              A
            </div>
          </div>
        </div>

        {/* Page Content */}
        <div className="p-4">
          {children}
        </div>

      </div>
    </div>
  );
}