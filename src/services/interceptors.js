import api from "@/services/api";
import router from '@/router'
import store from '@/stores/vuex'

export default function setup() {

//Interceptors
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem("t");
    const refreshToken = localStorage.getItem("r")
    if (token) {
      config.headers.common["Authorization"] = token;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);
api.interceptors.response.use(
  response => {
    if (response.status === 200 || response.status === 201) {
      console.log("Refresh fucntion not detected")
      return Promise.resolve(response);
    } else {
      console.log(response.data)
      if (response.data.detail === "Token is invalid or expired") {
        consonle.log("Refresh token function called")
        return Promise.resolve(response);
      }
      else {
        console.log("Refresh fucntion not detected")
        console.log(response.data)
        return Promise.reject(response);
      }
    }
  },
  error => {
    if (error.response.status) {
      switch (error.response.status) {
        case 400:
         
         //do something
          break;
        case 401:
          console.log(error.response.data.detail)
          console.log("session expired")
          // RefreshTokenCheck returned 401
          if (error.response.data.detail === "Token is invalid or expired") {
            console.log("Refresh token function called")
            router.replace({
            path: "/logout",
            query: { redirect: router.currentRoute.fullPath }
           }); 
          }
          // User login failed 
          else if (error.response.data.detail === "No active account found with the given credentials") {
            console.log("Login failed")
          }
          else {
          // Any other 401 failure will result in reissuing 
            console.log("Refresh fucntion not detected")
            store.dispatch('refreshToken')
          }
          break;
        case 403:
          router.replace({
            path: "/logout",
            query: { redirect: router.currentRoute.fullPath }
          });
           break;
        /* case 404:
          alert('page not exist');
            router.replace({
            path: "/logout",
            query: { redirect: router.currentRoute.fullPath }
          }); 
          break; */
        case 502:
         setTimeout(() => {
            router.replace({
              path: "/logout",
              query: {
                redirect: router.currentRoute.fullPath
              }
            });
          }, 1000);
      }
      //console.log(error.response)
      return Promise.resolve(error.response);
    }
  }
);

}
