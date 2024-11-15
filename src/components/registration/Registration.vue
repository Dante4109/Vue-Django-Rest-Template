<template>
  <v-container>
    <v-dialog 
    class="registration" 
    v-model="dialog" 
    max-width="1200px" 
    overlay-color="primary"
  >
    <v-tabs
      v-model="tab" align-tabs="center" 
      background-color="primary"
      slider-color="white">
      <v-tab value="1">Login</v-tab>
      <v-tab value="2">Sign Up</v-tab>
      <v-tab value="3">Forgot Password</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item value="1" background-color="primary">
      <LoginForm :next="this.next" @closeDialog="closeDialog"/>
      </v-tabs-window-item>
      <v-tabs-window-item value="2" background-color="primary">
      <RegistrationForm :next="this.next" @closeDialog="closeDialog"/>
      </v-tabs-window-item>
      <v-tabs-window-item value="3" background-color="primary">
      <ResetRequestForm :next="this.next" @closeDialog="closeDialog"/>
      </v-tabs-window-item>
    </v-tabs-window>
    </v-dialog>
  </v-container>
</template>

<script>

import RegistrationForm from '@/components/registration/RegistrationForm';
import ResetRequestForm from '@/components/registration/ResetRequestForm';
import LoginForm from '@/components/registration/LoginForm';

export default {
  name: 'Registration',
  components: {
    RegistrationForm,
    LoginForm,
    ResetRequestForm
  },
  data() {
    return {
    step: 1,
    next: 'dashboard',
    user: false,
    dialog: false,
    tab: "1"
    }
  },
  methods: {
    closeDialog(){
      this.dialog = false
    },
    openDialog() {
      this.dialog = true;

      if(data.next) {
        this.next = data.next
      }
    }


  },
  watch: {
    loggedIn: function() {
      this.dialog = false
    }
  },
  computed: {
    loggedIn: {
      get() {
        // return JSON.parse(this.$store.state.isLoggedIn)
        return false
      }
    }
  },
  mounted() {

  },
  created() {
    this.emitter.on('account_access', data => {
      this.dialog = true;

      if(data.next) {
        this.next = data.next
      }
    })
  }
}

</script>

  <style>
.v-stepper__content {
  padding: 0 !important;
}
</style>