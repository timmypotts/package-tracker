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
  },
  media: {
    height: 350,
  },
  right: {
    float: "right",
  },
});

export default function PackageCard() {
  const classes = useStyles();

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
            Package Name
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Location
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary">
          More Info
        </Button>
        <Button size="small" color="primary">
          Courier
        </Button>
        {/* <Typography className={classes.right}>Status</Typography> */}
      </CardActions>
    </Card>
  );
}
