import React, { useState } from "react";
import InfoForm from "../InfoForm";
import Container from "@material-ui/core/Container";
import Button from "@material-ui/core/Button";

export default function Home() {
  return (
    <Container maxWidth="lg">
      <header>
        <h1>Trackage</h1>
        <h3>
          Keep track of all your packages without having to scour your inbox for
          that one email with the tracking number.
        </h3>
      </header>
      <Button variant="contained" color="secondary">
        + Track a Package
      </Button>
      <InfoForm />
    </Container>
  );
}
