import React from 'react';
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="bg-gray-800 text-white p-4 flex justify-between">
      <div className="space-x-4">
        <Link to="/" className="hover:underline">Главная</Link>
        <Link to="/subscriptions" className="hover:underline">Подписки</Link>
      </div>
    </nav>
  );
}
