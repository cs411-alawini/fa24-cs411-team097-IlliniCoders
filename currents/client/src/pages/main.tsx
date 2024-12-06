import React, {useState} from "react";
import NaturalDisasterSearch from "../components/naturalDisasterSearch";
import SearchTable from "../components/searchTable"
 
const MainPage: React.FC = () => {
    const [result, set_result] = useState<any[]>([]);
    return (
        <div style={{ backgroundColor: 'lavender', minHeight: '100vh', padding: '20px', boxSizing: 'border-box' }}>
            <h1 style={{ fontStyle: 'italic', marginBottom: '20px', textAlign: 'center' }}>Currents</h1>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h2 style={{ margin: 0 }}>Data Playground</h2>
                    <NaturalDisasterSearch get_result={set_result}/>
                </div>
                <SearchTable data1={result} data2={[]}/>
                <div>
                </div>
            </div>
        </div>
    );
}  
export default MainPage;