import './App.css';
import {Route, BrowserRouter, Redirect, Switch} from 'react-router-dom';
import MainLayout from './layouts/mainLayout'
import Home from './views/home'
import Home2 from './views/home2'
import Error from './views/NotFound'

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <RouteWrapper exact path="/" component={Home} layout={MainLayout} />
        <RouteWrapper exact path="/teste" component={Home2} layout={MainLayout} />


        <Route path="/404" component={Error} />
        <Redirect to="/404" />
      </Switch>
    </BrowserRouter>
  );
}

function RouteWrapper({ component: Component, layout: Layout, ...rest}) {
  return (
    <Route {...rest} component={(props) =>
      <Layout {...props}>
        <Component {...props} />
      </Layout>
    } />
  );
}

export default App;
