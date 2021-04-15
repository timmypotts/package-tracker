import React, { useState } from "react";
import { makeStyles } from "@material-ui/core";
import {
  InputLabel,
  MenuItem,
  FormControl,
  Select,
  TextField,
  Button,
  Input,
} from "@material-ui/core";
import PackageService from "../services/package-service";

const useStyles = makeStyles((theme) => ({
  margin: {
    margin: theme.spacing(1),
  },
  formControl: {
    minWidth: 100,
  },
  form: {
    marginTop: 3,
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

  function handleSubmit() {
    console.log("========sending=============");
    PackageService.register(item, tracking, courier).catch((err) => {
      console.log(err);
    });
  }

  const handleChange = (event) => {
    setCourier(event.target.value);
    console.log(courier);
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
        required
      />

      <TextField
        label="Tracking Number"
        value={tracking}
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
          <MenuItem value={"DHL"}>DHL</MenuItem>
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
