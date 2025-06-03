import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleLogin = (e) => {
    e.preventDefault();
    login(); // Фейковая авторизация
    navigate('/');
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form onSubmit={handleLogin} className="p-6 border rounded">
        <h2 className="text-xl mb-4">Вход</h2>
        <input type="email" placeholder="Email" className="block mb-2 p-2 border w-full" />
        <input type="password" placeholder="Пароль" className="block mb-4 p-2 border w-full" />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded w-full">
          Войти
        </button>
        <p className="mt-4 text-sm">
          Нет аккаунта? <a href="/register" className="text-blue-600 underline">Зарегистрируйтесь</a>
        </p>
      </form>
    </div>
  );
}


