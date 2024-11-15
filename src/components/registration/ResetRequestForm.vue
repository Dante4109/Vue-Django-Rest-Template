<template>
<v-card
  color="primary"
  class="darken-1"
  tile
>
  <v-container>
    <h1 class="display-2 text-center ma-4 pa-2">Request Password Reset</h1>
    <h3 class="subtitle text-center ma-4 pa-2">Please enter the email address associated with your account to request a password reset link.</h3>
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
      </v-col>
      <v-btn outlined @click="reset" :disabled="!valid || !email ">Reset</v-btn>
    </v-form>
  </v-container>
  </v-card>
</template>

<script>
import passwordResetService from '@/services/passwordResetService';

export default {
  data: () => ({
    valid: true,
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
    async reset() {
      let data = {"email": this.email}

      const response = await passwordResetService.requestPasswordReset(data)

        switch(response.status) {
          case (500):
            this.displayNotification('authentication', 'Reset Failed', 'Something went wrong on our end.' + '\n' + 'Hang tight we are working on it.', 'error')
            break;
          case (404):
            this.displayNotification('authentication', 'Reset Failed', 'Something went wrong on our end.' + '\n' + 'Hang tight we are working on it.',  'error')
            break;  
          case (401):
            this.displayNotification('authentication', 'Username Not Found', 'Please enter an email address with an account to reset your password.',  'error')
            break;  
          case (200):
            this.displayNotification('authentication', 'Password Reset Sent', `Please check your inbox for your email.`, 'success')
            this.$emit("closeDialog")
              break;
          default:
            this.displayNotification('authentication', 'Reset Failed', response.data.detail, 'error')
            break;
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