import axios from "axios";
import authHeader from "./auth-header";

// const API_URL = "http://localhost:3080/api/";

class PackageService {
  submitPost(item, tracking, courier, user) {
    return axios
      .post(
        "http://localhost:5000/api/packages",
        {
          item,
          tracking,
          courier,
          user,
        },
        { headers: authHeader() }
      )
      .then((response) => {
        console.log(response);
        return response.data;
      });
  }
}
export default new PackageService();
