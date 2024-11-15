<template>
  <div>
      <v-flex class="heading">
        <h1>Player Sign-Up</h1>
        <h4>Enter information below for your player profile.</h4>
      </v-flex>

      <v-layout>
        <v-form
          ref="form"
          style="width:100%;"
        >

<!-- EAMUSE -->
        <v-text-field
          v-model="eamuse"
          solo-inverted
          color="white"
          label="Eamuse"></v-text-field>

<!-- Email Address -->
    <v-text-field
      v-model="email"
      label="Email address"
      solo-inverted
      color="white"
      ></v-text-field>
<!-- First Name -->
      <v-text-field
      v-model="first"
      label="First Name"
      solo-inverted
      color="white"
      ></v-text-field>
<!-- Last Name -->
      <v-text-field
      v-model="last"
      label="Last Name"
      solo-inverted
      color="white"
      ></v-text-field>


<!-- Date of Birth -->
        <div>
            <v-col cols="12" sm="6" md="4">
                <v-menu
                v-model="menu2"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="290px"
                >
                
                <template v-slot:activator="{ on }">
                    <v-text-field
                        v-model="date"
                        label="Date of Birth"
                        readonly
                        v-on="on"
                    ></v-text-field>
                </template>
                    <v-date-picker v-model="date" @input="menu2 = false"></v-date-picker>
                </v-menu>
            </v-col>
            <v-spacer></v-spacer>
        </div>

<!-- Prounouns --> 
    <v-container fluid>
      <v-combobox
        v-model="pronouns"
        :search-input.sync="search"
        hide-selected
        hint="Maximum of 5 pronouns"
        label="Preferred pronouns"
        multiple
        persistent-hint
        small-chips
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>
                No results matching "<strong>{{ search }}</strong>". Press <kbd>enter</kbd> to create a new one
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-combobox>
    </v-container>
<!-- Select Region --> 
    <v-container fluid>
      <v-row align="center">
        <v-col cols="6">
          <v-subheader>Select State</v-subheader>
        </v-col>
        <v-col cols="6">
          <v-select
            v-model="region"
            :items="states"
            menu-props="auto"
            hide-details
            label="Select"
            single-line
          ></v-select>
        </v-col>
      </v-row>
    </v-container>

<!-- Fun Facts -->
    <v-container fluid>
        <v-textarea
        counter
        v-model="facts"
        label="Fun Facts"
        :rules="rules"
        :value="value"
        ></v-textarea>
    </v-container>

<!-- Select Games -->
        <v-container fluid>
      <v-row align="center">
        
  
        <v-col cols="12" sm="6">
          <v-select
            v-model="selectedGames"
            :items="availableGames"
            label="Select"
            multiple
            chips
            hint="Select the games you will be playing in the tournament"
            persistent-hint
          ></v-select>
        </v-col>
      </v-row>
    </v-container>
<!-- Records -->
    <v-container fluid>
        <v-textarea
        counter
        v-model="records"
        label="Game Records"
        :rules="rules"
        :value="value"
        ></v-textarea>
    </v-container>
<!-- Submit Button -->
        <v-btn
          label="Submit"
          color="white"
          outlined
          @click="submit()" 
          right
          style="margin-left: auto;"
          >Submit</v-btn>
<!-- End Form -->


        </v-form>
      </v-layout>
  </div>



</template>

<script>
//import axios from 'axios';
import userService from '@/services/userService';


