import { createRouter, createWebHistory } from 'vue-router'
import store from "@/stores/vuex"
import Dashboard from '@/pages/Dashboard.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../pages/Home.vue')
    },
    {
    path: "/dashboard",
    name: "dashboard",
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      const user = JSON.parse(store.state.authenticatedUser);
      if (user) {
        next();
      } else {
        // eslint-disable-next-line no-console
        console.log("Route rejected.");
        next("/");
      }
    }
  },

    // Account registration and mangement
    {
      path: '/password_reset/:resetToken',
      name: 'passwordreset',
      props: true,
      component: () => import("../components/password_reset/Password_Reset.vue"),
    },
    {
      path: '/email_verification/:verificationToken',
      name: 'emailverification',
      props: true,
      component: () => import("../components/email_verification/Email_Verification.vue"),
    },
    {
      path: '/ProfileSetup/',
      name: 'profilesetup',
      props: true,
      component: () => import("../components/profile_setup/Profile_Setup.vue"),
    },
    {
    path: "/logout",
    name: "logout",
    beforeEnter: (to, from, next) => {
      if (store.state.authenticatedUser) {
        store.dispatch("logout");
        next("/");
      }
      this.$router.replace(this.next)
      // Eventually route to "You have been successfully logged out page"
      }
    },
    
    // Demo Pages

    /*
    Will eventually be added dynamically using
    Full documentation for this feature can be found in the 
    Official[unplugin - vue - router](https://github.com/posva/unplugin-vue-router) repository. 
    */
    {
    path: "/demo/Data",
    name: "csv_import",
    props: true,
    component: () => import("../pages/demo/csv_import.vue")
    },
    {
    path: "/demo/Files",
    name: "file_tree",
    props: true,
    component: () => import("../pages/demo/file_tree.vue")
    },
    {
    path: "/demo/Photos",
    name: "image_manager",
    props: true,
    component: () => import("../pages/demo/image_manager.vue")
    },
    {
    path: "/demo/Art",
    name: "meme_maker",
    props: true,
    component: () => import("../pages/demo/meme_maker.vue")
    },
    {
    path: "/demo/News",
    name: "news_feed",
    props: true,
    component: () => import("../pages/demo/news_feed.vue")
    },


    // Tests. Should not be accessible in production.
    {
    path: "/product/:productPath",
    name: "product",
    props: true,
    component: () => import("../pages/GenericPage.vue")
    },
    {
    path: "/fake",
    name: "fake",
    component: () => import("../pages/FakePage.vue")
    },
    {
    path: "/emit",
    name: "emitTest",
    component: () => import("../components/EmitTest.vue")
    },
    {
    path: "/emitTS",
    name: "emitTestTS",
    component: () => import("../components/EmitTestTS.vue")
    },
  ]
})

export default router