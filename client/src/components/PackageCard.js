import React, { Component } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
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
        <Button size="small" color="primary">
          {props.courier} : {props.tracking}
        </Button>
        <Button size="small" color="primary">
          Courier
        </Button>
        {/* <Typography className={classes.right}>Status</Typography> */}
      </CardActions>
    </Card>
  );
}
