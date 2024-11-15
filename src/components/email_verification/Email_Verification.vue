<template>
<v-layout>
<v-overlay :value="validatedToken">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>
</v-layout> 
</template>


<script>
import emailVerificationService from '@/services/emailVerificationService';

export default {
  name: "emailverification",
  props: ["verificationToken"],
  data: () => ({
      validatedToken: false,
  }),
  created() {
      this.tokenValidation()
  },

  methods:{
    async tokenValidation(){
      console.log(this.verificationToken)
      this.validatedToken =  await this.tokenCheck();
      if(this.validatedToken) {
        //Toast Message Email Verified, you can now log in
        this.displayNotification("authentication", "Email Verified", "You are being redirected. You may now log in.", "success")
        //Force Router Navigate to Home "/"
        }
      else {
        this.displayNotification("authentication", "Bad Token", "You are being redirected.", "error")
        }
        this.$router.push("/")
      },
    async tokenCheck() {
        let data = {"token": this.verificationToken}
        const tokenStatus = await emailVerificationService.checkVerificationToken(data);
        return tokenStatus.status===200?true:false
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

};
</script>