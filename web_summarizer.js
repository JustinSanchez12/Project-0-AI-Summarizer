import React, { useState } from 'react';
import axios from 'axios';

export default function WebSummarizer() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse('');
    try {
      const res = await axios.post('http://localhost:5000/summarize', { input });
      setResponse(res.data.output);
    } catch (err) {
      setResponse('An error occurred: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <h1 className="text-3xl font-bold mb-6">🧠 Web Summarizer</h1>
      <form onSubmit={handleSubmit} className="w-full max-w-xl">
        <textarea
          className="w-full p-4 rounded-lg shadow-md border border-gray-300 mb-4"
          rows={6}
          placeholder="Enter URL or text here..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button
          type="submit"
          className="w-full bg-blue-600 text-white font-semibold py-3 px-6 rounded-lg hover:bg-blue-700 transition"
        >
          {loading ? 'Summarizing...' : 'Summarize'}
        </button>
      </form>

      <div className="w-full max-w-xl mt-6 bg-white p-4 rounded-lg shadow">
        <h2 className="text-xl font-semibold mb-2">Summary</h2>
        <pre className="whitespace-pre-wrap text-gray-800">
          {response || 'No summary yet.'}
        </pre>
      </div>
    </div>
  );
} 
