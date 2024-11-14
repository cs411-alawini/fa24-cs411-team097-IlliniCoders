import React, { useState, ChangeEvent } from 'react';

// Users can search based on a region ID
const NaturalDisasterSearch: React.FC = () => {
    const [query, setQuery] = useState<string>(''); // Define the state type as string
    // const [ results] = useState([]);

    const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value); // Update the query with the input value
    };

    const sendData = async () => {
        try {
            const res = await fetch('http://127.0.0.1:5000/data', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify({query}),
        });
        } catch (error) {
            console.error("Error sending data:", error);
        }
    };

    const handleSearch = () => {
        // set results to be what the database returns
        console.log(`Query: ${query}`); // Perform search logic here
        sendData();
    };

    return (
        <div>
            <input
                type="text"
                value={query}
                onChange={handleInputChange}
                placeholder="Enter Natural Disaster..."
                style={{ padding: '8px', fontSize: '16px' }}
            />
            <button onClick={handleSearch} style={{ padding: '8px', marginLeft: '8px' }}>
                Enter
            </button>
        </div>
    );
};

export default NaturalDisasterSearch;
