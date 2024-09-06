// src/components/FormOne.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function FeedbackPage() {
  const [formData, setFormData] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Feedback submitted: ${formData}`);
  };

  return (
    <div>
      <h2>FEEDBACK</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter something"
          value={formData}
          onChange={(e) => setFormData(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      <br />
      <button onClick={() => navigate('/profile')}>Profile</button>
    </div>
  );
}

export default FeedbackPage;
