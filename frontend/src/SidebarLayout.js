// SidebarLayout.js
import React from 'react';
import { Box } from '@mui/material';
import Sidebar from './Sidebar';

const SidebarLayout = ({ children }) => {
  return (
    <Box sx={{ display: 'flex', height: '100vh' }}>
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <Box sx={{
        flexGrow: 1,
        backgroundColor: '#f0f4f8',
        p: 3,
        overflowY: 'auto',
      }}>
        {children}
      </Box>
    </Box>
  );
};

export default SidebarLayout;
