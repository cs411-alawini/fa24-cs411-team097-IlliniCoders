import React from "react";
import "./searchTable.css";

interface st {
  data1: any[]; 
  data2: any[]; 
}

const SearchTable: React.FC<st> = ({ data1, data2 }) => {
  const dataArray1 = Array.isArray(data1) ? data1 : [];
  const dataArray2 = Array.isArray(data2) ? data2 : [];

  const rows1 = dataArray1.map((element: any, idx: number) => {
    const values = Array.isArray(element) ? element : Object.values(element);

    return (
      <tr key={idx}>
        <td>{values[0]}</td>
        <td>{values[1]}</td>
        <td>{values[2]}</td>
        <td>{values[3]}</td>
        <td>{values[4]}</td>
      </tr>
    );
  });

  const rows2 = dataArray2

  return (
    <div>
      <h3>Natural Disasters</h3>
      <table className="table">
        <thead>
          <tr>
            <th>Region ID</th>
            <th>Date</th>
            <th>Name</th>
            <th>Maximum wind speed (kts)</th>
            <th>Minimum pressure (mb)</th>
          </tr>
        </thead>
        <tbody>{rows1}</tbody>
      </table>
      <h3>Ocean Species</h3>
      <table className="table">
        <thead>
          <tr>
            <th>Region ID</th>
            <th>Scientific name</th>
            <th>Year first seen</th>
            <th>Year last seen</th>
            <th>Minimum habitat depth</th>
            <th>Maximum habitat depth</th>
          </tr>
        </thead>
        <tbody>{rows2}</tbody>
      </table>
    </div>
  );
};

export default SearchTable;
