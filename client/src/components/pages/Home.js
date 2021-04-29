import React, { useEffect, useContext } from "react";
import { Container, Button, Typography, Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import shipgif from "../../assets/ship.gif";
import AuthService from "../../services/auth-service";
import { UserContext } from "../../context/UserContext";
import { Link } from "react-router-dom";

const useStyles = makeStyles({
  spacing: {
    marginTop: "30%",
  },
  gifspace: {
    marginTop: "5%",
  },
});

export default function Home() {
  const classes = useStyles();
  const { user, setUser } = useContext(UserContext);

  useEffect(() => {
    const user = AuthService.getCurrentUser();
    if (user) {
      setUser(user.username);
    } else {
      console.log("no user");
    }
  }, []);

  return (
    <Container maxWidth="xl">
      <Grid container spacing={0}>
        <Grid item xs={12} md={6} lg={6}>
          <header>
            <Typography className={classes.spacing} variant="h2">
              Trackage
            </Typography>
            <h3>
              Keep track of all your packages without having to repeatedly scour
              your inbox for that one email with the tracking number.
            </h3>
          </header>
          {user ? (
            <Button
              size="large"
              variant="contained"
              to="/tracking"
              color="primary"
              component={Link}
            >
              + Track a Package
            </Button>
          ) : (
            <Button
              size="large"
              variant="contained"
              to="/login"
              color="primary"
              component={Link}
            >
              + Track a Package
            </Button>
          )}
        </Grid>
        <Grid item xs={false} md={6} lg={6}>
          <img
            className={classes.gifspace}
            src={shipgif}
            alt={"gif of truck"}
          />
        </Grid>
      </Grid>
    </Container>
  );
}
