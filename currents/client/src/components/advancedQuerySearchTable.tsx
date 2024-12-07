import React from "react";
import "./searchTable.css";

interface st {
  data1: any[];
}

const SearchTable: React.FC<st> = ({ data1 }) => {
  const dataArray1 = Array.isArray(data1) ? data1 : [];

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

  return (
    <div>
      <div>
        <h3>Do you want to find the average weather metrics for each region during natural disasters?</h3>
        <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              <th>Region ID</th>
              <th>Date</th>
              <th>Average Max Temperature</th>
              <th>Average Precipitation</th>
              <th>Average Min Temperature</th>
            </tr>
          </thead>
          <tbody>{rows1}</tbody>
        </table>
        </div>
      </div>
    </div>
  );
};

export default SearchTable;
