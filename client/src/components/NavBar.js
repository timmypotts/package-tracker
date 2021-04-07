import React, { useState, useContext } from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

import AuthService from "../services/auth-service";
import { UserContext } from "../context/UserContext";

import { NavLink as RRNavLink, Link } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function NavBar() {
  const classes = useStyles();

  const { user, setUser } = useContext(UserContext);

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Trackage
          </Typography>
          {user ? (
            <Button
              style={{ color: "white" }}
              to={`/${user}/dashboard`}
              activeClassName="active"
              component={Link}
            >
              {user}
            </Button>
          ) : (
            <Button
              style={{ color: "white" }}
              to="/signup"
              activeClassName="active"
              component={Link}
            >
              Register
            </Button>
          )}

          {user ? (
            <Button
              style={{ color: "white" }}
              to="/"
              activeClassName="active"
              component={Link}
              onClick={() => {
                AuthService.logout();
                setUser(null);
              }}
            >
              Log Out
            </Button>
          ) : (
            <Button
              style={{ color: "white" }}
              to="/login"
              activeClassName="active"
              component={Link}
            >
              Log In
            </Button>
          )}
        </Toolbar>
      </AppBar>
    </div>
  );
}
