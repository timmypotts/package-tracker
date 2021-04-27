import React, { Component } from "react";
import { makeStyles } from "@material-ui/core/styles";
import {
  Card,
  CardActionArea,
  CardActions,
  CardContent,
  CardMedia,
  Button,
} from "@material-ui/core/";
// import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import { faGithubSquare, faLinkedin } from "@fortawesome/free-brands-svg-icons";
import USPS from "../assets/usps.png";
import UPS from "../assets/ups.png";
import FedEx from "../assets/fedex.png";
import Typography from "@material-ui/core/Typography";
// import MapBox from "./Map";
import MapHolder from "../assets/mapHolder.png";
// import Map from "./Map";

const useStyles = makeStyles({
  root: {
    maxWidth: "100%",
    marginTop: "20px",
    marginBottom: "20px",
  },
  media: {
    height: 350,
  },
  right: {
    float: "right",
  },
});

export default function PackageCard(props) {
  const classes = useStyles();

  function DisplayDate() {
    if (props.expected !== "Invalid date") {
      console.log(props.expected);
      return (
        <div>
          <Typography variant="body2" color="textSecondary" component="p">
            {props.status} : {props.carrierstatus}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Expected Delivery : {props.expected}
          </Typography>
        </div>
      );
    } else {
      return (
        <Typography variant="body2" color="textSecondary" component="p">
          {props.status} : {props.carrierstatus}
        </Typography>
      );
    }
  }

  function CourierIcon() {
    if (props.courier === "USPS") {
      return <img src={USPS} alt="USPS logo" width="25px" height="25px" />;
    } else if (props.courier === "UPS") {
      return <img src={UPS} alt="UPS logo" width="25px" height="25px" />;
    } else if (props.courier === "FedEx") {
      return <img src={FedEx} alt="FedEx logo" width="25px" height="25px" />;
    }
  }

  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          className={classes.media}
          image={MapHolder}
          title="Contemplative Reptile"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {props.item}
          </Typography>
          {/* <Typography variant="body2" color="textSecondary" component="p">
            {props.status} : {props.deliverdate}
          </Typography> */}
          <DisplayDate />
        </CardContent>
      </CardActionArea>
      <CardActions>
        <CourierIcon /> : {props.tracking}
        {/* <Typography className={classes.right}>Status</Typography> */}
      </CardActions>
    </Card>
  );
}
