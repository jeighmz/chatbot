// src/App.js
import React from 'react';
import Chatbot from './Chatbot';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Simple Chatbot</h1>
        <Chatbot />
      </header>
    </div>
  );
}

export default App;