<template>
<v-layout>
<v-overlay :value="profileCheck">
      <v-progress-circular
        indeterminate
        size="64"
      ></v-progress-circular>
    </v-overlay>
</v-layout> 
</template>


<script>
import emailVerificationService from '@/services/emailVerificationService';
import userService from '@/services/userService'

export default {
  name: "profilesetup",
  props: ["verificationToken"],
  data: () => ({
      validatedToken: false,
      profileCheck: false,
  }),
  created() {
      this.newUserProfile()
  },

  methods:{
    async newUserProfile() {
        
        // console.log(payload)
        this.profileCheck = await this.newProfileCheck();
        if(this.profileCheck) {
          //Toast Message Email Verified, you can now log in
          this.displayNotification("authentication", "Creating new user profile", `You are being redirected` + '\n' + `Welcome to Affinity Core!`, 'success')
          this.refreshUser()
          this.$router.push("/") 
        }
        else {
          console.log("Failed to create user profile")
          this.displayNotification("authentication", "Failed to create user profile", `You are being redirected.` + '\n' + `Please contact an administraor`, "error")
          this.$router.push("/")
        }
    },
    async tokenValidation(){
      console.log(this.verificationToken)
      this.validatedToken =  await this.tokenCheck();
      if(this.validatedToken) {
        //Toast Message Email Verified, you can now log in
        this.displayNotification("authentication", "Creating new user profile", "You are being redirected. `Welcome to Affinity Core!`", "success")
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
    
    async newProfileCheck() {
        let id = {  
          "id": this.user.id
        }
        let payload = {
          "user": id
        }
        const tokenStatus = await userService.createProfile(payload);
        return tokenStatus.status===201?true:false
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

  },
  computed: {
    user: {
    get() {
      return JSON.parse(this.$store.state.authenticatedUser)
        }
      },
  }

};
</script>