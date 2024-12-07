import React from "react";
import "./searchTable.css";

interface st {
  data1: any[];
}

const Sessions: React.FC<st> = ({ data1 }) => {
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
        <td>{values[5]}</td>
        <td>{values[6]}</td>
      </tr>
    );
  });

  return (
    <div>
      <div>
        <h3>Previous Sessions Data</h3>
        <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              <th>Session ID</th>
              <th>Min Latitude</th>
              <th>Max Latitude</th>
              <th>Min Longitude</th>
              <th>Max Longitude</th>
              <th>Rerun?</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>{rows1}</tbody>
        </table>
        </div>
      </div>
    </div>
  );
};

export default Sessions;
