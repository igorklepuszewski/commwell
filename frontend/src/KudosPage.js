import React, { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  TextField,
  Button,
  Container,
  MenuItem,
} from '@mui/material';

const KudosPage = () => {
  const [toWhom, setToWhom] = useState(''); // This will store the PK of the receiver
  const [category, setCategory] = useState(''); // This will store the ID of the selected category
  const [message, setMessage] = useState('');
  const [users, setUsers] = useState([]);
  const [categories, setCategories] = useState([]);
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState('');

  // Fetch users from API
  useEffect(() => {
    const fetchUsers = async () => {
      const token = localStorage.getItem('access_token');
      try {
        const response = await fetch('http://localhost:8001/api/user/', {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });
        if (response.ok) {
          const data = await response.json();
          setUsers(data);
        } else {
          setError('Failed to fetch users');
        }
      } catch (err) {
        console.error('Error fetching users:', err);
        setError('Error fetching users');
      }
    };

    fetchUsers();
  }, []);

  // Fetch categories from API
  useEffect(() => {
    const fetchCategories = async () => {
      const token = localStorage.getItem('access_token');
      try {
        const response = await fetch('http://localhost:8001/api/kudoscategory/', {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });
        if (response.ok) {
          const data = await response.json();
          setCategories(data);
        } else {
          setError('Failed to fetch categories');
        }
      } catch (err) {
        console.error('Error fetching categories:', err);
        setError('Error fetching categories');
      }
    };

    fetchCategories();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('access_token');
    const kudosData = {
      receiver: toWhom,  // Now sending the receiver's PK
      category: category,  // Now sending the selected category ID
      message: message,
    };

    try {
      const response = await fetch('http://localhost:8001/api/kudos/', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(kudosData),
      });

      if (response.ok) {
        setSuccessMessage('Kudos successfully sent!');
        setToWhom('');
        setCategory('');
        setMessage('');
      } else {
        setError('Failed to send kudos');
      }
    } catch (err) {
      console.error('Error sending kudos:', err);
      setError('Error sending kudos');
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        backgroundColor: '#f0f0f0',
      }}
    >
      <Container maxWidth="md" sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <Box
          sx={{
            padding: '40px',
            borderRadius: '15px',
            boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.1)',
            backgroundColor: 'white',
            width: '100%',
          }}
        >
          <Typography
            variant="h4"
            sx={{
              textAlign: 'center',
              mb: 3,
              fontWeight: 'bold',
            }}
          >
            Write kudos
          </Typography>

          {error && (
            <Typography color="error" sx={{ textAlign: 'center', mb: 3 }}>
              {error}
            </Typography>
          )}

          {successMessage && (
            <Typography color="primary" sx={{ textAlign: 'center', mb: 3 }}>
              {successMessage}
            </Typography>
          )}

          <form onSubmit={handleSubmit}>
            {/* Row with two dropdowns */}
            <Box sx={{ display: 'flex', gap: 2, mb: 3 }}>
              <TextField
                select
                label="To whom"
                value={toWhom}
                onChange={(e) => setToWhom(e.target.value)}
                fullWidth
                variant="outlined"
              >
                {users.length > 0 ? (
                  users.map((user) => (
                    <MenuItem key={user.id} value={user.id}>
                      {user.email}
                    </MenuItem>
                  ))
                ) : (
                  <MenuItem disabled>No users found</MenuItem>
                )}
              </TextField>

              <TextField
                select
                label="Badge Category"
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                fullWidth
                variant="outlined"
              >
                {categories.length > 0 ? (
                  categories.map((cat) => (
                    <MenuItem key={cat.id} value={cat.id}>
                      {cat.name}
                    </MenuItem>
                  ))
                ) : (
                  <MenuItem disabled>No categories found</MenuItem>
                )}
              </TextField>
            </Box>

            {/* Text area */}
            <TextField
              label="Message"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              fullWidth
              multiline
              rows={4}
              variant="outlined"
              sx={{ mb: 3 }}
            />

            {/* Submit button */}
            <Button
              type="submit"
              variant="contained"
              fullWidth
              sx={{
                backgroundColor: '#3600CC',
                color: '#FFFFFF',
                borderRadius: '50px',
                padding: '10px',
                fontSize: '18px',
                '&:hover': {
                  backgroundColor: '#28009E',
                },
              }}
            >
              Send!
            </Button>
          </form>
        </Box>
      </Container>
    </Box>
  );
};

export default KudosPage;
