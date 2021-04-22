import axios from "axios";
import authHeader from "./auth-header";

// const API_URL = "http://localhost:3080/api/";

class PackageService {
  addPackage(item, tracking, courier, pubId) {
    return axios
      .post(
        "http://localhost:5000/api/packages/",
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
      .get("http://localhost:5000/api/packages/" + public_id)
      .then((response) => {
        var packages = response.data.packages;
        // const sortByDate = (packages) => {
        //   const sorter = (a, b) => {
        //     return (
        //       new Date(b.deliverdate).getTime() -
        //       new Date(a.deliverdate).getTime()
        //     );
        //   };
        //   packages.sort(sorter);
        // };
        // sortByDate(packages);
        // console.log(packages);
        console.log(packages);
        return packages;
      });
  }
}
export default new PackageService();
