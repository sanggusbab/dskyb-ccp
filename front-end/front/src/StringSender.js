import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';

function StringSender() {
  const [inputText, setInputText] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    try {
      const res = await axios.post('http://localhost:9000/api/send-string', { text: inputText });
      setResponse(res.data.response); // Access the 'response' key
      setError('');
    } catch (error) {
      setError('Error sending the string.');
    }
  };

  return (
    <div className="string-sender-container">
      <div className="header">
        <h1 className="team-name">Dskyb</h1>
        <h2 className="subheading">Dynamic Sky Brain Control</h2>
      </div>
      <input
        type="text"
        placeholder="Enter a string"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button className="submit-button" onClick={handleSubmit}>
        Send to the Server
      </button>
      {error && <p className="error-text">{error}</p>}
      {response && (
        <p className="response-text">
          Received from the Server: {response}
        </p>
      )}
    </div>
  );
}

export default StringSender;
