import axios from "axios";
import authHeader from "./auth-header";
import { config } from "../Constants";

const API_URL = config.url.API_URL;

class PackageService {
  addPackage(item, tracking, courier, pubId) {
    return axios
      .post(
        API_URL + "/api/packages/",
        {
          item,
          tracking,
          courier,
          pubId,
        },
        { headers: authHeader() }
      )
      .then((response) => {
        console.log(response);
        return response.data;
      });
  }

  getUserPackages(public_id) {
    return axios
      .get(API_URL + "/api/packages/" + public_id)
      .then((response) => {
        var packages = response.data.packages;
        console.log(packages);
        return packages;
      });
  }

  deletePackage(package_id) {
    return axios
      .delete(API_URL + "/api/packages/" + package_id)
      .then((response) => {
        console.log(response);
        return response;
      });
  }
}
export default new PackageService();
