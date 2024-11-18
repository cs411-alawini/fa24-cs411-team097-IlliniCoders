import React, { useState, ChangeEvent } from 'react';
import axios from 'axios'

interface st {
    data: any[];
}

const SearchTable : React.FC<st> = ({data}) => {
    const rows = Object.values(data).map((element, idx) => {
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
            <table>            
                <thead>
                    <tr>
                        <th>
                            <button  onClick={()=> sort_column("")}>?</button>
                        </th>
                        <th>
                            <button  onClick={()=> sort_column("")}>?</button>
                        </th>
                        <th>
                            <button  onClick={()=> sort_column("")}>?</button>
                        </th>                               
                        <th>
                            <button  onClick={()=> sort_column("")}>?</button>
                        </th>
                        <th>
                            <button  onClick={()=> sort_column("")}>?</button>
                        </th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
    );
};


export default SearchTable;