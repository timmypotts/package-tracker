const prod = {
  url: {
    API_URL: "http://52.72.142.224:3080",
  },
};

const dev = {
  url: {
    API_URL: "http://localhost:9003",
  },
};

export const config = process.env.NODE_ENV === "development" ? dev : prod;
