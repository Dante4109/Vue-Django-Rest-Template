import api from '@/services/api'
import store from '@/stores/vuex'

export default {

async postImage(bodyFormData) {        
    try { 
        const token = store.state.token
        var baseURL  
        baseURL = `/image/`
        const response = await api.post(baseURL, 
        bodyFormData, {
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "multipart/form-data"
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
async fetchImage(imageId) {
    
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `/image/${imageId}/`
        const response = await api.get(baseURL, {
            headers: {
                "Authorization": `Bearer ${token}`,
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
                this.fetchimage(imageId, token)
                })
            }
        // eslint-disable-next-line 
        console.error(e);
        return e.response
    } 
    },
async fetchImageFromUUID(imageUUID) {
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `/imageUUID/${imageUUID}/`
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
                this.fetchimageFromUUID(imageUUID, token)
                })
            }
        // eslint-disable-next-line 
        console.error(e);
        return e.response
    } 
    },
async deleteImage(image_id) {        
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `/image/${image_id}/`
        return await api.delete(baseURL, 
        {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    )
        
} catch (e) {
    // eslint-disable-next-line no-console
    console.error(e);
    // eslint-disable-next-line no-console
    console.log(e.response);
    return e.response
        }
    }, 
async fetchImageCollection() {
    try { 
        const token = store.state.token
        var baseURL
        baseURL = `/image/`
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
