import React from 'react';
import { NavLink } from 'react-router-dom';
import './Header.css'; // 👈 добавили стили

export default function Header() {
  return (
    <nav>
      <NavLink to="/" end>
        Подписки
      </NavLink>
      <NavLink to="/login">
        Вход
      </NavLink>
      <NavLink to="/register">
        Регистрация
      </NavLink>
    </nav>
  );
}
