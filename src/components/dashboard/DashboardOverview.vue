<template>
<div>
  <div style="height:60px; width:100vh;"></div>
  <div>
  <Account />

  </div>
</div>
</template>

<script>
import TwitterCard from './TwitterCard';
import DashboardHistory from './DashboardHistory';
import DashboardComingSoon from './DashboardComingSoon';
import Account from './Account';


export default {
  data() {
    return {
    }
  },
  components: {
    TwitterCard,
    DashboardHistory,
    DashboardComingSoon,
    Account
  }
}
</script>