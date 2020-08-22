import React from 'react';
import Navbar from './Components/Navbar';
import Home from './Components/Home';
import About from './Components/About';
import Contact from './Components/Contact';
import Landing from './Components/Landing';
import './App.css';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'

function App() {
  return (
    <Router>
      <div>
        <Navbar/>
        <Switch>
          <Route exact path ="/">
            <Landing/>
          </Route>
          <Route path ="/home">
            <Home name="SRG"/>
          </Route>
          <Route path ="/about">
            <About/>
          </Route>
          <Route path ="/contact">
            <Contact/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
