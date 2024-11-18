import React, { useState } from "react";
import OceanSpeciesSearch from "../components/oceanSpeciesSearch";
import NaturalDisasterSearch from "../components/naturalDisasterSearch";
import LatSlider from "../components/latSlider"
import LongSlider from "../components/longSlider"
import SearchTable from "../components/SearchTable"

const MainPage: React.FC = () => {
    const [result, set_result] = useState([]);
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
                    <NaturalDisasterSearch get_result={set_result}/>
                </div>
                <div style={{ marginTop: '40px' }}> {/* Optional spacing for layout */}
                    <LongSlider />
                    <LatSlider />
                </div>
                <SearchTable data={result}/>
                <div>

                </div>
            </div>
        </div>
    );
}

export default MainPage;
