import React, { useState, useContext } from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Button from "@material-ui/core/Button";
import Container from "@material-ui/core/Container";
import AuthService from "../services/auth-service";
import { UserContext } from "../context/UserContext";

import { Link } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    fontSize: "17px",
    color: "black",
    paddingLeft: "5px",
    paddingRight: "5px",
    float: "left",
  },
  navItems: {
    color: "black",
    float: "right",
  },
}));

export default function NavBar() {
  const classes = useStyles();

  const { user, setUser } = useContext(UserContext);

  return (
    <div className={classes.root}>
      <AppBar position="static" color="white">
        <Toolbar>
          <Container maxWidth="xl">
            <Button className={classes.title} to={"/"} component={Link}>
              Trackage
            </Button>
            {user ? (
              <Button
                className={classes.navItems}
                to={`/${user}/dashboard`}
                activeClassName="active"
                component={Link}
              >
                {user}
              </Button>
            ) : (
              <Button
                className={classes.navItems}
                to="/signup"
                activeClassName="active"
                component={Link}
              >
                Register
              </Button>
            )}

            {user ? (
              <Button
                className={classes.navItems}
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
                className={classes.navItems}
                to="/login"
                activeClassName="active"
                component={Link}
              >
                Log In
              </Button>
            )}
          </Container>
        </Toolbar>
      </AppBar>
    </div>
  );
}
