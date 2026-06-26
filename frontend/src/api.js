import axios from "axios";

const bookApi = axios.create({
  baseURL: "http://localhost:8000"
});

const orderApi = axios.create({
  baseURL: "http://localhost:8080"
});

export const getBooks = () => bookApi.get("/books");

export const getOrders = () => orderApi.get("/orders");

export const createOrder = (data) =>
  orderApi.post("/orders", data);