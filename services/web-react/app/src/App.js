import React, { useState } from "react";
import Home from "./components/pages/Home";
import NavBar from "./components/NavBar";
import Signup from "./components/pages/Signup";
import Login from "./components/pages/Login";
import Tracking from "./components/pages/Tracking";
import { UserContext } from "./context/UserContext";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import "./App.css";

const Routes = () => {
  return (
    <Switch>
      <Route path="/" exact={true} component={Home} />
      <Route path="/signup" exact={true} component={Signup} />
      <Route path="/login" exact={true} component={Login} />
      <Route path="/tracking" exact={true} component={Tracking} />
    </Switch>
  );
};

function App() {
  const [user, setUser] = useState(null);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <Router>
        <div className="App">
          <NavBar />
          <Routes />
        </div>
      </Router>
    </UserContext.Provider>
  );
}

export default App;
