import React, { useState } from "react";
import InfoForm from "../InfoForm";
import Container from "@material-ui/core/Container";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core";

const useStyles = makeStyles({
  title: {
    fontWeight: "bold",
  },
});

export default function Home() {
  const classes = useStyles();
  const [view, setView] = useState(false);

  const toggle = () => {
    if (view === false) {
      setView(true);
    } else {
      setView(false);
    }
  };
  return (
    <Container maxWidth="lg">
      <header>
        <Typography className={classes.title} variant="h2">
          Trackage
        </Typography>
        <h3>
          Keep track of all your packages without having to repeatedly scour
          your inbox for that one email with the tracking number.
        </h3>
      </header>
      <Button
        size="large"
        variant="contained"
        onClick={toggle}
        color="secondary"
      >
        + Track a Package
      </Button>
      <br />
      {view ? <InfoForm /> : null}
    </Container>
  );
}
