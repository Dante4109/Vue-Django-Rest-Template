<template>
  <v-app-bar app rounded color="primary" class="hidden-xs-and-down">
    <!-- Logo -->
    
      <v-toolbar-title>
      <a @click="$router.replace('/')">
      
      <v-btn
      size="36px"
      max-height="40"
      max-width="40"      
      class="mr-4"
      icon="mdi-home"
      >
      </v-btn>   
      </a>
      </v-toolbar-title>
    
    <!-- Navigation items -->
    <v-toolbar-items>
      <v-menu v-for="item in navItems" :key="item.title" class="md-center" open-on-hover offset-y>
        <template v-slot:activator="{ props }">
          <v-btn
          v-bind="props"
          :class="{ 'highlight-nav': item.highlight }"
          @click="$router.push('/demo/' + item.title)"
          @mouseover="highlightItem(item)"
          @mouseleave="unhighlightItem(item)"
          >
          {{ item.title }}
        </v-btn>
      </template>
  </v-menu>
</v-toolbar-items>

<v-spacer></v-spacer>

<!-- Login or User profile icon -->
<div :key="user" v-if="!user">
      <v-btn data-cy="profile-btn-no-user" right icon @click="openAccountAccess">
            <v-icon
            v-bind="attrs"
            v-on="on"
            >mdi-login</v-icon>
      </v-btn>
    </div>

    <div :key="user" v-else>
      <v-btn data-cy="profile-btn-user" icon right @click="toggleDrawer">
        <div v-if="user.profile.ImgUrl==='none' || ''">
              <v-icon
                v-bind="attrs"
                v-on="on"
                >mdi mdi-account-circle
              </v-icon>
        </div>
        <div v-else>
          <v-avatar size="36px" >
            <v-img alt="Avatar" :src="user.profile.ImgUrl" />
          </v-avatar>
        </div>
      </v-btn>
    </div>
  </v-app-bar>

</template>

<script>
import userService from '@/services/userService'
export default {
  name: "Navbar",
  data() {
    return {
      dataKey: true,
      webpackpath: "",
      menuItems: [],
      menuRouteList: [],
      dialog: false,
      navItems: ([
        { num: 1, title: 'Photos', highlight: false },
        { num: 2, title: 'Art', highlight: false },
        { num: 3, title: 'News', highlight: false },
        { num: 4, title: 'Files', highlight: false },
        { num: 5, title: 'Data', highlight: false }
      ])
    };
  },
  created() {
    const user = JSON.parse(this.$store.state.authenticatedUser);
    if (user) {
      this.loggedIn = true;
    } else {
      this.loggedIn = false;
    }
  },
  methods: {
    changeData() {
      if(this.dataKey) {
        this.dataKey = false
      } 
      else {
        this.dataKey = true
      }
    },

    async refreshUser() {
        const user = JSON.parse(this.$store.state.authenticatedUser)

        if(user.id) {
          this.$router.replace('logout')
        }

        const response = await userService.fetchUser(user.id, this.$store.state.token)
        if(response.status != 200) {
          this.$router.replace('logout')
        } else {
          const refreshedUser = response.data
          this.$store.commit('updateSessionUser', refreshedUser)
        }
    },

    toggleDrawer() {
      // eslint-disable-next-line
      const drawer = this.$store.state.globalDrawer;
      if (drawer) {
        this.$store.commit("updateDrawer", false);
      } else {
        this.$store.commit("updateDrawer", true);
      }
    },

    logout() {
      this.$store.dispatch("logout");
      this.$router.go();
    },

    highlightItem(item) {
      item.highlight = true
    },
    unhighlightItem(item) {
      item.highlight = false
    },
    openAccountAccess() {
      this.emitter.emit('account_access');
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
  },
}
</script>

<style scoped>
.highlight-nav {
  background-color: rgba(248, 5, 5, 0.1);
}
</style>