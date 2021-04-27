import React, { useState, useEffect, useContext } from "react";
import {
  Container,
  Button,
  Typography,
  Grid,
  CircularProgress,
} from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import SearchBar from "material-ui-search-bar";
import AddIcon from "@material-ui/icons/Add";
import RemoveIcon from "@material-ui/icons/Remove";
import InfoForm from "../InfoForm";
import PackageCard from "../PackageCard";
import { UserContext } from "../../context/UserContext";
import AuthService from "../../services/auth-service";
import PackageService from "../../services/package-service";
import moment from "moment";

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
  const [packages, setPackages] = useState();

  const toggle = () => {
    if (view === false) {
      setView(true);
    } else {
      setView(false);
    }
  };

  function loadPackages(id) {
    PackageService.getUserPackages(id).then((res) => {
      if (!res) {
        console.log("error");
        return null;
      }
      setPackages(res);
    });
  }

  // JUST MAKE THE PUBLIC ID A CONTEXT VARIABLE
  function getUser() {
    const user = AuthService.getCurrentUser();
    console.log("2");
    if (user) {
      console.log(user);
      setUser(user.username);
      const pubId = user.pub_id;
      console.log("================ID======================");
      console.log(pubId);
      return pubId;
    } else {
      return { error: "no user" };
    }
  }

  useEffect(() => {
    let id = getUser();
    loadPackages(id);
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
          {packages ? (
            <div>
              {packages.map((x) => (
                <PackageCard
                  key={x.id}
                  postID={x.id}
                  item={x.item}
                  shipdate={moment(x.shipdate).calendar()}
                  status={x.status}
                  expected={moment(x.expected).calendar()}
                  deliverdate={moment(x.deliverdate).calendar()}
                  carrierstatus={x.carrierstatus}
                  tracking={x.tracking}
                  user={x.user}
                  courier={x.courier}
                />
              ))}
            </div>
          ) : (
            <CircularProgress />
          )}
        </Grid>
      </Grid>
    </Container>
  );
}
