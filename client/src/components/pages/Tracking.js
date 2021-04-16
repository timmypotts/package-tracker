import React, { useState, useEffect, useContext } from "react";
import { Container, Button, Typography, Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import SearchBar from "material-ui-search-bar";
import AddIcon from "@material-ui/icons/Add";
import RemoveIcon from "@material-ui/icons/Remove";
import InfoForm from "../InfoForm";
import PackageCard from "../PackageCard";
import { UserContext } from "../../context/UserContext";
import AuthService from "../../services/auth-service";

const useStyles = makeStyles({
  spacing: {
    marginTop: "5%",
  },
  searchContainer: {
    justifyContent: "center",
  },
  searchBar: {
    width: "50%",
    marginLeft: "auto",
    marginRight: "auto",
  },
});

export default function Tracking() {
  const classes = useStyles();

  const [search, setSearch] = useState("");
  const { user, setUser } = useContext(UserContext);
  const [view, setView] = useState(false);

  const toggle = () => {
    if (view === false) {
      setView(true);
    } else {
      setView(false);
    }
  };

  useEffect(() => {
    const user = AuthService.getCurrentUser();
    if (user) {
      setUser(user.username);
    } else {
      console.log("no user");
    }
  }, []);

  return (
    <Container maxWidth="lg">
      {/* <CheckUser /> */}
      <Grid container spacing={3}>
        <Grid item xs={12} sm={12} md={12} lg={12} xl={12}>
          <header>
            <Typography className={classes.spacing} variant="h2">
              Packages
            </Typography>
          </header>
        </Grid>
        <Grid
          item
          xs={8}
          sm={6}
          md={6}
          lg={6}
          xl={6}
          className={classes.searchContainer}
        >
          <SearchBar
            onChange={(e) => setSearch(e.target.value)}
            margin="normal"
            className={classes.searchBar}
            value={search}
            name="search"
            type="label"
            id="label"
            //   autoComplete="current-username"
          />
        </Grid>
        <Grid item xs={4} sm={6} md={6} lg={6} xl={6}>
          {view ? (
            <Button
              size="large"
              variant="contained"
              color="default"
              onClick={toggle}
            >
              <RemoveIcon />{" "}
            </Button>
          ) : (
            <Button
              size="large"
              variant="contained"
              color="primary"
              onClick={toggle}
            >
              <AddIcon />
            </Button>
          )}
        </Grid>
        <Grid item xl={12} lg={12} md={12} sm={12} xs={12}>
          {view ? <InfoForm /> : null}
        </Grid>
        <Grid item xs={12} sm={12} md={12} lg={12} xl={12}>
          <PackageCard />
        </Grid>
      </Grid>
    </Container>
  );
}
