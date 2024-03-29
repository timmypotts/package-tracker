import React from "react"
import { makeStyles } from "@material-ui/core/styles"
import { Card, CardActionArea, CardActions, CardContent, CardMedia, Button } from "@material-ui/core/"
import USPS from "../assets/usps.png"
import UPS from "../assets/ups.png"
import Pin from "../assets/map-marker.png"
import FedEx from "../assets/fedex.png"
import Typography from "@material-ui/core/Typography"
import PackageService from "../services/package-service"
import GoogleMapReact from "google-map-react"

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
    marginRight: "1%",
    marginLeft: "auto",
  },
  left: {
    marginLeft: "1%",
  },
})

export default function PackageCard(props) {
  const classes = useStyles()

  function DisplayDate() {
    if (props.statuscode === "IT") {
      console.log(props.expected)
      return (
        <div>
          <Typography variant="body2" color="textSecondary" component="p">
            <span style={{ color: "orange", fontWeight: "bold" }}>{props.status}</span> : {props.carrierstatus}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            <span style={{ fontWeight: "bold" }}>Expected Delivery : </span> {props.expected}
          </Typography>
        </div>
      )
    } else if (props.statuscode === "DE") {
      return (
        <Typography variant="body2" color="textSecondary" component="p">
          <span style={{ color: "green", fontWeight: "bold" }}>{props.status}</span> : {props.carrierstatus}
        </Typography>
      )
    } else {
      return (
        <Typography variant="body2" color="textSecondary" component="p">
          <span style={{ fontWeight: "bold" }}>{props.status}</span> : {props.carrierstatus}
        </Typography>
      )
    }
  }

  // Delete package function
  function deletePackage(event) {
    console.log("DELETING PACKAGE")
    PackageService.deletePackage(props.itemId).then((res) => {
      console.log(res)
      window.location.reload()
    })
  }

  const Marker = () => <img src={Pin} alt="Map Marker" width="25px" height="25px" />

  function CourierIcon() {
    if (props.courier === "USPS") {
      return <img src={USPS} alt="USPS logo" width="25px" height="25px" />
    } else if (props.courier === "UPS") {
      return <img src={UPS} alt="UPS logo" width="25px" height="25px" />
    } else if (props.courier === "FedEx") {
      return <img src={FedEx} alt="FedEx logo" width="25px" height="25px" />
    }
  }

  return (
    <Card className={classes.root}>
      <CardActionArea>
        <div style={{ height: "350px", width: "100%" }}>
          <GoogleMapReact
            bootstrapURLKeys={{ key: process.env.GOOGLE_MAPS_KEY }}
            defaultCenter={{
              lat: props.lat,
              lng: props.lon,
            }}
            defaultZoom={11}
          >
            <Marker lat={props.lat} lng={props.lon} />
          </GoogleMapReact>
        </div>
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {props.item}
          </Typography>
          <DisplayDate />
        </CardContent>
      </CardActionArea>
      <CardActions disableSpacing>
        <CourierIcon className={classes.left} /> : {props.tracking}
        <Button onClick={deletePackage} color="secondary" className={classes.right}>
          Delete
        </Button>
      </CardActions>
    </Card>
  )
}
