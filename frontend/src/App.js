import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import LoginPage from './LoginPage.js';
import HomePage from './HomePage.js';
import FeedbackPage from './FeedbackPage.js';
import KudosPage from './KudosPage.js';
import ProfilePage from './ProfilePage.js';  
import SidebarLayout from './SidebarLayout.js'; // Import the SidebarLayout component

// PrivateRoute component to check authentication
const PrivateRoute = ({ children }) => {
  const isAuthenticated = localStorage.getItem("access_token"); // Check if user is authenticated
  return isAuthenticated ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <Router>
      <Routes>
        {/* Public route for login */}
        <Route path="/login" element={<LoginPage />} />

        {/* Protected routes with SidebarLayout */}
        <Route
          path="/"
          element={
            <PrivateRoute>
              <SidebarLayout>
                <HomePage />
              </SidebarLayout>
            </PrivateRoute>
          }
        />
        <Route
          path="/feedback"
          element={
            <PrivateRoute>
              <SidebarLayout>
                <FeedbackPage />
              </SidebarLayout>
            </PrivateRoute>
          }
        />
        <Route
          path="/kudos"
          element={
            <PrivateRoute>
              <SidebarLayout>
                <KudosPage />
              </SidebarLayout>
            </PrivateRoute>
          }
        />
        <Route
          path="/profile"
          element={
            <PrivateRoute>
              <SidebarLayout>
                <ProfilePage />
              </SidebarLayout>
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
