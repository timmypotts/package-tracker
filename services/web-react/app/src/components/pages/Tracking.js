import React, { useState, useEffect, useContext } from "react";
import {
  Container,
  Button,
  Typography,
  Grid,
  CircularProgress,
} from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import AddIcon from "@material-ui/icons/Add";
import RemoveIcon from "@material-ui/icons/Remove";
import InfoForm from "../InfoForm";
import PackageCard from "../PackageCard";
import { UserContext } from "../../context/UserContext";
import AuthService from "../../services/auth-service";
import PackageService from "../../services/package-service";
import SearchIcon from "@material-ui/icons/Search";
import moment from "moment";

const useStyles = makeStyles((theme) => ({
  spacing: {
    marginTop: "5%",
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: "100%",
    position: "absolute",
    pointerEvents: "none",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  inputRoot: {
    color: "inherit",
  },
}));

export default function Tracking() {
  const classes = useStyles();

  const [search, setSearch] = useState("");
  const { setUser } = useContext(UserContext);
  const [view, setView] = useState(false);
  const [packages, setPackages] = useState([]);
  const [message, setMessage] = useState(null);

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
        setMessage("You are not currently tracking any packages.");
        return;
      }
      setPackages(res);
    });
  }

  // JUST MAKE THE PUBLIC ID A CONTEXT VARIABLE
  function getUser() {
    const user = AuthService.getCurrentUser();

    if (user) {
      setUser(user.username);
      const pubId = user.pub_id;
      return pubId;
    } else {
      return { error: "no user" };
    }
  }

  function RenderResults() {
    if (packages.length) {
      return (
        <div>
          {packages.map((x) => (
            <PackageCard
              key={x.id}
              itemId={x.id}
              item={x.item}
              shipdate={moment(x.shipdate).calendar()}
              status={x.status}
              statuscode={x.statuscode}
              expected={moment(x.expected).format("dddd MMM Do")}
              deliverdate={moment(x.deliverdate).calendar()}
              carrierstatus={x.carrierstatus}
              tracking={x.tracking}
              user={x.user}
              courier={x.courier}
            />
          ))}
        </div>
      );
    } else if (message !== null) {
      return <h2>{message}</h2>;
    } else {
      return <CircularProgress />;
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
        ></Grid>
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
          <RenderResults />
        </Grid>
      </Grid>
    </Container>
  );
}
