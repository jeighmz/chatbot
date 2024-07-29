// src/Chatbot.js
import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import './Chatbot.css';

const Chatbot = () => {
  const [messages, setMessages] = useState([
    { text: 'Hello! How can I help you today?', isBot: true }
  ]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (input.trim() === '') return;
  
    const newMessages = [...messages, { text: input, isBot: false }];
    setMessages(newMessages);
    setInput('');
  
    try {
      const response = await axios.post('http://127.0.0.1:5000/generate', {
        prompt: input
      });
  
      const botMessage = response.data.generated_text;
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: botMessage, isBot: true }
      ]);
    } catch (error) {
      console.error('Error fetching response from the server:', error);
      if (error.response) {
        console.error('Server responded with:', error.response.data);
      }
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: 'Sorry, I am having trouble responding right now.', isBot: true }
      ]);
    }
  };
  
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div className="chatbot-container">
      <div className="messages-container">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.isBot ? 'bot' : 'user'}`}>
            <ReactMarkdown>{message.text}</ReactMarkdown>
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;