import React, { Component }from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Bot from './Button/Button.js';
import * as serviceWorker from './serviceWorker';

class App extends Component {
  constructor(props){
    super(props)

    this.state = {
      valor: 0
    }    
  }
  soma = (a, b) => {
    this.setState({
      valor: 10
    })
  }
  sub = (a, b) => {
    this.setState({
      valor: 15
    })
  }
  render() {
    var {valor} = this.state
    return(
      <body>
        <h1>{ valor }</h1>
        <div class='Header'>
          <div class='Btn'>
            <button onClick={() => this.soma(5 ,5)}>click</button>
            <li><Bot onClick={() => this.soma(5 ,5)} nome='5 + 5' /></li>
            <li><Bot onClick={() => this.sub(20 ,5)} nome='20 - 5' /></li>
            <li><Bot onClick= '' nome='Btn3' /></li>
          </div>
       </div>
      </body>
    )
  }
}
const rootElement = document.getElementById('root')
ReactDOM.render(<App />, rootElement);

