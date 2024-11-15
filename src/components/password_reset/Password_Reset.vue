<template>
<v-layout>
    <v-container> 
            <div v-if="validatedToken">
                <v-card
                  color="primary"
                  tile
                >
                    <v-card-title class="layout justify-center">Password Reset</v-card-title>
                    <v-card-subtitle class="layout justify-center">Please enter a new password for your account.</v-card-subtitle>
                    <v-form 
                    class="pa-4"
                    v-model="passwordValid"
                    >

                    <v-text-field 
                        type="password" 
                        label="New Password"
                        v-model="newPassword"
                        solo-inverted
                        :rules="[passwordRules.rule]"
                    >
                    </v-text-field>

                    <v-text-field 
                        type="password" 
                        label="Confirm password"
                        v-model="confirmedPassword"
                        solo-inverted
                        :rules="[passwordRules.rule]"
                        :error-messages="passwordErrors()"
                    >
                    </v-text-field>
                    <v-btn
                        @click="submitNewPassword()"
                        :disabled="!passwordValid"
                        outlined
                    >
                        Change Password
                    </v-btn>
                    </v-form>
                </v-card>
            </div>
            <div v-else>
              <p1>Invalid password token provided</p1>
            </div>
    </v-container>
</v-layout> 
</template>


<script>
import passwordResetService from '@/services/passwordResetService';

export default {
  name: "passwordreset",
  props: ["resetToken"],
  data: () => ({
      validatedToken: false,
      newPassword: '',
      confirmedPassword: '',
      passwordValid: false,
      passwordNote: "Please update your password.",
      passwordRules: {
          rule: v => v.length >= 8|| 'Password must be 8 or more characters.',
        },
  }),
  methods:{
      
      clearPasswords(){
          this.newPassword = ''
          this.confirmedPassword = ''
      },

      async submitNewPassword(){
          let data = {
              "password": this.newPassword,
              "token": this.resetToken
          }
          const passwordStatus = await passwordResetService.submitPasswordReset(data)

        switch(passwordStatus.status) {
          case (500):
            this.displayNotification('authentication', 'Server Error', 'Something went wrong on our end.' + '\n' + 'Hang tight we are working on it.', 'error')
            this.clearPasswords()
            break;
          case (404):
            this.displayNotification('authentication', 'Invalid Token', 'It appears your token has expired.' + '\n' + 'Please submit a new password reset request.',  'error')
            this.clearPasswords()
            break;  
          case (400):
            this.displayNotification('authentication', 'Invalid Password Selected', passwordStatus.data.password,  'error')
            this.clearPasswords()
            break;  
          case (200):
            this.displayNotification('authentication', 'Password Reset Successful', `You have successfully reset your password.`, 'success')
            this.$router.push("/")
              break;
          default:
            this.displayNotification('authentication', 'Failure', passwordStatus.data.detail, 'error')
            this.clearPasswords()
            break;
            }

          return passwordStatus.status===200?true:false
      },

      async tokenValidation(){
         this.validatedToken =  await this.tokenCheck();
      },
      async tokenCheck() {
        let data = {"token": this.resetToken}
        const tokenStatus = await passwordResetService.checkResetToken(data);
        console.log(tokenStatus.status)
        return tokenStatus.status===200?true:false
      },

      passwordErrors() {
      return (this.newPassword === this.confirmedPassword) ? '' : 'Passwords must match.'
    },

    displayNotification(group, title, text, type) {
      this.$notify({
                  group: group,
                  title: title,
                  text: text,
                  type: type
                })
    }

  },

  watch:{
      confirmedPassword: function() {
        if(this.confirmedPassword !== this.newPassword) {
          this.passwordValid = false
        } else {
          this.passwordValid = true
        }
      }
  },
  created() {
      this.tokenValidation()
  },
};
</script>