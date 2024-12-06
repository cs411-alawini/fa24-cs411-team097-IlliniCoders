import React, { useState, ChangeEvent } from "react";
import axios from "axios";

interface nds {
  get_result: (result: any[]) => void;
}

const NaturalDisasterSearch: React.FC<nds> = ({ get_result }) => {
  const [formData, setFormData] = useState({
    natural_disaster: "",
    ocean_species: "",
    latitude: "",
    longitude: "",
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
          Natural Disaster:
          <input
            type="text"
            name="natural_disaster"
            value={formData.natural_disaster}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Ocean Species:
          <input
            type="text"
            name="ocean_species"
            value={formData.ocean_species}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Latitude:
          <input
            type="text"
            name="latitude"
            value={formData.latitude}
            onChange={handleChange}
          />
        </label>
        <br />
        <label>
          Longitude:
          <input
            type="text"
            name="longitude"
            value={formData.longitude}
            onChange={handleChange}
          />
        </label>
        <br />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
};

export default NaturalDisasterSearch;
