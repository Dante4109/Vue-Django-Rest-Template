import api from '@/services/api'

export default {
    async checkVerificationToken(data){
        try{
            var baseURL
            baseURL = `/email_verification/`
            return await api.post(baseURL, data)
        }catch (e) {
            // eslint-disable-next-line no-console
            console.error(e);
            return e.response
        }
    },
  }