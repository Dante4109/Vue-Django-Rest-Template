import api from '@/services/api'

export default {
    async checkResetToken(data){
        try{
            var baseURL
            baseURL = `/password_reset/validate_token/`
            return await api.post(baseURL, data)
        }catch (e) {
            if (e.response.status == 404) {
                // eslint-disable-next-line 
                console.error("Invalid token")
                // eslint-disable-next-line 
                console.log("Token:" + resetToken);
              }
            // eslint-disable-next-line no-console
            console.error(e);
            return e.response
        }
    },
    async submitPasswordReset(data){
        try{
            var baseURL
            baseURL = `/password_reset/confirm/`
            return await api.post(baseURL, data)
        }catch (e) {
            if (e.response.status == 404) {
                // eslint-disable-next-line 
                console.error("Invalid token")
                // eslint-disable-next-line 
                console.log("Token:" + resetToken);
              }
            // eslint-disable-next-line no-console
            console.error(e);
            return e.response
        }
    },
    async requestPasswordReset(data){
        try{
            var baseURL
            baseURL = `/password_reset/`
            return await api.post(baseURL, data)
        }catch (e) {
            if (e.response.status == 404) {
                // eslint-disable-next-line 
                console.error("Invalid token")
                // eslint-disable-next-line 
                console.log("Token:" + resetToken);
              }
            // eslint-disable-next-line no-console
            console.error(e);
            return e.response
        }
    },
  }