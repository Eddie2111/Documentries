// plots array in a loop using map

import "./styles.css";
//import {useState} from 'react';
import { useCookies } from "react-cookie";
export default function Web() {
  const [cookie, setCookie] = useCookies(["name"]);
  const array = ["cake", "ake", "cae", "ake"];
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
        {
        array.map((array) => <option value={array.value}>{array}</option>)
        }
      </select>
    </div>
  );
}
