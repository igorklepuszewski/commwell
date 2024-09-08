// Sidebar.js
import React from 'react';
import { List, ListItem, ListItemText, Box, ListItemIcon } from '@mui/material';
import { EmojiEvents, Feedback, Logout } from '@mui/icons-material';
import { Link, useLocation } from 'react-router-dom';

const Sidebar = () => {
  const location = useLocation();

  // Define the current path to highlight the active tab
  const currentPath = location.pathname;

  return (
    <Box sx={{ width: '80px', height: '100vh', bgcolor: '#f7f8fc', boxShadow: 3 }}>
      <List sx={{ pt: 5 }}>
        {/* Sidebar item for Kudos and Badges */}
        <ListItem
          button
          component={Link}
          to="/profile"
          sx={{
            flexDirection: 'column',
            color: currentPath === '/profile' ? '#673ab7' : '#757575',
            '&:hover': { bgcolor: '#e3f2fd' },
            ...(currentPath === '/profile' && {
              bgcolor: '#f3e5f5', // Highlight the current page
              borderRight: '4px solid #673ab7', // Purple highlight on the left
            }),
          }}
        >
          <ListItemIcon sx={{ minWidth: 'auto', color: currentPath === '/kudos' ? '#673ab7' : '#757575' }}>
            <EmojiEvents />
          </ListItemIcon>
          <ListItemText primary="Kudos" sx={{ fontSize: '12px', mt: 1 }} />
        </ListItem>

        {/* Sidebar item for Write Feedback */}
        <ListItem
          button
          component={Link}
          to="/kudos"
          sx={{
            flexDirection: 'column',
            color: currentPath === '/kudos' ? '#673ab7' : '#757575',
            '&:hover': { bgcolor: '#e3f2fd' },
            ...(currentPath === '/kudos' && {
              bgcolor: '#f3e5f5',
              borderRight: '4px solid #673ab7',
            }),
          }}
        >
          <ListItemIcon sx={{ minWidth: 'auto', color: currentPath === '/kudos' ? '#673ab7' : '#757575' }}>
            <Feedback />
          </ListItemIcon>
          <ListItemText primary="Write Kudos" sx={{ fontSize: '12px', mt: 1 }} />
        </ListItem>

        {/* Sidebar item for Logout/Profile
        <ListItem
          button
          component={Link}
          to="/logout"
          sx={{
            flexDirection: 'column',
            color: currentPath === '/logout' ? '#673ab7' : '#757575',
            '&:hover': { bgcolor: '#e3f2fd' },
            ...(currentPath === '/logout' && {
              bgcolor: '#f3e5f5',
              borderRight: '4px solid #673ab7',
            }),
          }}
        >
          <ListItemIcon sx={{ minWidth: 'auto', color: currentPath === '/profile' ? '#673ab7' : '#757575' }}>
            <Logout />
          </ListItemIcon>
          <ListItemText primary="Logout" sx={{ fontSize: '12px', mt: 1 }} />
        </ListItem> */}
      </List>
    </Box>
  );
};

export default Sidebar;
