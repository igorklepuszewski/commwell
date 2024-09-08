import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import axios from 'axios';

function FeedbackPage() {
  const [name, setName] = useState('');
  const [comments, setComments] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Basic validation
    if (!name || !comments) {
      setError('Please fill out all required fields.');
      return;
    }

    // Reset error
    setError('');

    try {
      // POST request to the API
      await axios.post('http://localhost:8001/api/feedback', {
        name,
        comments
      });

      // Clear form fields
      setName('');
      setComments('');
    } catch (err) {
      setError('Failed to submit feedback. Please try again.');
    }
  };

  return (
    <Box className="container" component="form" noValidate autoComplete="off" onSubmit={handleSubmit}>
      <TextField
        label="Comments"
        variant="filled"
        fullWidth
        multiline
        rows={4}
        margin="normal"
        value={comments}
        onChange={(e) => setComments(e.target.value)}
        helperText="Provide comments for the issue"
      />
      <TextField
        label="Name"
        variant="filled"
        fullWidth
        required
        margin="normal"
        value={name}
        onChange={(e) => setName(e.target.value)}
        helperText="*required"
        error={!!error}
      />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <Button type="submit" variant="contained" color="primary">
        Submit
      </Button>
    </Box>
  );
}

export default FeedbackPage;
