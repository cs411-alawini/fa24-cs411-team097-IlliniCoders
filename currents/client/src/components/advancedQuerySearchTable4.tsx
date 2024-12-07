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
      </tr>
    );
  });

  return (
    <div>
      <div>
        <h3>Do you want to find ocean species that live in regions where there were at least 5 days in which the precipitation was over 100 (cm)?</h3>
        <div className="table-container">
        <table className="table">
          <thead>
            <tr>
              <th>Region ID</th>
              <th>Scientific Name</th>
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
