import React, { useState } from "react";
import { makeStyles } from "@material-ui/core";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import TextField from "@material-ui/core/TextField";
import NativeSelect from "@material-ui/core/NativeSelect";
import InputBase from "@material-ui/core/InputBase";

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
}));

export default function CustomizedSelects() {
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
    </form>
  );
}
