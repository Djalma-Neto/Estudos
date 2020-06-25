import React from 'react';
import logo from './logo.svg';
import './App.css';
import Bot from './Button/Button';

function App() {
  return (
    <body>
      <div class='Header'>
  <div><h1>{ valor }</h1></div>
        <div class='Btn'>
          <li><Bot onClick={() => soma(5+5)} nome='5 + 5' /></li>
          <li><Bot onClick= {sub(20-5)} nome='20 - 5' /></li>
          <li><Bot onClick= '' nome='Btn3' /></li>
        </div>
      </div>
    </body>
  );
}

export default App;
