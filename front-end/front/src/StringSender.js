import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';

function StringSender() {
  const [Location1_x, setLocation1_X] = useState('');
  const [Location1_y, setLocation1_Y] = useState('');
  const [Location2_x, setLocation2_X] = useState('');
  const [Location2_y, setLocation2_Y] = useState('');
  const [inputText, setInputText] = useState('');
  const [userId, setUserId] = useState('');

  const [response, setResponse] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    try {
      const currentTime = new Date().toISOString().slice(0, 19);
      const res = await axios.post('http://localhost:8000/request', {
        Location1_x: Location1_x,
        Location1_y: Location1_y,
        Location2_x: Location2_x,
        Location2_y: Location2_y,
        text: inputText,
        currentTime: currentTime,
        userId: userId
      });
      setResponse(res.data.response);
      setError('');
    } catch (error) {
      setError('Error sending the string.');
    }
  };

  const generateRandomData = () => {
    const getRandomNumber = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

    setUserId(`user_${getRandomNumber(1, 1000)}`);
    setLocation1_X(getRandomNumber(200, 800).toString());
    setLocation1_Y(getRandomNumber(200, 800).toString());
    setLocation2_X(getRandomNumber(200, 800).toString());
    setLocation2_Y(getRandomNumber(200, 800).toString());
    setInputText(`Random string: ${getRandomNumber(1, 100)}`);
  };

  return (
    <div className="string-sender-container">
      <div className="header">
        <h1 className="team-name">Dskyb</h1>
        <h2 className="subheading">Dynamic Sky Brain Control Service</h2>
      </div>
      <div className="text-box-container">
        <div className="styled-input-container">
          <div className='styled-input'>
            <label htmlFor="userId" className="id-label">
              User ID
            </label>
            <input
              id="userId"
              className='id-input-label'
              type="text"
              placeholder="Enter your user ID"
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
            />
          </div>
        </div>
      </div>
      <div>
        <div className="text-box-container">
          <div className="text-box">
            <div className="line"><p>Home</p></div>
            <label htmlFor="Location1_x" className="input-label">
              Location_x
            </label>
            <input
              id="Location1_x"
              type="text"
              placeholder="Enter a Location_x of your home"
              value={Location1_x}
              onChange={(e) => setLocation1_X(e.target.value)}
            />
            <label htmlFor="Location1_y" className="input-label">
              Location_y
            </label>
            <input
              id="Location1_y"
              type="text"
              placeholder="Enter a Location_y of your home"
              value={Location1_y}
              onChange={(e) => setLocation1_Y(e.target.value)}
            />
          </div>
          <div className="text-box">
            <div className="line"><p>Store</p></div>
            <label htmlFor="Location2_x" className="input-label">
              Location_x
            </label>
            <input
              id="Location2_x"
              type="text"
              placeholder="Enter a Location_x of the store"
              value={Location2_x}
              onChange={(e) => setLocation2_X(e.target.value)}
            />
            <label htmlFor="Location2_y" className="input-label">
              Location_y
            </label>
            <input
              id="Location2_y"
              type="text"
              placeholder="Enter a Location_y of the store"
              value={Location2_y}
              onChange={(e) => setLocation2_Y(e.target.value)}
            />
          </div>
        </div>
        <div className="text-box-container">
          <input
            type="text"
            placeholder="Enter a string for datail"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />
        </div>
      </div>
      <div className="text-box-container">
        <button className="submit-button" onClick={handleSubmit}>
          Send to the Server
        </button>

        {/* Apply the new class to the random data button */}
        <button className="submit-button random-data-button" onClick={generateRandomData}>
          Use Random Data
        </button>
      </div>
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
