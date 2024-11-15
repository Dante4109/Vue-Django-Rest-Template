<template>
    <v-col cols="12" >
      <Account v-if="active == 'Account'" />
      <Support v-if="active == 'Support'" />
      <Settings v-if="active == 'Settings'" />
      <Feedback v-if="active == 'Feedback'" />
      <Display v-if="active == 'Display'" />
    <v-snackbar v-model="alert" :color="alert.color" :timeout="alertTimeout">
      {{ alert.message }}
      <v-btn dark @click="alert = false">Close</v-btn>
    </v-snackbar>
    </v-col>
</template>

<script>
import Account from "@/components/dashboard/Account";
import Support from "@/components/dashboard/Support";
import Feedback from "@/components/dashboard/Feedback";
import Settings from "@/components/dashboard/Settings";
import Display from "@/components/dashboard/Display";

export default {
  name: "Dashboard",
  components: {
    Account,
    Support,
    Settings,
    Feedback,
    Display
  },
  data() {
    return {
      active: "account",
      mobile: false,
      user: false,
      alert: false,
      alertTimeout: 4000
    };
  },
  mounted() {
    this.emitter.on("changeDashboardComponent", data => {
      this.active = data;
      // eslint-disable-next-line no-console
      // console.log("test:" + data)
    });

    this.emitter.on("sidebar", data => {
      // eslint-disable-line no-unused-vars
      this.drawer = !this.drawer;
    });
  }
};
</script>