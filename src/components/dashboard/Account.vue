<template>
  <ImageManager />
  <div style="margin-left: 20%; margin-right: 20%">
    <v-layout row class="heading">
      <v-flex>
        <h1>Manage Account</h1>
        <h4>Manage your account information.</h4>
      </v-flex>
    </v-layout>

    <v-card color="primary" class="pa-4">
      <v-container>
        <v-col cols="12">
        <v-flex class="ma-4">
        <div>
          <v-hover v-slot="{ isHovering, props }">                     
          <v-btn
          :elevation="isHovering ? 16 : 2"
          :class="{ 'on-hover': isHovering }" 
          v-bind="props"
          icon size="100px" 
          @click="openImageManager">
            <div v-if="user.profile.ImgUrl==='none' || ''">
              <v-icon
                @click="openImageManager"
                v-bind="attrs"
                v-on="on"
                size="100px"
                >mdi mdi-account-circle
              </v-icon>
            </div>
          <div v-else>
          <v-avatar
            size="100px" 
            aspect-ratio="1.0"
          >
            <v-img alt="Avatar" :src="user.profile.ImgUrl" />
          </v-avatar>
          </div>
        </v-btn>
      </v-hover>
        </div>
        </v-flex>        
        </v-col>
        <v-flex class="ma-4">
        <p><strong>Name: </strong>{{ user.name }}</p>
        <p><strong>Email: </strong>{{ user.email }}</p>

        </v-flex>
        <v-form 
          class="pa-4"
        >

          <v-text-field 
            label="Change your name"
            solo-inverted
            v-model="newName"
          >
          </v-text-field>
          <v-btn 
            @click="updateName()"
            outlined
            :disabled="!newName != ''"
          >
            Change Name
          </v-btn>
        </v-form>

        <v-form 
          class="pa-4"
          v-model="emailValid"
        >
          <v-text-field 
            label="New Email" 
            solo-inverted
            v-model="newEmail"
            :rules="emailRules"
          >
          </v-text-field>

          <v-text-field 
            label="Confirm Email"
            solo-inverted
            :rules="emailRules"  
            v-model="confirmedEmail"
            :error-messages="emailErrors()"
          >
          </v-text-field>
          <v-btn 
            @click="updateEmail()"
            outlined
            :disabled="!emailValid"
          >
            Change Email
          </v-btn>
        </v-form>
      </v-container>

      <v-container>
        <v-card-title>Password</v-card-title>
        <v-card-text>Last changed 0 days ago.</v-card-text>
        <v-form 
          class="pa-4"
          v-model="passwordValid"
        >

          <v-text-field 
            type="password" 
            label="New Password"
            v-model="newPassword"
            solo-inverted
            :rules="[passwordRules.min]"
          >
          </v-text-field>

          <v-text-field 
            type="password" 
            label="Confirm password"
            v-model="confirmedPassword"
            solo-inverted
            :rules="[passwordRules.min]"
            :error-messages="passwordErrors()"
          >
          </v-text-field>
          <v-btn
            @click="updatePassword()"
            :disabled="!passwordValid"
            outlined
          >
            Change Password
          </v-btn>
        </v-form>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import userService from '@/services/userService';

