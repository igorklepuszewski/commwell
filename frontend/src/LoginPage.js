// src/Login.js
import React, { useState } from "react";
import axios from "axios";
import { TextField, Button, Divider, Container, Box, Typography } from "@mui/material";
import { useNavigate } from 'react-router-dom';  // Import useNavigate


const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();  // Initialize useNavigate

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8001/api/token/", {
        username,
        password,
      });
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);
      localStorage.setItem("userId", response.data.user_id)
      navigate("/profile");  // Redirect to homepage after login
    } catch (error) {
      console.error("Login failed:", error.response.data);
    }
  };

  return (<Container maxWidth="sm">
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      height="100vh"
    >
      <Box
        sx={{
          padding: "40px",
          borderRadius: "15px",
          boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
          backgroundColor: "white",
        }}
      >
        <Typography
          sx={{
            fontSize: "36px",
            fontWeight: "bold",
            textAlign: "center",
            marginBottom: "20px",
          }}
        >
          B3 Kudos
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Login"
            variant="outlined"
            margin="normal"
            fullWidth
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextField
            label="Password"
            variant="outlined"
            type="password"
            margin="normal"
            fullWidth
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <Button
            type="submit"
            variant="contained"
            fullWidth
            sx={{
              mt: 2,
              backgroundColor: "#3600CC",
              color: "#FFFFFF",
              borderRadius: "50px",
              padding: "10px",
              fontSize: "18px",
            }}
          >
            Sign In
          </Button>

          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              mt: 3,
            }}
          >
            <Divider sx={{ flexGrow: 1 }} />
            <Typography sx={{ mx: 2, color: "#888", fontSize: "16px" }}>
              or
            </Typography>
            <Divider sx={{ flexGrow: 1 }} />
          </Box>

          <Button
            variant="outlined"
            fullWidth
            sx={{
              mt: 2,
              borderColor: "#3600CC",
              color: "#3600CC",
              borderRadius: "50px",
              padding: "10px",
              fontSize: "18px",
              borderWidth: "2px",
            }}
          >
            Sign Up
          </Button>
        </form>
      </Box>
    </Box>
  </Container>
);
};

export default LoginPage;
