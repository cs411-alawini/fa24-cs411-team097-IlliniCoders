import React, { useState, ChangeEvent } from 'react';

// Users can search based on a region ID
const OceanSpeciesSearch: React.FC = () => {
    const [query, setQuery] = useState<string>(''); // Define the state type as string
    const [ results] = useState([]);

    const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value); // Update the query with the input value
    };

    const handleSearch = () => {
        // set results to be what the database returns
        console.log(`Query: ${query}`); // Perform search logic here
    };

    return (
        <div>
            <input
                type="text"
                value={query}
                onChange={handleInputChange}
                placeholder="Enter OceanSpecies..."
                style={{ padding: '8px', fontSize: '16px' }}
            />
            <button onClick={handleSearch} style={{ padding: '8px', marginLeft: '8px' }}>
                Enter
            </button>
        </div>
    );
};

export default OceanSpeciesSearch;
