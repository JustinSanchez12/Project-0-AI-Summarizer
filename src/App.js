import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const response = await fetch('http://localhost:8000/summarize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      console.log('Response data:', data); // Debug log
      
      if (typeof data.summary !== 'string') {
        console.error('Unexpected summary format:', data.summary);
        throw new Error('Invalid response format from server');
      }
      
      setSummary(data.summary);
    } catch (error) {
      console.error('Error:', error);
      setError('Error occurred while summarizing the text.');
      setSummary('');
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <div className="w-full max-w-2xl bg-white rounded-lg shadow-md p-8 flex flex-col items-center">
        <h1 className="text-4xl font-bold mb-8 text-center text-gray-800">Project 0: AI Text Summarizer</h1>
        
        <form onSubmit={handleSubmit} className="w-full space-y-6 flex flex-col items-center">
          <div className="w-full flex flex-col items-center">
            <textarea
              id="text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              className="w-full max-w-xl rounded-lg border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 min-h-[200px] p-4 text-lg text-center"
              placeholder="Enter Your Prompt Here..."
              required
            />
          </div>
          
          <div className="flex justify-center w-full">
            <button
              type="submit"
              disabled={loading}
              className="w-48 py-3 px-6 border border-transparent rounded-lg shadow-sm text-lg font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 transition-colors duration-200"
            >
              {loading ? 'Summarizing...' : 'Enter'}
            </button>
          </div>
        </form>
        
        {error && (
          <div className="mt-8 p-4 bg-red-50 text-red-700 rounded-lg text-center w-full max-w-xl">
            {error}
          </div>
        )}
        
        {summary && (
          <div className="mt-8 w-full flex flex-col items-center">
            <h2 className="text-2xl font-semibold mb-4 text-center text-gray-800">Summary</h2>
            <div className="bg-gray-50 p-6 rounded-lg w-full max-w-xl">
              <p className="text-gray-700 whitespace-pre-wrap text-lg leading-relaxed text-center">{summary}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App; 