export default {
  name: 'Profile',
  components: {},
  data: () => ({
  //#region Player Profile 
    eamuse: "",
    email: "",
    first: "",
    last: "",
    pronouns: [],
    region: '',
    records: [],
    facts: [],
    selectedGames: [],
  //#endregion      
  //#region Date Picker
      date: new Date().toISOString().substr(0, 10),
      menu: false,
      modal: false,
      menu2: false,
      textboxRules: [v => v.length <= 25 || 'Max 25 characters'],

  //#endregion
  //#region Game Select
      availableGames: [
        'Dance Dance Revolution A20', 'BeatmaniaIIDX', 'Pump it Up', 'Sound Voltex',
        'Popn Music', 'Museca', 'Dance Rush', 'DDR Extreme Pro',
    ],
  //#endregion
  //#region Region Picker
    e1: 'Florida',
    e2: 'Texas',
    e3: null,
    e4: null,
    items: [
      { text: 'State 1' },
      { text: 'State 2' },
      { text: 'State 3' },
      { text: 'State 4' },
      { text: 'State 5' },
      { text: 'State 6' },
      { text: 'State 7' },
      ],
      states: [
        'Alabama', 'Alaska', 'American Samoa', 'Arizona',
        'Arkansas', 'California', 'Colorado', 'Connecticut',
        'Delaware', 'District of Columbia', 'Federated States of Micronesia',
        'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho',
        'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
        'Louisiana', 'Maine', 'Marshall Islands', 'Maryland',
        'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
        'Missouri', 'Montana', 'Nebraska', 'Nevada',
        'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
        'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio',
        'Oklahoma', 'Oregon', 'Palau', 'Pennsylvania', 'Puerto Rico',
        'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
        'Texas', 'Utah', 'Vermont', 'Virgin Island', 'Virginia',
        'Washington', 'West Virginia', 'Wisconsin', 'Wyoming',
      ],
  //#endregion
  search: "", 
  value: "",
  rules: [],

  }),
  
  watch: {
    pronouns (val) {
      if (val.length > 5) {
        this.$nextTick(() => this.pronouns.pop())
      }
    },
  },

  mounted() {
    this.checkPlayerProfile(this.user)
  },

  methods: {
  async checkPlayerProfile(user) {
        if(user.player_profile_id != null) {
        this.player_profile = this.getPlayerProfile(user.player_profile_id)
      }
        else {
        this.newPlayerProfile(this.user.id)
      }
    },
  async submit() {
      let payload = {
        "first_name": this.first,
        "last_name": this.last,
        "eamuse": this.eamuse,
        "age": this.date,
        "pronouns": this.pronouns,
        "region": this.region,
        "records": this.records,
        "facts": this.facts,
        "email": this.email,
        "games": this.selectedGames
      }
  
      await userService.updatePlayerProfile(this.user.player_profile_id, payload)
    
    },
  async displayNotification(group, title, text, type) {
      this.$notify({
                  group: group,
                  title: title,
                  text: text,
                  type: type
                })
    },
  
  async getPlayerProfile(payload) {
            const player_Profile = await userService.fetchPlayerProfile(payload)
            this.player_profile = player_Profile
            this.first = this.player_profile.first_name
            this.last = this.player_profile.last_name
            this.eamuse = this.player_profile.eamuse
            this.date = this.player_profile.age
            this.pronouns = this.player_profile.pronouns
            this.region = this.player_profile.region
            this.records = this.player_profile.records
            this.facts = this.player_profile.facts
            this.email = this.user.email
            this.selectedGames = this.player_profile.games
            this.ImgUrl = this.player_profile.ImgUrl
        },
  async newPlayerProfile(user_id) {
      let id = {
        "id": user_id
      }
      let payload = {
       "user": id
      }
      console.log(payload)
      await userService.createPlayerProfile(payload)
      this.refreshUser()
      this.checkPlayerProfile(user)
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
    }
  },
  computed: {
    user: {
      get() {
        return JSON.parse(this.$store.state.authenticatedUser)
      }
    },
  }
}

</script>

<style scoped>
p {
  color: #B2B4B2;
  margin: 0 1em;
  font-weight: 700;
}

.v-card {
  margin-bottom: 2em;
}

.heading {
  margin-bottom: 1em !important;
}

a {
  color: #fff !important;
  text-decoration: none;
}

</style>
