import React, { useState, useEffect } from 'react';
import { Box, Tabs, Tab, Typography, Paper, List, ListItem, ListItemText } from '@mui/material';

function ProfilePage() {
  const [value, setValue] = useState(0);
  const [badges, setBadges] = useState([]);  // State for badges
  const [kudosesReceived, setKudosesReceived] = useState([]);  // State for kudos (inbox)
  const [kudosesSent, setKudosesSent] = useState([]);  // State for kudos (inbox)

  // Fetch badges from /api/badge
  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (value === 0) {
      fetch('http://localhost:8001/api/badge/', {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((data) => setBadges(data))
        .catch((error) => console.error('Error fetching badges:', error));
    }
  }, [value]);  // Only fetch badges when the Badges tab is selected

  // Fetch kudos from /api/kudos
  useEffect(() => {
    const token = localStorage.getItem('access_token');
    const userId = localStorage.getItem('userId')
    if (value === 1) {
      fetch(`http://localhost:8001/api/kudos/?receiver=${userId}`, {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((data) => setKudosesReceived(data))
        .catch((error) => console.error('Error fetching kudos:', error));
    }
  }, [value]);  // Only fetch kudos when the Inbox tab is selected

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    const userId = localStorage.getItem('userId')
    if (value === 2) {
      fetch(`http://localhost:8001/api/kudos/?sender=${userId}`, {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((data) => setKudosesSent(data))
        .catch((error) => console.error('Error fetching kudos:', error));
    }
  }, [value]);  // Only fetch kudos when the Inbox tab is selected

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Paper
      sx={{
        maxWidth: 800,
        margin: '0 auto',
        borderRadius: '12px',
        boxShadow: '0 4px 10px rgba(0,0,0,0.1)',
        overflow: 'hidden',
      }}
    >
      <Tabs
        value={value}
        onChange={handleChange}
        sx={{
          backgroundColor: '#f4f4f4',
          borderBottom: '1px solid #ddd',
        }}
        TabIndicatorProps={{
          style: {
            backgroundColor: '#3500CC', // Purple underline for selected tab
            height: '3px',
          },
        }}
      >
        <Tab
          label="Badges"
          sx={{
            color: "#000"
          }}
        />
        <Tab
          label="Inbox"
          sx={{
            color: "#000"
          }}
        />
        <Tab
          label="Send"
          sx={{
            color: "#000"
          }}
        />
      </Tabs>

      {/* Badges Tab Content */}
      {value === 0 && (
        <Box sx={{ p: 3 }}>
          <Typography sx={{ fontSize: '24px', fontWeight: 'bold' }}>Badges</Typography>
          <List>
            {badges.length > 0 ? (
              badges.map((badge) => (
                <ListItem key={badge.id}>
                  <ListItemText
                    primary={badge.name}
                  />
                </ListItem>
              ))
            ) : (
              <Typography>No badges gotten.</Typography>
            )}
          </List>
        </Box>
      )}

      {/* Inbox (Kudos) Tab Content */}
      {value === 1 && (
        <Box sx={{ p: 3 }}>
          <Typography sx={{ fontSize: '24px', fontWeight: 'bold' }}>Inbox</Typography>
          <List>
            {kudosesReceived.length > 0 ? (
              kudosesReceived.map((kudos) => (
                <ListItem key={kudos.id}>
                  <ListItemText
                    primary={kudos.message.trim() === "" ? "Empty Kudos" : kudos.message}
                  />
                </ListItem>
              ))
            ) : (
              <Typography>No kudos received.</Typography>
            )}
          </List>
        </Box>
      )}

      {/* Send Tab Content */}
      {value === 2 && (
        <Box sx={{ p: 3 }}>
        <Typography sx={{ fontSize: '24px', fontWeight: 'bold' }}>Outbox</Typography>
        <List>
          {kudosesSent.length > 0 ? (
            kudosesSent.map((kudos) => (
              <ListItem key={kudos.id}>
                <ListItemText
                  primary={kudos.message.trim() === "" ? "Empty Kudos" : kudos.message}
                  secondary={kudos.receiver_mail}
                />
              </ListItem>
            ))
          ) : (
            <Typography>No kudos sent.</Typography>
          )}
        </List>
      </Box>
      )}
    </Paper>
  );
}

export default ProfilePage;
