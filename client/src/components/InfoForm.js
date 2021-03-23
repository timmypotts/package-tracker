import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";

const useStyles = makeStyles((theme) => ({
  root: {
    "& .MuiTextField-root": {
      margin: theme.spacing(1),
      width: "25ch",
    },
  },
}));

export default function MultilineTextFields() {
  const classes = useStyles();
  const [value, setValue] = React.useState("Controlled");

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <form className={classes.root} noValidate autoComplete="off">
      <div>
        <TextField
          id="standard"
          label="Item"
          multiline
          rowsMax={1}
          value={value}
          onChange={handleChange}
        />
        <TextField
          id="standard"
          label="Tracking Number"
          multiline
          rowsMax={1}
          value={value}
          onChange={handleChange}
        />
        <TextField
          id="standard"
          label="Courier"
          multiline
          rowsMax={1}
          value={value}
          onChange={handleChange}
        />
      </div>
    </form>
  );
}
