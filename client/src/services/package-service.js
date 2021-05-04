import axios from "axios";
import authHeader from "./auth-header";

// const API_URL = "http://localhost:3080/api/";

class PackageService {
  addPackage(item, tracking, courier, pubId) {
    return axios
      .post(
        "http://52.72.142.224:3080/api/packages/",
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
      .get("http://52.72.142.224:3080/api/packages/" + public_id)
      .then((response) => {
        var packages = response.data.packages;
        console.log(packages);
        return packages;
      });
  }

  deletePackage(package_id) {
    return axios
      .delete("http://52.72.142.224:3080/api/packages/" + package_id)
      .then((response) => {
        console.log(response);
        return response;
      });
  }
}
export default new PackageService();
