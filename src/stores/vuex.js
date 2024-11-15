import { createStore } from "vuex";
import api from '@/services/api'
import { jwtDecode } from "jwt-decode";
//import { decode } from 'punycode'
import userService from '@/services/userService'
import imageService from "@/services/imageService";


const store = createStore({
  state: {
    token: localStorage.getItem('t'),
    refreshToken: localStorage.getItem('r'),
    authenticatedUser: localStorage.getItem('u'),
    userProfile: localStorage.getItem('profile'),
    globalDrawer: localStorage.getItem('drawer'),
    isLoggedIn: localStorage.getItem('isLoggedIn'),
    closedBanner: localStorage.getItem('closedBanner'),
    endpoints: {
      obtainToken: "auth/obtain_token/",
      refreshToken: "auth/refresh_token/",
      }
    },
  mutations: {
      updateBanner(state, closed) {
        localStorage.setItem('closedBanner', closed)
        state.closedBanner = closed
          },
      updateDrawer(state, active) {
        localStorage.setItem('globalDrawer', active)
        state.globalDrawer = active
        },
      updateLoggedInState(state, loggedIn){
        localStorage.setItem('isLoggedIn', loggedIn)
        state.isLoggedIn = loggedIn
        },
      updateSessionUser(state, user) {
        localStorage.setItem('u', JSON.stringify(user))
        state.authenticatedUser = JSON.stringify(user)
        },
      updateSessionUserProfile(state, profile) {
        localStorage.setItem('profile', JSON.stringify(profile))
        state.authenticatedUser = JSON.stringify(profile)
        },
      updateToken(state, tokens) {
        localStorage.setItem('t', tokens.access)
        state.token = tokens.access
  
        if(tokens.refresh) {
          localStorage.setItem('r', tokens.refresh)
          state.refreshToken = tokens.refresh
        }
        },
      revokeToken(state) {
        localStorage.removeItem('t')
        state.token = null
        },
      revokeUser(state) {
        localStorage.removeItem('u')
        state.authenticatedUser = null
        }
        },
  actions: {
    logout() {
      this.commit('revokeUser')
      this.commit('revokeToken')
      this.commit('updateLoggedInState', false)
    },
    refreshToken() {
      // eslint-disable-next-line no-console
      console.log("Attempt to get new access token from refresh token.")
      const data = {
        "refresh": this.state.refreshToken
        
      }
      return api.post(this.state.endpoints.refreshToken, data)
      .then((response => {
        if (response.status == 401) {
          console.log("refresh token is invalid.")
          console.log("log out user")
          
        }
        else {
          console.log("refresh token is valid.")
          this.commit('updateToken', response.data)
        }
      }))
        
    },
    obtainToken(state, payload) {
      const data = {
        email: payload.email,
        password: payload.password
      }
  
      return api.post(this.state.endpoints.obtainToken, data)
      .then((response => {
        this.commit('updateToken', response.data)        
        this.commit('updateLoggedInState', true)
        //console.log('Succesful response:' + response)
        return response
      }))
      .catch((e) => {
        //console.log('Bad token exception:' + e.response.data.detail + 'Error status:' + e.response.status)
        return e.response
        })
    },
    async getUserFromToken(state, token) {
      const decodedToken = jwtDecode(token)
      if(decodedToken.user_id) {
        const response = await userService.fetchUser(decodedToken.user_id, token)
        return response.data
      } else { return null }
    },
    inspectToken() {
      const token = this.state.token
      if(token) {
        const decoded = jwtDecode(token)
        const exp = decoded.exp
        const orig_iat = decoded.orig_iat
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200) {
          this.dispatch('refreshToken')
        }
        else if (exp - (Date.now()/1000) < 1800) {
          // do not refresh
          // eslint-disable-next-line no-console
          console.log("User needs to login again")
        }
        else {
          // user needs to log in again
          // eslint-disable-next-line no-console
          console.log("User needs to login again")
        }
      }
    }
  }
})

export default store



