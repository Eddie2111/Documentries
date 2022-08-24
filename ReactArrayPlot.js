// plots array in a loop using map

import "./styles.css";
//import {useState} from 'react';
import { useCookies } from "react-cookie";
export default function Web() {
  const [cookie, setCookie] = useCookies(["name"]);
  const array = ["cake", "ake", "cae", "ake"];
  const value = ["1", "2", "3", "4"];
  function x(newName) {
    if (newName === "x") {
      setCookie("name", newName, { path: "/" });
    }
  }
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see something happen!</h2>
      <p onClick={x("x")}>ppp</p>
      <select>
        {array.map((array, value) => (
          <option value={value}>{array}</option>
        ))}
      </select>
    </div>
  );
}


// plots objects in react
import "./styles.css";
//import {useState} from 'react';
import { useCookies } from "react-cookie";
export default function Web() {
  const [cookie, setCookie] = useCookies(["name"]);
  const employee = {
    value:"21",
    value1:"22",
    value2:"23"
  };
  
  function x(newName) {
    if (newName === "x") {
      setCookie("name", newName, { path: "/" });
    }
  }
  return (
    
      <div>
        {/* 👇️ iterate object KEYS */}
        {Object.keys(employee).map((key, index) => {
          return (
            <div key={index}>
              <h2>
                {key}: {employee[key]}
              </h2>
  
              <hr />
            </div>
          );
        })}
  
        <br />
        <br />
        <br />
  
        {/* 👇️ iterate object VALUES */}
        {Object.values(employee).map((value, index) => {
          return (
            <div key={index}>
              <h2>{value}</h2>
  
              <hr />
            </div>
          );
        })}
      </div>
    );
  }
  
