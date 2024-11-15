<template>
  <v-app>
    <v-main>
      <NavbarSimple />
      <v-layout>
        <Registration />
      </v-layout>      
      <GlobalNavigation />
      <router-view :key="$route.fullPath"/>
    </v-main>
    <notifications group="authentication" position="bottom right" style="z-index: 99999;"/>
    <cookie-law
      theme="dark-lime"
      message="VDRF-Template uses cookies and personally provided data to remember who you are &amp; offer the best possible experience. You can learn more about how we use cookies in our Privacy Policy."
    ></cookie-law>
    <AppFooter />
  </v-app>
</template>

<script>
import axios from 'axios'

import GlobalNavigation from './components/navigation/GlobalNavigation.vue';
import Navbar from './components/navigation/Navbar.vue';
import AppFooter from './components/AppFooter.vue';
import Registration from './components/registration/Registration.vue';
import CookieLaw from 'vue-cookie-law';

export default {
 name: 'App',
  data() {
    return {
    }
  },
  Watch: {
    watch:{
      $route (){
          if(this.$store.state.token==null){
            this.$notify({group: "authentication",
                    title: "Logged Out",
                    text: "You have been securely logged out.",
                    type: "success",
                    duration: -1
                    })
            this.$store.commit('updateDrawer', false)
          }
      }
    }
  },
  computed: {
    banner: {
      get() {
        return this.$store.state.closedBanner
      },
      set(newVal) {
        return this.$store.commit('updateBanner', newVal)
      }
    }
  }
}
</script>

<style>
  .Cookie {
    background: #070b2e !important;
  }

  .Cookie .Cookie__button {
    background: #c0090b !important;
  }
</style>
