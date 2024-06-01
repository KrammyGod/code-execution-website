import React, { useState } from 'react';
import Editor from '@monaco-editor/react';
import axios from 'axios';

const App = () => {
  const [code, setCode] = useState<string>('');
  const [result, setResult] = useState<string>('');

  const handleTestCode = async () => {
    try {
      const response = await axios.post('http://localhost:8000/test', { code });
      setResult(response.data.result);
    } catch (error) {
      setResult('Error running code');
    }
  };

  const handleSubmitCode = async () => {
    try {
      const response = await axios.post('http://localhost:8000/submit', { code });
      setResult(response.data.result);
    } catch (error) {
      setResult('Error submitting code');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <Editor
        height="50vh"
        defaultLanguage="python"
        defaultValue="# Write your Python code here"
        onChange={(value) => setCode(value || '')}
      />
      <div className="mt-4">
        <button className="btn btn-primary" onClick={handleTestCode}>
          Test Code
        </button>
        <button className="btn btn-secondary ml-4" onClick={handleSubmitCode}>
          Submit
        </button>
      </div>
      <div className="mt-4">
        <h2>Result:</h2>
        <pre>{result}</pre>
      </div>
    </div>
  );
};

export default App;
