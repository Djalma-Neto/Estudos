import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import QualquerNome from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(
  <React.StrictMode>
    <QualquerNome />
  </React.StrictMode>,
  document.getElementById('root')
);

serviceWorker.unregister();
