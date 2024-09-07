import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './LoginPage.js';
import HomePage from './HomePage.js';
import FeedbackPage from './FeedbackPage.js';
import KudosPage from './KudosPage.js';
import ProfilePage from './ProfilePage.js';  // Import the ProfilePage component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/" element={<HomePage />} />
        <Route path="/feedback" element={<FeedbackPage />} />
        <Route path="/kudos" element={<KudosPage />} />
        <Route path="/profile" element={<ProfilePage />} />
      </Routes>
    </Router>
  );
}

export default App;
