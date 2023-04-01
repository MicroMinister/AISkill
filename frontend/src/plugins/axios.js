import axios from 'axios';

const instance = axios.create({
  // Replace with your actual API base URL
  baseURL: 'https://your-api-url.com/',
  timeout: 3000, // Optional: Set a request timeout
});

export default instance;
