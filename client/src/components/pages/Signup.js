import React, { useState, useContext } from "react";
import {
  Avatar,
  Button,
  CssBaseline,
  TextField,
  Link,
  Paper,
  Box,
  Grid,
  Typography,
} from "@material-ui/core/";

import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import { makeStyles } from "@material-ui/core/styles";
import AuthService from "../../services/auth-service";
import CheckUser from "../../context/CheckUser";
import { UserContext } from "../../context/UserContext";

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      <Link color="inherit" href="https://timpotts.xyz/">
        timpotts.xyz
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    height: "100vh",
  },
  image: {
    backgroundImage: "url(https://source.unsplash.com/uBe2mknURG4/)",
    backgroundRepeat: "no-repeat",
    backgroundColor:
      theme.palette.type === "light"
        ? theme.palette.grey[50]
        : theme.palette.grey[900],
    backgroundSize: "cover",
    backgroundPosition: "center",
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  error: {
    color: "red",
  },
}));

export default function Signup() {
  const classes = useStyles();

  //   Form handling

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [error, setError] = useState("");
  const { user, setUser } = useContext(UserContext);
  const [submitting, setSubmitting] = useState(false);

  function checkFields() {
    if (password !== confirm) {
      setError("Passwords do not match");
      return false;
    } else if (
      password === "" ||
      email === "" ||
      username === "" ||
      confirm === ""
    ) {
      setError("Please fill out every field");
      return false;
    }
  }

  function handleSubmit(event) {
    setSubmitting(true);
    event.preventDefault();
    let valid = checkFields();
    if (valid === false) {
      setSubmitting(false);
      console.log("this");
      return;
    } else {
      console.log("========sending=============");
      AuthService.register(username, email, password)
        .then((res) => {
          console.log(res);
          setUser(res.username);
        })
        .catch((err) => {
          console.log(err.status);
          console.log(err);
        });
      setSubmitting(false);
    }
  }

  return (
    <Grid container component="main" className={classes.root}>
      <CssBaseline />
      <CheckUser />
      <Grid item xs={false} sm={4} md={7} className={classes.image} />
      <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign Up
          </Typography>
          <form className={classes.form} onSubmit={handleSubmit} noValidate>
            <TextField
              onChange={(e) => setUsername(e.target.value)}
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="username"
              label="Username"
              type="username"
              id="username"
              autoComplete="current-username"
            />
            <TextField
              onChange={(e) => setEmail(e.target.value)}
              variant="outlined"
              margin="normal"
              required
              fullWidth
              value={email}
              id="email"
              label="Email Address"
              name="email"
              autoComplete="email"
              autoFocus
            />
            <TextField
              onChange={(e) => setPassword(e.target.value)}
              variant="outlined"
              margin="normal"
              required
              fullWidth
              value={password}
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <TextField
              onChange={(e) => setConfirm(e.target.value)}
              variant="outlined"
              margin="normal"
              required
              fullWidth
              value={confirm}
              name="password-confirm"
              label="Confirm Password"
              type="password"
              id="password-confirm"
              autoComplete="current-password"
            />
            {error ? <p className={classes.error}>{error}</p> : null}
            <Button
              type="submit"
              fullWidth
              disabled={submitting}
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Register
            </Button>

            <Box mt={5}>
              <Copyright />
            </Box>
          </form>
        </div>
      </Grid>
    </Grid>
  );
}
