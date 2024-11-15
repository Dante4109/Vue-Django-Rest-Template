/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

import mitt from 'mitt'

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'


const app = createApp(App)
const emitter = mitt();

registerPlugins(app)
app.config.globalProperties.emitter = emitter
app.mount('#app')
