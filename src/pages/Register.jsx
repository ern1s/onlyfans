import React from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Register() {
  const navigate = useNavigate();
  const { login } = useAuth(); // После регистрации сразу "авторизуем"

  const handleRegister = (e) => {
    e.preventDefault();
    // Тут можно будет подключить API для регистрации
    login(); // Авторизация после регистрации
    navigate('/'); // Переход на главную
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form onSubmit={handleRegister} className="p-6 border rounded">
        <h2 className="text-xl mb-4">Регистрация</h2>
        <input type="text" placeholder="Имя" className="block mb-2 p-2 border w-full" />
        <input type="text" placeholder="Email" className="block mb-2 p-2 border w-full" />
        <input type="password" placeholder="Пароль" className="block mb-4 p-2 border w-full" />
        <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded w-full">
          Зарегистрироваться
        </button>
        <p className="mt-4 text-sm text-center">
          Нет аккаунта? <Link to="/login" className="text-blue-600 underline">Войти</Link>
        </p>
      </form>
    </div>
  );
}
