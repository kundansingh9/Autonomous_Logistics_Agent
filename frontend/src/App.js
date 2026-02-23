import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!query) return;

    setLoading(true);
    setResult("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/research", {
        query: query,
      });

      setResult(response.data.result);
    } catch (error) {
      setResult("Error connecting to backend.");
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🚚 Autonomous Logistics Research Agent</h1>

      <textarea
        placeholder="Enter logistics research query..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Researching..." : "Start Research"}
      </button>

      {result && (
        <div className="result">
          <h2>📊 Research Output</h2>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default App;