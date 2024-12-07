import React from "react";
import axios from "axios";

interface AdvancedQueryProps {
  get_result: (result: any[]) => void;
}

const formData = {
  advanced_query: "4",
};

const AdvancedQuery4: React.FC<AdvancedQueryProps> = ({ get_result }) => {
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
        Let's find out!
      </button>
    </div>
  );
};

export default AdvancedQuery4;