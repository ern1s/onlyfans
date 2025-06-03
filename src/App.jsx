import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Subscriptions from './pages/Subscriptions';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Subscriptions />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}




