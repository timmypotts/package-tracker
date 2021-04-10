import React, { useState } from "react";
import { makeStyles } from "@material-ui/core";
import {
  InputLabel,
  MenuItem,
  FormControl,
  Select,
  TextField,
  Button,
} from "@material-ui/core";

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
  const handleChange = (event) => {
    setItem(event.target.value);
  };
  return (
    <form className="form" noValidate autoComplete="off">
      <TextField label="Item Name" required />

      <TextField label="Tracking Number" required />

      <FormControl className={classes.formControl}>
        <InputLabel>Courier</InputLabel>
        <Select>
          <MenuItem value={"UPS"}>UPS</MenuItem>
          <MenuItem value={"USPS"}>USPS</MenuItem>
          <MenuItem value={"FedEx"}>FedEx</MenuItem>
        </Select>
      </FormControl>

      <Button
        className={classes.button}
        size="large"
        variant="contained"
        color="primary"
      >
        Go
      </Button>
    </form>
  );
}
