import api from '@/services/api'
import store from '@/stores/vuex'

export default {

async createData(url, data) {        
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `/${url}/`
        const response = await api.post(baseURL, 
        data, {
            headers: {
                "Authorization": `Bearer ${token}`
                }
            }
        )
        return response.data

        } catch (e) {
            // eslint-disable-next-line no-console
            console.error(e);
            // eslint-disable-next-line no-console
            console.log(e.response);
            return e.response
            } 
    },
    async fetchData(url, DataId) {
    
        try {
            const token = store.state.token
            var baseURL
            baseURL = `${url}/${DataId}/`
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
                        this.fetchData(DataId, token)
                    })
            }
            // eslint-disable-next-line 
            console.error(e);
            return e.response
        }
    },

    async fetchDataPublic(url, DataId) {
        
        try {
            var baseURL
            baseURL = `${url}/${DataId}/`
            const response = await api.get(baseURL, {

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
                        this.fetchData(DataId, token)
                    })
            }
            // eslint-disable-next-line 
            console.error(e);
            return e.response
        }
    },
        
async fetchDataPublicList(url) {
        
        try { 
            var baseURL
            baseURL = `${url}`
            const response = await api.get(baseURL, {

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
                    this.fetchData(DataId, token)
                    })
                }
            // eslint-disable-next-line 
            console.error(e);
            return e.response
        }

    },
async fetchDataUUID(url, DataUUID) {
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `${url}/${DataUUID}`
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
                this.fetchDataUUID(DataUUID, token)
                })
            }
        // eslint-disable-next-line 
        console.error(e);
        return e.response
    } 
    },
async updateData(url, DataId, data) {        
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `${url}/${DataId}/`
        return await api.patch(baseURL, data, {
            headers: {
                Authorization: `Bearer ${token}`
            }
        });
    } catch (e) {
        // eslint-disable-next-line no-console
        console.error(e);
        // eslint-disable-next-line no-console
        console.log(e.status);
        return e.response
            }
    }, 
async deleteData(url, id) {        
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `${url}/${id}/`;
        const response = await api.delete(baseURL, {
        headers: {
          Authorization: `Bearer ${token}`
        }
        });
        return response.data
    } catch (e) {
        // eslint-disable-next-line no-console
        console.error(e);
        // eslint-disable-next-line no-console
        console.log(e.status);
        return e
            }
        }, 
async fetchCollection(url) {
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `/${url}/`
        const response = await api.get(baseURL, {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        })
        // eslint-disable-next-line 
        //console.log(response.data)
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
    } 
  }
