const axios = require("axios");

const options = {
  method: "GET",
  url: "https://azone-real-time-amazon-data-api.p.rapidapi.com/product-details",
  params: {
    asin: "B0B8G1Q9DM",
    country: "US"
  },
  headers: {
    "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
  }
};

axios.request(options)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
