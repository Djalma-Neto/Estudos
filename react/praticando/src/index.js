import Index from './components/tela_Home'
import Listagem from './components/tela_Reproducao'
import Upload from './components/tela_Upload'
// import Erro404 from './components/erro404';

import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'

ReactDOM.render(
  <BrowserRouter>
      <Switch>
          <Route path="/" exact={true} component={Index} />
          <Route path="/listar" component={Listagem} />
          <Route path="/upload" component={Upload} />
          {/* <Route path="*" component={Erro404} /> */}
      </Switch>
  </ BrowserRouter>
  , document.getElementById('root')
)