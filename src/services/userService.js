import api from '@/services/api'
import store from '@/stores/vuex'

export default {
    async createProfile(data) {        
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `/profilesetup/`
        return await api.post(baseURL, 
        data, {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    )

    } catch (e) {
         if (e.status == 401) {
            store.dispatch('refreshToken')
              .then(() => {
                const token = store.state.token
                this.updateProfile(playerKey, data, token)
              })
          }
        // eslint-disable-next-line no-console
        console.error(e);
        return e.response;
    } 
    },
    async fetchProfile(playerKey) {
        
        try { 
            const token = store.state.token
            var baseURL
            baseURL = `/profile/${playerKey}/`
            const response = await api.get(baseURL, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            })
            return response.data
            
        } catch (e) {
            if (e.response.status == 401) {
                // eslint-disable-next-line 
                console.error("Invalid token")
                // eslint-disable-next-line 
                console.log("Token:" + token);
                store.dispatch('refreshToken')
                  .then(() => {
                    const token = store.state.token
                    this.fetchProfile(playerKey, token)
                  })
              }
            // eslint-disable-next-line 
            console.error(e);
            return e.response
        } 
    },
    async fetchProfilePublic(playerKey) {
      try { 
          
          var baseURL
          baseURL = `/public/profile/${playerKey}/`
          const response = await api.get(baseURL, {

          })
          return response.data
          
      } catch (e) {
          if (e.response.status == 401) {
              // eslint-disable-next-line 
              console.error("Error: " + e.response.status)

            }
          // eslint-disable-next-line 
          console.error(e);
          return e.response
      } 
    },
    async updateProfile(playerKey, data) {        
        try { 
            const token = store.state.token
            var baseURL
            baseURL = `/profile/${playerKey}/`
            return await api.patch(baseURL, 
            data, {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }
        )
            
            
        } catch (e) {
            if (e.response.status == 401) {
                store.dispatch('refreshToken')
                  .then(() => {
                    const token = store.state.token
                    this.updateProfile(playerKey, data, token)
                  })
              }
            // eslint-disable-next-line no-console
            console.error(e);
            return e.response
        } 
    },
    async createUser(payload) {
        try {
          return await api.post(`users/`, payload)
        } catch (e) {
          return e.response
        }
    },
    async fetchUser(userId, token) {
        try {
          return await api.get(`users/${userId}/`, {
            headers: {
              "Authorization": `Bearer ${token}`
            }
          })
        } catch (e) {
          if (e.response.status == 401) {
            store.dispatch('refreshToken')
              .then(() => {
                const token = store.state.token
                this.fetchUser(userId, token)
              })
          }
          return e.response
        }
    },
    async updateUser(userId, data) {
        try {
          const token = store.state.token
          return await api.patch(`users/${userId}/`,
            data, {
              headers: {
                "Authorization": `Bearer ${token}`
              }
            }
          )
        } catch (e) {
          if (e.response.status == 401) {
            store.dispatch('refreshToken')
              .then(() => {
                const token = store.state.token
                this.updateUser(userId, token, data)
              })
          }
        return e.response
        }
    },
}