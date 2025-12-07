import axios from "axios";

// La URL viene desde tu .env
const API_URL = import.meta.env.VITE_API_URL;

export const api = axios.create({
  baseURL: API_URL,
  withCredentials: true, // si tu backend usa cookies / sesiones
});
