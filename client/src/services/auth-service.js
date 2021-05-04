import axios from "axios";

// const API_URL = "http://localhost:3080/api/auth/";

class AuthService {
  login(username, password) {
    return axios
      .post("http://54.164.112.2:3080/api/auth/login", {
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
      .post("http://54.164.112.2:3080/api/auth/register", {
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
    console.log("1");
    console.log(x);
    return x;
  }
}

export default new AuthService();
