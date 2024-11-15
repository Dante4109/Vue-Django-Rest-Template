<template>
  <v-card
    color="primary"
    class="darken-1"
    tile
  >
  <v-container>
    <h1 class="display-2 ma-4 pa-2 text-center">Register</h1>

    <v-form 
      ref="registrationForm" 
      method="POST" 
      action="/api/users/" 
      v-model="valid" 
      lazy-validation
      class="pa-4"
    >
      <v-row align="center">
        <v-col cols="12">
          <v-text-field 
            v-model="name" 
            label="Your name" 
            required
            solo-inverted
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col cols="6">
          <v-text-field 
            v-model="email" 
            :rules=emailRules
            :error-messages="emailErrors()"
            label="Email" 
            required 
            solo-inverted
          ></v-text-field>
        </v-col>

        <v-col cols="6">
          <v-text-field 
            v-model="confirmedEmail" 
            :rules=emailRules 
            label="Confirm Email" 
            :error-messages="emailErrors()"
            required 
            solo-inverted
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
          <v-text-field 
            v-model="password" 
            label="Password" 
            type="password" 
            :rules="[passwordRules.min,]"
            required 
            :error-messages="passwordErrors()"
            solo-inverted
          ></v-text-field>
        </v-col>
        <v-col cols="6">
          <v-text-field 
            v-model="confirmedPassword" 
            label="Confirm Password" 
            type="password" 
            :rules="[passwordRules.min,]"
            :error-messages="passwordErrors()"
            required 
            solo-inverted
          ></v-text-field>
        </v-col>
      </v-row>
      <v-checkbox v-model="agreement">
        <template v-slot:label>
          <div>
            I agree to the 
            <v-tooltip location="bottom">
              <template v-slot:activator="{ props }">
                <a
                  href='/terms-of-service'
                  target="_blank"
                  v-bind="props"
                  @click.stop
                >
                  Terms of Service
                </a>
              </template>
              Opens in new window
            </v-tooltip>
            and
            <v-tooltip location="bottom">
              <template v-slot:activator="{ props }">
                <a
                  href='/privacy-policy'
                  target="_blank"
                  v-bind="props"
                  @click.stop
                >
                  Privacy Policy.
                </a>
              </template>
              Opens in new window
            </v-tooltip> 
          </div>
        </template>
      </v-checkbox>
        <v-btn 
          outlined 
          @click="submit()" 
          :disabled="!valid"
          >Sign Up
        </v-btn>
      </v-form>
    </v-container>
  </v-card>
</template>

<script>
import userService from '@/services/userService';


export default {
  components: {},
  data: () => ({
    agreement: false,
    name: '',
    nameRules: [
      v => !!v || 'Name is required.',
    ],
    password: '',
    passwordRules: {
      min: v => v.length >= 8 || 'Password must be 8 or more characters.',
    },
    confirmedPassword: '',
    passwordValid: false,
    email: '',
    emailValid: false,
    confirmedEmail: '',
    emailRules: [
      v => !!v || 'Email is required.',
      v => /.+@.+\..+/.test(v) || 'Please use a valid email.',
    ],
  }),
  emits: {
    closeDialog: null
  },
  watch: {
    
    confirmedPassword: function (oldVal, newVal) // eslint-disable-line no-unused-vars 
    {
      if (this.confirmedPassword !== this.password) {
        // passwords do not match
        this.passwordValid = false
      } else {
        this.passwordValid = true
      }
    },
  
    confirmedEmail: function (oldVal, newVal) // eslint-disable-line no-unused-vars
    {
      if (this.confirmedEmail !== this.email) {
        this.emailValid = false
      } else {
        this.emailValid = true
      }
    },
  },
  computed: {
    valid:  {
      set(newVal) { // eslint-disable-line no-unused-vars
        return this.emailValid && this.passwordValid && this.agreement
      },
      get() {
        return this.emailValid && this.passwordValid && this.agreement
      }
    }
  },
  props: {
    next: {
      type: String,
      default: 'dashboard'
    }
  },
  methods: {
    emailErrors() {
      return (this.email === this.confirmedEmail) ? '' : 'Emails must match.'
    },
    passwordErrors() {
      return (this.password === this.confirmedPassword) ? '' : 'Passwords must match.'
    },
    
    
  async submit() {
    let payload = {
      "name": this.name,
      "email": this.email,
      "password": this.password
    }

    const response = await userService.createUser(payload) // eslint-disable-line no-unused-vars
      .then((response) =>{
        switch(response.status) {
        case (500): 
          this.displayNotification('authentication', 'Cannot register your account at this time.', 'Please visit our Discord for help.', 'error')
          break;
        case (404): 
          this.displayNotification('authentication', 'Cannot register your account at this time.', 'Please visit our Discord for help.', 'error')
          break;
        case (400): 
          this.displayNotification('authentication', 'An account for ' + payload.email + ' already exists.', 'Please try a different email address.', 'error')
          break;  
        case(201):
          this.$emit("closeDialog")
          this.displayNotification('authentication', 'Registration successful!',`Welcome aboard! Please check your inbox for your verification email in order to log in.`, 'success')
              break;
          default:
            this.displayNotification('authentication', 'Registration failed', response.data.detail, 'error')
            break;
          }
      })
    },
    openDashboard() {
      this.$router.replace(this.next)
    },
    async newProfile(user_id) {
        let id = {  
          "id": user_id
        }
        let payload = {
          "user": id
        }
        // console.log(payload)
        const response = await userService.createProfile(payload)
        .then((response) => { 
        switch(response.status) {
          case(200): 
            console.log("User Profile created successfully")
            this.refreshUser()
            return true 
          case(401): 
            this.displayNotification('authentication', 'Error', 'Unable to create a profile at this time', 'error')
            return false 
          }
        });
      },
    async checkProfile(user) {
          if(user.player_profile_id != null) {
            console.log("Found")
            return true 
          }
          else {
          const newProfile = await this.newProfile(user.id)
          return newProfile
        }
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