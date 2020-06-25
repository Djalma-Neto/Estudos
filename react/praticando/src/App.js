import React from 'react';
import logo from './logo.svg';
import './App.css';
import Bot from './Button';


var Tag = 'Hello World!'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

function Teste () {
  return (
    <div>
      <Bot />
      {Tag}
    </div>
  )
}

function Full () {
  return (
    <div>
      {Teste()}
      {App()}
    </div>
  )
}

export default Full;
