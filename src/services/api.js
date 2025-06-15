import axios from "axios";
import Cookies from "js-cookie";
import loadenv from "@/services/loadenv";

let baseURL;

import.meta.env.MODE === "development"
  ? console.log("Development mode")
  : console.log("Production mode");

import.meta.env.MODE === "development"
  ? (baseURL = `${import.meta.env.VITE_SITE_URL}/api`)
  : (baseURL = "/api");

export default axios.create({
  // baseURL: 'http://127.0.0.1:8000/api',

  baseURL: baseURL,
  /* baseURL: loadenv.env_url, */
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    "X-CSRFToken": Cookies.get("csrftoken"),
  },
});
