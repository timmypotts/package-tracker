import React, { useState, useEffect } from "react";
import { makeStyles } from "@material-ui/core";
import {
  InputLabel,
  MenuItem,
  FormControl,
  Select,
  TextField,
  Button,
} from "@material-ui/core";
import PackageService from "../services/package-service";
import AuthService from "../services/auth-service";

const useStyles = makeStyles((theme) => ({
  margin: {
    margin: theme.spacing(1),
  },
  formControl: {
    minWidth: 100,
  },
  form: {
    marginTop: 3,
    minWidth: "100%",
  },
  button: {
    marginTop: 6,
    marginLeft: 10,
  },
}));

export default function InfoForm() {
  const classes = useStyles();
  const [item, setItem] = useState("");
  const [tracking, setTracking] = useState("");
  const [courier, setCourier] = useState("");
  const [pubId, setPubId] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    PackageService.addPackage(item, tracking, courier, pubId)
      .then((res) => {
        console.log(res);
        window.location.reload();
      })
      .catch((err) => {
        console.log(err);
      });
  }

  useEffect(() => {
    const user = AuthService.getCurrentUser();
    if (user) {
      setPubId(user.pub_id);
    } else {
      console.log("no user");
    }
  }, []);

  const handleChange = (event) => {
    setCourier(event.target.value);
  };

  return (
    <form
      className="form"
      noValidate
      onSubmit={handleSubmit}
      autoComplete="off"
    >
      <TextField
        label="Item Name"
        value={item}
        onChange={(e) => {
          setItem(e.target.value);
        }}
        style={{
          margin: "0 auto",
          minWidth: "20%",
        }}
        required
      />

      <TextField
        label="Tracking Number"
        value={tracking}
        style={{
          margin: "0 auto",
          minWidth: "25%",
        }}
        onChange={(e) => {
          setTracking(e.target.value);
        }}
        required
      />

      <FormControl className={classes.formControl}>
        <InputLabel>Courier</InputLabel>
        <Select name="name" value={courier} onChange={handleChange}>
          <MenuItem value={"UPS"}>UPS</MenuItem>
          <MenuItem value={"USPS"}>USPS</MenuItem>
          <MenuItem value={"FedEx"}>FedEx</MenuItem>
        </Select>
      </FormControl>

      <Button
        className={classes.button}
        type="submit"
        size="large"
        variant="contained"
        color="primary"
      >
        Go
      </Button>
    </form>
  );
}
