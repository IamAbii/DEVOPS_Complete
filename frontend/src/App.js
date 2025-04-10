import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import config from './config.json'; // Import configuration

function App() {
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  
  // Use backend URL from configuration
  const { backendUrl } = config;
  
  // UPDATED: Improved error handling and response processing
  const handleClick = async () => {
    setLoading(true); // Set loading state to true while request is being made
    try {
      // Make API call to backend
      const res = await axios.get(`${backendUrl}/api/getJoke`);
      
      // UPDATED: Handle both object and string responses properly
      if (typeof res.data === 'object' && res.data.joke) {
        // If the response is an object with a joke property (new format)
        setResponse(res.data.joke);
      } else {
        // For backward compatibility with original format
        setResponse(res.data);
      }
      
      // Log successful response for debugging
      console.log('Successful response:', res.data);
      
    } catch (error) {
      // UPDATED: More detailed error logging
      console.error('Error details:', error);
      
      // Show a more specific error message if available
      if (error.response) {
        // The server responded with a status code outside the 2xx range
        console.error('Error response:', error.response.data);
        setResponse(`Error ${error.response.status}: ${error.response.data.message || 'Server error'}`);
      } else if (error.request) {
        // The request was made but no response was received
        console.error('Error request:', error.request);
        setResponse('No response received from server. Please check your network connection.');
      } else {
        // Something happened in setting up the request
        setResponse('Error occurred while fetching data. Check console for details.');
      }
    } finally {
      setLoading(false); // Set loading state back to false after request is completed
    }
  };

  // ADDED: Test function to verify backend connectivity
  const testBackend = async () => {
    try {
      const res = await axios.get(`${backendUrl}/api/test`);
      console.log("Backend test response:", res.data);
      alert("Backend connection successful!");
    } catch (error) {
      console.error("Backend test failed:", error);
      alert("Backend connection failed. Check console for details.");
    }
  };

  return (
    <div className="container">
      <h1 className="heading">You are viewing the frontend.</h1>
      <div className="content">
        <p className="info">Need a smile? Click here for a quick mood lifter!</p>
        <button className="button" onClick={handleClick} disabled={loading}>
          {loading ? 'Loading...' : 'Click'}
        </button>
        
        {/* ADDED: Test button for debugging */}
        <button className="button test-button" onClick={testBackend} style={{marginLeft: '10px', backgroundColor: '#4a90e2'}}>
          Test Backend
        </button>
        
        {response && <p className="response">{response}</p>}
      </div>
    </div>
  );
}

export default App;
