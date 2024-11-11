import React from "react";
import OceanSpeciesSearch from "../components/oceanSpeciesSearch";
import NaturalDisasterSearch from "../components/naturalDisasterSearch";

const MainPage: React.FC = () => {
    return (
        <div style={{ backgroundColor: 'lavender', minHeight: '100vh', padding: '20px', boxSizing: 'border-box' }}>
            <h1 style={{ fontStyle: 'italic', marginBottom: '20px', textAlign: 'center' }}>Currents</h1>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h2 style={{ margin: 0 }}>Search Ocean Species</h2>
                    <OceanSpeciesSearch />
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h2 style={{ margin: 0 }}>Search Natural Disaster</h2>
                    <NaturalDisasterSearch />
                </div>
            </div>
        </div>
    );
}

export default MainPage;
