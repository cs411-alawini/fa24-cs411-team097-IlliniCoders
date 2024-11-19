import React, { useState, ChangeEvent } from 'react';
import axios from 'axios'

interface nds {
    get_result: (result: any[])=>void;
}
const NaturalDisasterSearch: React.FC<nds> = ({get_result}) => {
    const [query, setQuery] = useState<string>(''); // Define the state type as string

    const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
        setQuery(event.target.value); // Update the query with the input value
    };

    const sendData = async () => {
        try {
            const res = await axios.post('http://127.0.0.1:5000/data', {query});
            console.log(res.data);
            get_result(res.data)
            
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
