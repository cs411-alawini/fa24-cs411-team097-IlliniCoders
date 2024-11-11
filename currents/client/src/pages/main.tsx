import React from "react";
import SearchBar from "../components/searchBar";


const MainPage: React.FC = () => {
    return (
        <div style={{ backgroundColor: 'lavender', minHeight: '100vh', padding: '20px', boxSizing: 'border-box', textAlign: 'center' }}>
            <h1 style={{ fontStyle: 'italic', marginBottom: '20px' }}>Currents</h1>
            <SearchBar />
        </div>
    );
}

export default MainPage;