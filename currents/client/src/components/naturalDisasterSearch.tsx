import React, { useState, ChangeEvent } from "react";
import axios from "axios";

interface nds {
  get_result: (result: any[]) => void;
}

const NaturalDisasterSearch: React.FC<nds> = ({ get_result }) => {
  const [formData, setFormData] = useState({
    min_latitude: "",
    max_latitude: "",
    min_longitude: "",
    max_longitude: ""
  });

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({ ...prevState, [name]: value }));
  };

  const sendData = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/data", formData, {
        headers: { "Content-Type": "application/json" }, // Ensure JSON payload
      });
      console.log("Response:", res.data);
      get_result(res.data.data); // Use `data` key from response
    } catch (error) {
      console.error("Error sending data:", error);
    }
  };

  const handleSearch = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault(); // Prevent page reload
    console.log("Form Data:", formData);
    sendData(); // Send form data to the backend
  };

  return (
    <div>
      <form
        onSubmit={handleSearch}
        style={{ padding: "8px", marginLeft: "8px" }}
      >
        <label>
          Minimum Latitude:
          <input
            type="text"
            name="min_latitude"
            value={formData.min_latitude}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Maximum Latitude:
          <input
            type="text"
            name="max_latitude"
            value={formData.max_latitude}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Minimum Longitude:
          <input
            type="text"
            name="min_longitude"
            value={formData.min_longitude}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Maximum Longitude:
          <input
            type="text"
            name="max_longitude"
            value={formData.max_longitude}
            onChange={handleChange}
          />
        </label>
        <br />
        <br />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default NaturalDisasterSearch;