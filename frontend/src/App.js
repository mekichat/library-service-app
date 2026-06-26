import { BrowserRouter, Routes, Route } from "react-router-dom";
import DashboardLayout from "./layout/DashboardLayout";

import Books from "./components/Books";
import Orders from "./components/Orders";
import CreateOrder from "./components/CreateOrder";

function App() {
  return (
    <BrowserRouter>
      <DashboardLayout>
        <Routes>
          <Route path="/books" element={<Books />} />
          <Route path="/orders" element={<Orders />} />
          <Route path="/create-order" element={<CreateOrder />} />
        </Routes>
      </DashboardLayout>
    </BrowserRouter>
  );
}

export default App;