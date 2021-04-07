import axios from "axios";

// const API_URL = "http://localhost:3080/api/auth/";

class AuthService {
  login(username, password) {
    return axios
      .post("http://54.205.120.4:3080/api/auth/login", {
        username,
        password,
      })
      .then((response) => {
        if (response.data.token) {
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
      .post("http://localhost:5432/api/auth/register", {
        username,
        email,
        password,
      })
      .then((response) => {
        if (response.data.token) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  getCurrentUser() {
    return JSON.parse(localStorage.getItem("user"));
  }
}

export default new AuthService();
