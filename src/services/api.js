import axios from 'axios'
import Cookies from 'js-cookie'
import loadenv from '@/services/loadenv'

export default axios.create({
  // baseURL: 'http://127.0.0.1:8000/api',
  baseURL: '/api',
  /* baseURL: loadenv.env_url, */
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': Cookies.get('csrftoken')
  }
})