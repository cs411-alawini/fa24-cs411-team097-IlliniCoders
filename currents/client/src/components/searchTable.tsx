import React from "react";
import "./searchTable.css";

interface st {
  data: any[]; 
}

const SearchTable: React.FC<st> = ({ data }) => {
  const data_array: any[] = Array.isArray(data) ? data : [];
  const rows = data_array.map((element: any, idx: number) => {
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

  return (
    <div>
      <table className="table">
        <thead>
          <tr>
            <th>Region Id</th>
            <th>Date</th>
            <th>Name</th>
            <th>Max Wind (kts)</th>
            <th>Min Pressure (mb)</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  );
};

export default SearchTable;
