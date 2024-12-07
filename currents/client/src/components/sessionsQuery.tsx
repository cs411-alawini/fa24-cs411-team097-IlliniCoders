import React from "react";
import axios from "axios";

interface SessionsQueryProps {
  get_result: (result: any[]) => void;
}

const formData = {
  sessions: "yes",
};

const SessionsQuery: React.FC<SessionsQueryProps> = ({ get_result }) => {
  const sendData = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/data", formData, {
        headers: { "Content-Type": "application/json" },
      });
      console.log("Response:", res.data);
      get_result(res.data.data);
    } catch (error) {
      console.error("Error sending data:", error);
      // Add user feedback for errors here
    }
  };

  return (
    <div className="advanced-query-container">
      <button
        onClick={sendData}
        className="search-button"
        aria-label="Perform advanced query"
      >
        Explore your previous searches!
      </button>
      
    </div>
  );
};

export default SessionsQuery;