// src/components/HomePage.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function HomePage() {
  const navigate = useNavigate();

  return (
    <div>
      <h2>Home Page</h2>
      <button onClick={() => navigate('/feedback')}>FEEDBACK</button>
      <button onClick={() => navigate('/kudos')}>KUDOS</button>
      <br />
      <button onClick={() => navigate('/profile')}>Profile</button>
    </div>
  );
}

export default HomePage;
