import React from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

export default function Subscriptions() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4">Страница подписок</h1>
      <button onClick={handleLogout} className="bg-red-500 text-white px-4 py-2 rounded">
        Выйти
      </button>
    </div>
  );
}
