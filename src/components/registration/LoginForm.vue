<template>
<v-card
  color="primary"
  class="darken-1"
  tile
>
  <v-container>
    <h1 class="display-2 text-center ma-4 pa-2">Login</h1>
    <h3 class="subtitle text-center ma-4 pa-2">Welcome back. Login to manage your account.</h3>
    <v-form 
      ref="form" 
      v-model="valid" 
      lazy-validation
      class="pa-4"
    >
      <v-col cols="12" md="12">
        <v-row align="center">
          <v-text-field 
            v-model="email" 
            :rules=emailRules 
            label="Email" 
            required
            solo-inverted
          ></v-text-field>
        </v-row>
        <v-row align="center">
          <v-text-field 
            v-model="password"
            label="Password"
            required
            type="password"
            solo-inverted
          ></v-text-field>
        </v-row>
      </v-col>
      <v-btn outlined @click="login" :disabled="!valid || !email && !password">Login</v-btn>
    </v-form>
  </v-container>
  </v-card>
</template>

<script>
import userService from '@/services/userService'

export default {
  data: () => ({
    valid: true,
    password: '',
    email: '',
    emailRules: [
      v => !!v || 'Email is required.',
      v => /.+@.+\..+/.test(v) || 'You have entered an invalid email.',
    ],
  }),
  props: {
    next: {
      type: String,
      default: 'dashboard'
    }
  },
  methods: {
    async login() {
      this.$store.dispatch('obtainToken', { email: this.email, password: this.password })
      .then((response) => {
        switch(response.status) {
          case (500):
            this.displayNotification(
              'authentication',
              'Login failed',
              'Something went wrong on our end.' + '\n' + 'Hang tight we are working on it.',
              'error')
            break;
          case (404):
            this.displayNotification(
              'authentication',
              'Login failed',
              'Something went wrong on our end.' + '\n' + 'Hang tight we are working on it.',
              'error')
            break;  
          case (401):
            this.displayNotification(
              'authentication',
              'Login failed',
              'Incorrect Username/Password.' + '\n' + 'Please try again',
              'error')
            break;  
          case (200):
            this.$store.dispatch('getUserFromToken', response.data.access)
                .then((user) => {
                  if(user.is_verified) {
                    this.$store.commit('updateSessionUser', user)                
                      if(user.profile_id) {
                        this.displayNotification(
                          'authentication',
                          'Login successful',
                          `Welcome back.`,
                          'success')
                        this.$emit("closeDialog")
                      }
                      else {
                          console.log("Logging in first time. Creating user profile")
                          this.$emit("closeDialog")
                          this.$router.push("/ProfileSetup/")
                          }
                        }
                  else {                    
                    this.displayNotification(
                      'authentication',
                      'Email Not Verified',
                      `Please check your inbox for your verification email` + '\n'
                      + 'and follow the instructions to activate your account.',
                      'error')
                  }
                })
              break;
            }
        })
      },
    openDashboard() {
      /* this.$router.replace(this.next) */
      // Eventually route to "You have been successfully logged in page"
      window.location.reload()
    },
    async refreshUser() {
        const user = JSON.parse(this.$store.state.authenticatedUser)

        if(!user.id) {
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
    displayNotification(group, title, text, type) {
      this.$notify({
                  group: group,
                  title: title,
                  text: text,
                  type: type
                })
    }
  }
}
</script>