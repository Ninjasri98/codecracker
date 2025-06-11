import { useState,useEffect } from 'react'
import './App.css'

function App() {
  const [msg, setMsg] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/ping')
      .then(res => res.json())
      .then(data => setMsg(data.message))
      .catch(err => setMsg("API call failed"));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Code Cracker</h1>
      <p>{msg}</p>
    </div>
  );
}

export default App