export default {
  name: 'Account',
  data() {
    return {
      newName: '',
      newEmail: '',
      confirmedEmail: '',
      newPassword: '',
      confirmedPassword: '',
      emailValid: false,
      passwordValid: false,
      nameValid: false,
      passwordRules: {
        min: v => v.length >= 8 || 'Password must be 8 or more characters.',
      },
      emailRules: [
        v => !!v || 'Email is required.',
        v => /.+@.+\..+/.test(v) || 'Please use a valid email.',
      ],
      activeImage: [],
    }
  },
  methods: {
    async updateEmail() {
      const userId = this.user.id
      const token = this.token // eslint-disable-line no-unused-vars
      const data = {
        "email": this.newEmail
      }

      await userService.updateUser(userId, data)
        .then((response) => {
          if (response.status == 204) {
            this.$notify({
              group: 'authentication',
              title: 'Email updated!',
              text: `You have updated your email to ${this.newEmail}.`,
              type: 'success'
            })
            this.refreshUser()
            this.clearFields()
          } else {
            if (response.status == 409) {
              this.$notify({
                group: 'authentication',
                title: 'Failed to update email.',
                text: `It appears that this email address is already in use.  Please use a different email address.`,
                type: 'error'
              })
            }
            else {
              this.$notify({
                group: 'authentication',
                title: 'Failed to update email.',
                text: `An error occurred while attempting to update email. Please contact support.`,
                type: 'error'
              })
            }
          }
        })
    },
    async updatePassword() {
      const userId = this.user.id
      const token = this.token // eslint-disable-line no-unused-vars
      const data = {
        "password": this.newPassword
      }

      await userService.updateUser(userId, data)
        .then((response) => {
          if (response.status == 204) {
            this.$notify({
              group: 'authentication',
              title: 'Password updated!',
              text: `You have successfully changed your password.`,
              type: 'success'
            })
            this.refreshUser()
            this.clearFields()
          } else {
            this.$notify({
              group: 'authentication',
              title: 'Failed to update password.',
              text: `An error occurred while attempting to update your password. Please contact support.`,
              type: 'error'
            })
          }
        })
    },
    async updateName() {
      const userId = this.user.id
      const token = this.token // eslint-disable-line no-unused-vars
      const data = {
        "name": this.newName
      }

      await userService.updateUser(userId, data)
        .then((response) => {
          if (response.status == 204) {
            this.$notify({
              group: 'authentication',
              title: 'Your name has been updated!',
              text: `You have successfully changed your name.`,
              type: 'success'
            })
            this.refreshUser()
            this.clearFields()
          } else {
            this.$notify({
              group: 'authentication',
              title: 'Failed to update name.',
              text: `An error occurred while attempting to update your name. Please contact support.`,
              type: 'error'
            })
          }
        })
    },
    async refreshUser() {
      const user = JSON.parse(this.$store.state.authenticatedUser)

      if (!user.id) {
        this.$router.replace('logout')
      }

      const response = await userService.fetchUser(user.id, this.$store.state.token)
      if (response.status != 200) {
        this.$router.replace('logout')
      } else {
        const refreshedUser = response.data
        this.$store.commit('updateSessionUser', refreshedUser)
      }
    },
    async updateProfileImage(imageUrl) {            
      let data = {
        "ImgUrl": imageUrl,
      }
      await userService.updateProfile(this.user.profile_id, data)
        .then((response) => {
          if (response.status == 200) {
            this.$notify({
              group: 'authentication',
              title: 'Profile image updated!',
              text: `You have successfully changed updated your profile image.`,
              type: 'success'
            })
            this.refreshUser()
            this.clearFields()
          } else {
            this.$notify({
              group: 'authentication',
              title: 'Failed to update profile image.',
              text: `An error occurred while attempting to update your name. Please contact support.`,
              type: 'error'
            })
          }
        })
    },
  clearFields() {
    this.newName = ''
    this.newEmail = ''
    this.confirmedEmail = ''
    this.newPassword = ''
    this.confirmedPassword = ''
    },
  emailErrors() {
    return (this.newEmail === this.confirmedEmail) ? '' : 'Emails must match.'
    },
  passwordErrors() {
    return (this.newPassword === this.confirmedPassword) ? '' : 'Passwords must match.'
    },
  openImageManager() {
    this.emitter.emit('image_manager');
    },
  },  
  computed: {
    user: {
      get() {
        return JSON.parse(this.$store.state.authenticatedUser)
      }
    },
    token: {
      get() {
        return this.$store.state.token
      }
    }
  },
  created() {
    // Change profile picture
    this.emitter.on('updateCurrentImageParent', (data) => {
      this.activeImage = data.activeImage
      })
    },
    watch: {
      confirmedEmail: function() {
        if(this.confirmedEmail !== this.newEmail) {
          this.emailValid = false
        } else {
          this.emailValid = true
        }
      },
      confirmedPassword: function() {
        if(this.confirmedPassword !== this.newPassword) {
          this.passwordValid = false
        } else {
          this.passwordValid = true
        }
      },
      activeImage: function() {
        this.updateProfileImage(this.activeImage.url)
      },
    }
  }
</script>

<style scoped>
  .v-card {
    margin-bottom: 2em;
  }

  .heading {
    margin-bottom: 1em !important;
  }
</style>