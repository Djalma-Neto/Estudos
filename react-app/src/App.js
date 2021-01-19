import './App.css'
import {Route, BrowserRouter, Redirect, Switch} from 'react-router-dom'

import Home from './views/home'
import Home2 from './views/home2'
import Error from './views/NotFound'

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/teste" exact component={Home2} />


        <Route path="/404" component={Error} />
        <Redirect to="/404" />
      </Switch>
    </BrowserRouter>
  );
}

export default App;
