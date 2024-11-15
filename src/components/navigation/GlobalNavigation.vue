<template>
      <v-navigation-drawer 
      style="max-height: 80vh;"
      location="right" 
      fixed
      dark
      temporary
      width="256px"
      v-if="$store.state.globalDrawer"
      v-model="$store.state.globalDrawer"
      :key="loggedIn"
      >
        <template v-slot:prepend>
          <v-list-item
            v-if="user.profile.ImgUrl==='none' || ''"
            lines="two"
            :prepend-avatar=images.blankProfile
            subtitle="Logged in"
            :title=user.name
            >
          </v-list-item>
          <v-list-item
            v-else="user.profile.ImgUrl==='none' || ''"
            lines="two"
            :prepend-avatar=user.profile.ImgUrl
            subtitle="Logged in"
            :title=user.name
            >
          </v-list-item>          
        </template>

        <v-divider></v-divider>

        <v-list 
        density="compact" 
        nav
        >
          <v-list-item
            @click="changeDashboardComponent(link.dashboardComponent)"
            v-for="(link, i) in accountLinks"
            :key="i"
            :color="activeLinkColor"
            :to="link.target"          
            :prepend-icon=link.icon
            :title="link.text"
          >          
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
</template>


<script>
import genericProfileImage from '@/assets/pageimages/Generic-profile-picture.jpg'

export default {
  data() {
    return {
      activeLinkColor: "#fff",
      accountLinks: [{
          "icon": "mdi-shield-account",
          "dashboardComponent": "Account",
          "text": "My Account",
        },
        {
          "icon": "mdi-tools",
          "dashboardComponent": "Feedback",
          "text": "Give Feedback"
        },
        {
          "icon": "mdi-credit-card",
          "dashboardComponent": "Settings",
          "text": "Settings and Privacy"
        },
        {
          "icon": "mdi-credit-card",
          "dashboardComponent": "Support",
          "text": "Help and Support",
        },
        {
          "icon": "mdi-bug",
          "dashboardComponent": "Display",
          "text": "Display and Accessibility"
        },
        {
          "icon": "mdi-logout",
          "dashboardComponent": "logout",
          "text": "Logout"
        }
      ],
      quickLinks: [
        /*  {
            "icon": "mdi-gift",
            "click": "",
            "text": "Gift a Streamer"
          },
          {
            "icon": "mdi-mail",
            "click": "",
            "text": "Contact Us"
          },*/
        /* {
          "icon": "mdi-diamond-stone",
          "target": "/founders-program",
          "text": "Become a Founder",
        },
        {
          "icon": "mdi-library-video",
          "click": "",
          "text": "Our Streamers"
        }, */
        /* {
          "icon": "mdi-discord",
          "target": "https://discord.gg/JUrAdzu",
          "text": "Discord",
          "external": true
        },
        {
          "icon": "mdi-twitter",
          "target": "https://twitter.com/streambeacontv/",
          "text": "Twitter",
          "external": true
        }
      ],
      legalLinks: [
        {
          "icon": "mdi-shield-check",
          "target": "/terms-of-service",
          "text": "Terms of Service"
        },
        {
          "icon": "mdi-shield-lock",
          "target": "/privacy-policy",
          "text": "Privacy Policy"
        },
        {
          "icon": "mdi-help",
          "target": "/faq",
          "text": "FAQ"
        } */
      ], 
      images: {
        blankProfile: genericProfileImage
      },
    };
  },
  methods: {
    changeDashboardComponent(targetComponent) {
      if (targetComponent === "logout") {
        console.log(this.$route.name)
        console.log("clicked logout")
        this.drawerLogout()
      }

      else {
        this.switchDashboardComponent(targetComponent)
      }
    },

    switchDashboardComponent(targetComponent) {
      if (this.$route.name != 'dashboard') {
        this.$router.push('/dashboard')
          .then(() => {
            this.emitter.emit('changeDashboardComponent', targetComponent)
            this.$store.commit('updateDrawer', false)
          })
      } else {
        this.emitter.emit('changeDashboardComponent', targetComponent)
        this.$store.commit('updateDrawer', false)
      }
    },
    drawerLogout() {
      this.$store.commit('updateDrawer', false)
      this.$router.push("/logout")
    }
  },
  computed: {
    loggedIn: {
      get() {
        return this.$store.state.isLoggedIn
      },
      set(value) {
        this.$store.commit('updateLoggedInState', value)
      }
    },
    user: {
      get() {
        return JSON.parse(this.$store.state.authenticatedUser)
      }
    },
    drawer: {
      get() {
        return this.$store.state.globalDrawer
      },
      set(val) {
        return this.$store.commit('updateDrawer', val)
      }
    }
  }
}
</script>
