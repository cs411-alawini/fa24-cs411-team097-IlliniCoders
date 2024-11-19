import React, { useState, ChangeEvent } from 'react';
import "./SearchTable.css"
import axios from 'axios'
// Users can search based on a region ID
interface st {
    data: any[];
}


    

const SearchTable : React.FC<st> = ({data}) => {
    const data_array: any[] = Object.values(data)[0] || [];
    const rows = data_array.map((element:any[], idx:number) => {
        console.log(Object.values(data)[0][0]);
        console.log(element);
        return (
        <tr key={idx}>
        <td>{element[0]}</td>
        <td>{element[1]}</td>
        <td>{element[2]}</td>
        <td>{element[3]}</td>
        <td>{element[4]}</td>
        </tr>
        );
    });
    const sort_column = (column: String) =>{
    //TODO
    console.log(column);
    };
    const handleSearch = () => {
    console.log(data);
    };
    return (
        <div>
                <table className='table'>            
                <thead>
                            <tr>
                                    <th>
                                    <button  onClick={()=> sort_column("")}>Region Id</button>
                                </th>
                                <th>
                                    <button  onClick={()=> sort_column("")}>Date</button>
                                </th>
                                 <th>
                                    <button  onClick={()=> sort_column("")}>Max Wind</button>
                                </th>                               
                                <th>
                                    <button  onClick={()=> sort_column("")}>Min Pressure</button>
                                </th>

                                <th>
                                    <button  onClick={()=> sort_column("")}>Name</button>
                                </th>




                            </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
    );
};


export default SearchTable;
