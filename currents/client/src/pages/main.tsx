import React, {useState} from "react";
import NaturalDisasterSearch from "../components/naturalDisasterSearch";
import SearchTable from "../components/searchTable"
import AdvancedQuery1 from "../components/advancedQuery1"
import AdvancedQuerySearchTable from "../components/advancedQuerySearchTable"
import AdvancedQuery2 from "../components/advancedQuery2"
import AdvancedQuerySearchTable2 from "../components/advancedQuerySearchTable2"
import AdvancedQuery3 from "../components/advancedQuery3"
import AdvancedQuerySearchTable3 from "../components/advancedQuerySearchTable3"
import AdvancedQuery4 from "../components/advancedQuery4"
import AdvancedQuerySearchTable4 from "../components/advancedQuerySearchTable4"
 
const MainPage: React.FC = () => {
    const [result, set_result] = useState<any[]>([]);
    const [result2, set_result2] = useState<any[]>([]);
    const [result3, set_result3] = useState<any[]>([]);
    const [result4, set_result4] = useState<any[]>([]);
    const [result5, set_result5] = useState<any[]>([]);
    return (
        <div style={{ backgroundColor: 'lavender', minHeight: '100vh', padding: '20px', boxSizing: 'border-box' }}>
            <h1 style={{ fontStyle: 'italic', marginBottom: '20px', textAlign: 'center' }}>Currents</h1>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h2 style={{ margin: 0 }}>Data Playground</h2>
                    <NaturalDisasterSearch get_result={set_result}/>
                </div>
                <SearchTable data1={result[0]} data2={result[1]}/>
                <div>
                </div>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h2 style={{ margin: 0 }}>Advanced Query 1</h2>
                    <AdvancedQuery1 get_result={set_result2}/>
                </div>
                <AdvancedQuerySearchTable data1={result2}/>
                <div>
                </div>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h2 style={{ margin: 0 }}>Advanced Query 2</h2>
                    <AdvancedQuery2 get_result={set_result3}/>
                </div>
                <AdvancedQuerySearchTable2 data1={result3}/>
                <div>
                </div>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h2 style={{ margin: 0 }}>Advanced Query 3</h2>
                    <AdvancedQuery3 get_result={set_result4}/>
                </div>
                <AdvancedQuerySearchTable3 data1={result4}/>
                <div>
                </div>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: '20px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <h2 style={{ margin: 0 }}>Advanced Query 4</h2>
                    <AdvancedQuery4 get_result={set_result5}/>
                </div>
                <AdvancedQuerySearchTable4 data1={result5}/>
                <div>
                </div>
            </div>
        </div>
    );
}  
export default MainPage;