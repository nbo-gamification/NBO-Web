import React from 'react';
import Route from 'react-router-dom/Route';
import Switch from 'react-router-dom/Switch';
import Login from './login/login';
import './App.css';

const App = () => (
  <Switch>
    <Route exact path="/" component={Login} />
  </Switch>
);

export default App;
