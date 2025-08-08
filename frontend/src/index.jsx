// src/index.jsx
import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import './base.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [meetingCode, setMeetingCode] = useState('');
  const [language, setLanguage] = useState('en');
  const [signLanguage, setSignLanguage] = useState('asl');

  const createMeeting = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/create-meeting/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ language, sign_language: signLanguage })
      });
      const data = await res.json();
      setMeetingCode(data.code);
    } catch (err) {
      alert('Failed to create meeting');
    }
  };

  return (
    <div className="container mt-5">
      <div className="text-center">
        <h1 className="text-primary">SignBridge</h1>
        <p className="text-muted">Connect with anyone using sign language interpretation in real-time.</p>
        <div className="overview-box mb-4">
          <p><strong>How it works:</strong> This app helps bridge communication between hearing and deaf users using sign language recognition and live video/audio. Start a meeting and share the code with others to join!</p>
        </div>

        <div className="form-group mb-3">
          <label htmlFor="language">Select Spoken Language:</label>
          <select id="language" className="form-control" value={language} onChange={e => setLanguage(e.target.value)}>
            <option value="en">English</option>
            <option value="es">Spanish</option>
          </select>
        </div>

        <div className="form-group mb-3">
          <label htmlFor="sign-language">Select Sign Language:</label>
          <select id="sign-language" className="form-control" value={signLanguage} onChange={e => setSignLanguage(e.target.value)}>
            <option value="asl">ASL (American Sign Language)</option>
            {/* More languages can be added later */}
          </select>
        </div>

        <button className="btn btn-highlight" onClick={createMeeting}>Create Meeting</button>

        {meetingCode && (
          <div className="alert alert-success mt-4">
            Meeting created! Share this code: <strong>{meetingCode}</strong>
          </div>
        )}
      </div>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
