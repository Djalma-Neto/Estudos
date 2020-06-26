import React, { Component }from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Bot from './Button/Button.js';
import Valor from './Store/valores.js';
import * as serviceWorker from './serviceWorker';

class Stores extends Component {
  constructor(props){
    super(props)

    this.state = {
      valor1: 'Desligado',
      valor2: 'Desligado',
      valor3: 'Desligado'
    }
  }
  setValor1 = (val) => {
    if (this.state.valor1.toLowerCase() === 'ligado') {
      this.setState({
        valor1: 'Desligado'
      })
      return 0
    }
    this.setState({
      valor1: 'Ligado'
    })
  }
  setValor2 = (val) => {
    if (this.state.valor2.toLowerCase() === 'ligado') {
      this.setState({
        valor2: 'Desligado'
      })
      return 0
    }
    this.setState({
      valor2: 'Ligado'
    })
  }
  setValor3 = (val) => {
    if (this.state.valor3.toLowerCase() === 'ligado') {
      this.setState({
        valor3: 'Desligado'
      })
      return 0
    }
    this.setState({
      valor3: 'Ligado'
    })
  }
  render() {
    var {valor1, valor2, valor3} = this.state
    return(
      <body>
        <h1>valor1: {valor1}</h1>
        <h1>valor2: {valor2}</h1>
        <h1>valor3: {valor3}</h1>
        <div class='Header'>
          <div class='Btn'>
            <li><Bot onClick={() => this.setValor1()} nome='Power_1' /></li>
            <li><Bot onClick={() => this.setValor2()} nome='Power_2' /></li>
            <li><Bot onClick={() => this.setValor3()} nome='Power_3' /></li>
          </div>
      </div>
      </body>
    )
  }
}

const rootElement = document.getElementById('root')
ReactDOM.render(<Stores />, rootElement);

