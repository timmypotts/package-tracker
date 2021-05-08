import axios from "axios";
import { config } from "../Constants";

const API_URL = config.url.API_URL;

class AuthService {
  login(username, password) {
    return axios
      .post(API_URL + "/api/auth/login", {
        username,
        password,
      })
      .then((response) => {
        if (response.data.token) {
          console.log(response);
          localStorage.setItem("user", JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem("user");
  }

  register(username, email, password) {
    return axios
      .post(API_URL + "/api/auth/register", {
        username,
        email,
        password,
      })
      .then((response) => {
        console.log(response);
        if (response.data.token) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  getCurrentUser() {
    let x = JSON.parse(localStorage.getItem("user"));
    return x;
  }
}

export default new AuthService();
