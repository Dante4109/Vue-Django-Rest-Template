<template>
  <v-container fluid>
    <v-row align="center">
      <v-col cols="12">
        <div align="center" class="title">
          <h1>
            Deck Builder
            <v-icon color="white">mdi-tools</v-icon>
          </h1>
        </div>
        <!-- Buttons -->
        <v-col :cols="0">
        <v-row justify="center"
          >
          <v-btn @click="postDeck(sortedDeck, sortedDeckQty)">
              Post Deck
            </v-btn>
          <v-btn
          @click.stop="dialogDeckId = true"
          >
              Load Deck 
            </v-btn>
          <!-- Pop Up -->
            <v-dialog
                    v-model="dialogDeckId"
                    max-width="290"
                      >
                    <v-card>
                      <v-card-title class="headline">Enter Deck Id</v-card-title>
              
                      <v-col cols="12">
                        <v-text-field v-model="deckId"></v-text-field>
                      </v-col>
              
                      <v-card-actions> 
                        <div class="text-center">
                          <div class="my-2">
                        <v-btn
                          color="green darken-1"
                          text
                          @click="dialogDeckId = false"
                        >
                          OK
                        </v-btn>
                          </div>
                        </div>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
          
          <v-btn @click="publishDeck">
              Publish Deck
            </v-btn>
          <v-btn @click="delDeck">
              Delete Deck
            </v-btn>
          <v-btn @click="saveDeck">
              Save Deck
            </v-btn>
          <v-btn @click="downloadDeckData(sortedDeck, sortedDeckQty)">
              Download Deck Data
            </v-btn>
          <v-btn @click="reset">
            Reset
            </v-btn>
          <v-btn @click="info">
            Info
            </v-btn>
        </v-row>
        </v-col>
      </v-col>
    </v-row>
    <!-- Card Preview -->
    <!-- Title -->
    <v-row>
      <v-col :col="9">
        <div>
          <h1>Collecton</h1>
        </div>

        

        <v-col cols="12">
          <v-text-field hide-details label="Search"></v-text-field>
        </v-col>

        <v-col>
          <v-flex class="heading">
            <h1>Cards go here</h1>
          </v-flex>

          <v-container fluid class="collection">
            <v-row>
              <v-col cols="12">
                <v-row style="justify-content: space-evenly;">
                  <v-hover
                    v-slot:default="{ hover }"
                    :key="card.name"
                    v-for="(card) in cardCollection"
                  >
                    <v-card class="card-tile" :img="card.cardimg_url" @click="addToDeck(card)">
                      <v-expand-transition>
                        <div
                          v-if="false"
                          class="d-flex transition-fast-in-fast-out blue darken-2 v-card--reveal display-3 white--text"
                          style="height: 100%;"
                        >
                          <p class="card_details">
                            {{card.card_name}}
                            <br />
                            {{card.card_type}} - {{card.card_subtypes}}
                            <br />
                            Cost: {{card.affinity_cost_total}}
                          </p>
                        </div>
                      </v-expand-transition>
                    </v-card>
                  </v-hover>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
          <!--
        <v-list>
          <v-list-item-group v-model="cardCollection">
            <v-list-item 
              v-for="card in cardCollection"
              :key="card"
            >
            <h1> card name: {{ card.name}} </H1>
            <v-img :src="card.img_url" aspect-ratio="1.0" contain class="image" />
            </v-list-item>
          </v-list-item-group>
        </v-list>
          -->
        </v-col>
      </v-col>

      <!-- Collection Info -->
      <!-- Title -->
      
      <v-col :cols="3">
        <v-container fluid class="collection">
        <v-layout fab fixed>
 
          <v-form ref="form" style="width:100%;">
            <v-flex class="heading">
              <h1>Deck List</h1>
            </v-flex>
            <!-- Deck Name -->
            <v-text-field
              v-model="txtDeckName"
              solo-inverted
              color="white"
              label="Deck Name"
            ></v-text-field>

            <!-- Cardlist -->
            <v-list class="decklistbar">
              <template v-for="(item, i) in sortedDeck">
                <v-hover v-slot:default="{ hover }" :key="i">
                  <v-list-item :key="i">
                    <v-list-item-action v-if="hover">
                      <v-btn icon ripple>
                        <v-icon color="grey lighten-1">mdi-information</v-icon>
                      </v-btn>
                    </v-list-item-action>

                    <v-list-item-avatar>
                      <v-list-item-title v-text="item.affinity_cost_total"></v-list-item-title>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title v-text="item.card_name" class="wrap-title"></v-list-item-title>
                    </v-list-item-content>

                    <v-spacer></v-spacer>

                    <v-list-item-action v-if="hover">
                      <v-btn icon ripple @click="increaseCardQty(item)">
                        <v-icon color="grey lighten-1">mdi-plus</v-icon>
                      </v-btn>
                    </v-list-item-action>

                    <v-list-item-action v-if="hover">
                      <v-btn icon ripple @click="decreaseCardQty(item)">
                        <v-icon color="grey lighten-1">mdi-minus</v-icon>
                      </v-btn>
                    </v-list-item-action>

                    <v-list-item-avatar>
                      <v-list-item-title v-text="sortedDeckQty[i]"></v-list-item-title>
                    </v-list-item-avatar>
                  </v-list-item>
                </v-hover>
              </template>
            </v-list>
            <v-divider></v-divider>
            <!-- End Form -->
          </v-form>
        </v-layout>
        </v-container>
      </v-col>
      
    </v-row>
  </v-container>
</template>


<script>
//import axios from 'axios';
import userService from '@/services/userService'
import cardService from '@/services/cardService'
import deckService from '@/services/deckService'
import canvasService from '@/services/canvasService'
import mathService from '@/services/mathService'
import stringService from '@/services/stringService'
import arrayService from '@/services/arrayService'

export default {
  name: 'Deckeditor',
  components: {},
  data: () => ({
    dataSnapShot: "",
    name: "",
    cardCollection: [],
    cardData: [],
    deck: [],
    sortedDeck: [],
    sortedDeckQty: [],
    qty: 0,
    dialogDeckId: false,
    deckId: 0,
    deckUUID: "",
    txtDeckName: "",
  //#region Card Type
    cardtype: '',
    card_types: [
        'Creature', 'Construct', 'Spell', 'Immortal', 'Construct Creature' 
      ],
    creature_enabled: false,
  //#region AffinityList
    affinityselected: null,
    AffinityList: ['Light', 'Dark', 'Fire', 'Water', 'Nature', 'Air', 'Basic'],
  //#regiopn Subtypes
    subtype_items: [
      {
        text: 'Human',
      },
      {
        text: 'Elf',
      },
      {
        text: 'Elemental',
      },
      {
        text: 'Merfolk',
      },
      {
        text: 'Zombie',
      },
      {
        text: 'Soldier',
      },
      {
        text: 'Wizard',
      },
      {
        text: 'Dragon',
      },
      ],
    loading: false,
    subtypes: '',
    subtype_selected: [], 
    value: "",
    rules: [],
  //#region CanvasProperties
    canvasPropertySelected: '',
    canvasProperties: 
      [
        'Canvas Size',
        'Image Size',
        'Image Position',
      ],
  //#region TextProperties
    textPropertySelected: 'txtLightCost',
    textProperties: 
    [
      //'Nothing',
      'txtLightCost', //0 
      'txtDarkCost', //1
      'txtFireCost',
      'txtWaterCost',
      'txtNatureCost',
      'txtAirCost',
      'txtBasicCost',
      'txtTotalCost',
      'txtMain',
      'txtName',
      'txtType', //9
      'txtSubType', //10
      'txtFlavor', //12
      'txtBottom', //13
      'txtForce', //14
      'txtVitality' //15
    ],
    TestPositionX: 0,
    TestPositionY: 0,
  //#region Textboxes
    textbox: "",
    textbox_value: "",
    textbox_rules: [],
    flavor_text: "",
    flavor_text_value: "",
    flavor_text_rules: [],
  //#region Card Preview variables 
    //#region Canvas
      canvasElementId: 'canvas',
      width: 375,
      height: 523,
      image: "",
      imageWidth: 0,
      imageHeight: 0,
      selectedImage: null,
      cardFrame: '',
      cardImageWidth: 0,
      cardImageHeight: 0,
      cardImagePositionX: 0,
      cardImagePositionY: 0,
      cardFrameCheckbox: false,
      cardImageAspectPercentage: 100,
      presets: [
        require('@/assets/Card.png')
      ],
      memeImage: "",
    //#region TextArrays
      arrIndex: 0,
      arrFont: [
      //"1"
      ],
      arrMaxWidth: [
      //"1"
      ],
      arrLineWidth:[
      //"1"
      ],
      arrLineHeight:[
      //"1"
      ],
      arrStrokeStyle:[
      //"1"
      ],
      arrFillStyle:[
      //"1"
      ],
      arrPositionX: [],
      arrPositionY: [],
    //#region LightCostTextVariables 0
      txtLightCost: "0",
      txtLightCostMaxWidth: 250,
      txtLightCostStrokeStyle: '#000000',
      txtLightCostFillStyle: '#FFFFFF',
      txtLightCostLineWidth: 1,
      txtLightCostPositionX: 50,
      txtLightCostPositionY: 23,
      txtLightCostFont: '15px "Impact", sans-serif',
      txtLightCostLineHeight: 60,
    //#region DarkCostTextVariables
      txtDarkCost: "0",
      txtDarkCostMaxWidth: 250,
      txtDarkCostStrokeStyle: '#000000',
      txtDarkCostFillStyle: '#FFFFFF',
      txtDarkCostLineWidth: 1,
      txtDarkCostPositionX: 50,
      txtDarkCostPositionY: 75,
      txtDarkCostFont: '15px "Impact", sans-serif',
      txtDarkCostLineHeight: 60,
    //#region FireCostTextVariables
      txtFireCost: "0",
      txtFireCostMaxWidth: 250,
      txtFireCostStrokeStyle: '#000000',
      txtFireCostFillStyle: '#FFFFFF',
      txtFireCostLineWidth: 1,
      txtFireCostPositionX: 28,
      txtFireCostPositionY: 35,
      txtFireCostFont: '15px "Impact", sans-serif',
      txtFireCostLineHeight: 60,
    //#region WaterCostTextVariables
      txtWaterCost: "0",
      txtWaterCostMaxWidth: 250,
      txtWaterCostStrokeStyle: '#000000',
      txtWaterCostFillStyle: '#FFFFFF',
      txtWaterCostLineWidth: 1,
      txtWaterCostPositionX: 72,
      txtWaterCostPositionY: 36,
      txtWaterCostFont: '15px "Impact", sans-serif',
      txtWaterCostLineHeight: 60,
    //#region NatureCostTextVariables
      txtNatureCost: "0",
      txtNatureCostMaxWidth: 250,
      txtNatureCostStrokeStyle: '#000000',
      txtNatureCostFillStyle: '#FFFFFF',
      txtNatureCostLineWidth: 1,
      txtNatureCostPositionX: 29,
      txtNatureCostPositionY: 63,
      txtNatureCostFont: '15px "Impact", sans-serif',
      txtNatureCostLineHeight: 60,
    //#region AirCostTextVariables
      txtAirCost: "0",
      txtAirCostMaxWidth: 250,
      txtAirCostStrokeStyle: '#000000',
      txtAirCostFillStyle: '#FFFFFF',
      txtAirCostLineWidth: 1,
      txtAirCostPositionX: 72,
      txtAirCostPositionY: 63,
      txtAirCostFont: '15px "Impact", sans-serif',
      txtAirCostLineHeight: 60,
    //#region BasicCostTextVariables
      txtBasicCost: "0",
      txtBasicCostMaxWidth: 250,
      txtBasicCostStrokeStyle: '#000000',
      txtBasicCostFillStyle: '#FFFFFF',
      txtBasicCostLineWidth: 1,
      txtBasicCostPositionX: -25,
      txtBasicCostPositionY: 30,
      txtBasicCostFont: '15px "Impact", sans-serif',
      txtBasicCostLineHeight: 60,
    //#region TotalCostTextVariables
      txtTotalCost: "0",
      txtTotalCostMaxWidth: 250,
      txtTotalCostStrokeStyle: '#000000',
      txtTotalCostFillStyle: '#FFFFFF',
      txtTotalCostLineWidth: 1,
      txtTotalCostPositionX: 50,
      txtTotalCostPositionY: 51,
      txtTotalCostFont: '18px "Impact", sans-serif',
      txtTotalCostLineHeight: 60,
    //#region MainTextVariables 8
      txtMain: '',
      txtMainMaxWidth: 250,
      txtMainStrokeStyle: '#000000',
      txtMainFillStyle: '#FFFFFF',
      txtMainLineWidth: 1,
      txtMainPositionX: 38,
      txtMainPositionY: 367,
      txtMainFont: '20px "Impact", sans-serif',
      txtMainLineHeight: 60,
    //#region NameTextVariables
      txtName: '',
      txtNameMaxWidth: 250,
      txtNameStrokeStyle: '#000000',
      txtNameFillStyle: '#FFFFFF',
      txtNameLineWidth: 1,
      txtNamePositionX: 97,
      txtNamePositionY: 30,
      txtNameFont: '20px "Impact", sans-serif',
      txtNameLineHeight: 60,
    //#region TypeTextVariables
        txtType: '',
        txtTypeMaxWidth: 250,
        txtTypeStrokeStyle: '#000000',
        txtTypeFillStyle: '#FFFFFF',
        txtTypeLineWidth: 1,
        txtTypePositionX: 36,
        txtTypePositionY: 320,
        txtTypeFont: '20px "Impact", sans-serif',
        txtTypeLineHeight: 60,
    //#region SubTypeTextVariables
      txtSubType: '',
      txtSubTypeMaxWidth: 250,
      txtSubTypeStrokeStyle: '#000000',
      txtSubTypeFillStyle: '#FFFFFF',
      txtSubTypeLineWidth: 1,
      txtSubTypePositionX: 108,
      txtSubTypePositionY: 317,
      txtSubTypeFont: '20px "Impact", sans-serif',
      txtSubTypeLineHeight: 60,
    //#region FlavorTextVariables
      txtFlavor: '',
      txtFlavorMaxWidth: 250,
      txtFlavorStrokeStyle: '#000000',
      txtFlavorFillStyle: '#FFFFFF',
      txtFlavorLineWidth: 1,
      txtFlavorPositionX: 45,
      txtFlavorPositionY: 471,
      txtFlavorFont: '20px "Impact", sans-serif',
      txtFlavorLineHeight: 60,
    //#region BottomInfoVariables
      txtBottom: '',
      txtBottomMaxWidth: 250,
      txtBottomStrokeStyle: '#000000',
      txtBottomFillStyle: '#FFFFFF',
      txtBottomLineWidth: 1,
      txtBottomPositionX: 10,
      txtBottomPositionY: 514,
      txtBottomFont: '15px "Impact", sans-serif',
      txtBottomLineHeight: 60,
    //#region ForceTextVariables
      txtForce: '',
      txtForceMaxWidth: 250,
      txtForceStrokeStyle: '#000000',
      txtForceFillStyle: '#FFFFFF',
      txtForceLineWidth: 1,
      txtForcePositionX: 6,
      txtForcePositionY: 507,
      txtForceFont: '20px "Impact", sans-serif',
      txtForceLineHeight: 60,
    //#region VitalityTextVariables
      txtVitality: '',
      txtVitalityMaxWidth: 250,
      txtVitalityStrokeStyle: '#000000',
      txtVitalityFillStyle: '#FFFFFF',
      txtVitalityLineWidth: 1,
      txtVitalityPositionX: 356,
      txtVitalityPositionY: 507,
      txtVitalityFont: '20px "Impact", sans-serif',
      txtVitalityLineHeight: 60,
  //#region Other
    selectErrors: [],
  //#endregion
  }),
mounted() 
    {
    //this.checkPlayerProfile(this.user)
    //this.setImage(this.framePreset)
    
    //this.arrIndex = (this.textProperties.indexOf(this.textPropertySelected))
    //this.setArrays()
    this.setDataSnapShot()
    this.getCardCollection()
  },
methods: {
  next () {
      this.loading = true
      setTimeout(() => {
        this.subtypes = ''
        this.subtype_selected = []
        this.loading = false
      }, 2000)
    },
  async setDataSnapShot() {
    this.dataSnapShot = this.$data
      // console.log("new dataSnapShot saved")
      // console.log(this.dataSnapShot)
    },
  async increment() {
      switch(this.affinityselected) {
      case ('Light'):
        this.txtLightCost = String(parseInt(this.txtLightCost, 10) + 1)
        break;
      case ('Dark'):
        this.txtDarkCost = String(parseInt(this.txtDarkCost, 10) + 1)
        break;
      case ('Fire'):
        this.txtFireCost = String(parseInt(this.txtFireCost, 10) + 1)
        break;
      case ('Water'):
        this.txtWaterCost = String(parseInt(this.txtWaterCost, 10) + 1)
        break;
      case ('Nature'):
        this.txtNatureCost = String(parseInt(this.txtNatureCost, 10) + 1)
        break;
      case ('Air'):
        this.txtAirCost = String(parseInt(this.txtAirCost, 10) + 1)
        break;
      case ('Basic'):
        this.txtBasicCost = String(parseInt(this.txtBasicCost, 10) + 1)
        break;
      }
    },
  async decrement() {
    switch(this.affinityselected) {
      case ('Light'):
        this.txtLightCost = String(parseInt(this.txtLightCost, 10) - 1)
        break;
      case ('Dark'):
        this.txtDarkCost = String(parseInt(this.txtDarkCost, 10) - 1)
        break;
      case ('Fire'):
        this.txtFireCost = String(parseInt(this.txtFireCost, 10) - 1)
        break;
      case ('Water'):
        this.txtWaterCost = String(parseInt(this.txtWaterCost, 10) - 1)
        break;
      case ('Nature'):
        this.txtNatureCost = String(parseInt(this.txtNatureCost, 10) - 1)
        break;
      case ('Air'):
        this.txtAirCost = String(parseInt(this.txtAirCost, 10) - 1)
        break;
      case ('Basic'):
        this.txtBasicCost = String(parseInt(this.txtBasicCost, 10) - 1)
        break;
      }
    },
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
        "last_name": this.last
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
            this.username = this.player_profile.username
            this.date = this.player_profile.age
            this.pronouns = this.player_profile.pronouns
            this.region = this.player_profile.region
            this.records = this.player_profile.records
            this.facts = this.player_profile.facts
            this.email = this.user.email
            this.subtype_selectedGames = this.player_profile.games
            this.ImgUrl = this.player_profile.ImgUrl
        },
  async newPlayerProfile(user_id) {
      let id = {
        "id": user_id
      }
      let payload = {
        "user": id
      }
      // console.log(payload)
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
    },
  async createCardData() {
      let cardData = 
      {
      "txt_light_cost": {
          "text": this.txtLightCost,
          "max_width": this.txtLightCostMaxWidth,
          "stroke_style": this.txtLightCostStrokeStyle,
          "fill_style": this.txtLightCostFillStyle,
          "line_width": this.txtLightCostLineWidth,
          "position": {
            "x": this.txtLightCostPositionX,
            "y": this.txtLightCostPositionY
          },
          "font": this.txtLightCostFont,
          "line_height:": this.txtLightCostLineHeight
        },
      "txt_dark_cost": {
          "text": this.txtDarkCost,
          "max_width": this.txtDarkCostMaxWidth,
          "stroke_style": this.txtDarkCostStrokeStyle,
          "fill_style": this.txtDarkCostFillStyle,
          "line_width": this.txtDarkCostLineWidth,
          "position": {
            "x": this.txtDarkCostPositionX,
            "y": this.txtDarkCostPositionY
          },
          "font": this.txtDarkCostFont,
          "line_height:": this.txtDarkCostLineHeight
        },
      "txt_fire_cost": {
          "text": this.txtFireCost,
          "max_width": this.txtFireCostMaxWidth,
          "stroke_style": this.txtFireCostStrokeStyle,
          "fill_style": this.txtFireCostFillStyle,
          "line_width": this.txtFireCostLineWidth,
          "position": {
            "x": this.txtFireCostPositionX,
            "y": this.txtFireCostPositionY
          },
          "font": this.txtFireCostFont,
          "line_height:": this.txtFireCostLineHeight
        },
      "txt_water_cost": {
          "text": this.txtWaterCost,
          "max_width": this.txtWaterCostMaxWidth,
          "stroke_style": this.txtWaterCostStrokeStyle,
          "fill_style": this.txtWaterCostFillStyle,
          "line_width": this.txtWaterCostLineWidth,
          "position": {
            "x": this.txtWaterCostPositionX,
            "y": this.txtWaterCostPositionY
          },
          "font": this.txtWaterCostFont,
          "line_height:": this.txtWaterCostLineHeight
        },
      "txt_nature_cost": {
          "text": this.txtNatureCost,
          "max_width": this.txtNatureCostMaxWidth,
          "stroke_style": this.txtNatureCostStrokeStyle,
          "fill_style": this.txtNatureCostFillStyle,
          "line_width": this.txtNatureCostLineWidth,
          "position": {
            "x": this.txtNatureCostPositionX,
            "y": this.txtNatureCostPositionY
          },
          "font": this.txtNatureCostFont,
          "line_height:": this.txtNatureCostLineHeight
        },
      "txt_air_cost": {
          "text": this.txtAirCost,
          "max_width": this.txtAirCostMaxWidth,
          "stroke_style": this.txtAirCostStrokeStyle,
          "fill_style": this.txtAirCostFillStyle,
          "line_width": this.txtAirCostLineWidth,
          "position": {
            "x": this.txtAirCostPositionX,
            "y": this.txtAirCostPositionY
          },
          "font": this.txtAirCostFont,
          "line_height:": this.txtAirCostLineHeight
        },
      "txt_basic_cost": {
          "text": this.txtBasicCost,
          "max_width": this.txtBasicCostMaxWidth,
          "stroke_style": this.txtBasicCostStrokeStyle,
          "fill_style": this.txtBasicCostFillStyle,
          "line_width": this.txtBasicCostLineWidth,
          "position": {
            "x": this.txtBasicCostPositionX,
            "y": this.txtBasicCostPositionY
          },
          "font": this.txtBasicCostFont,
          "line_height:": this.txtBasicCostLineHeight
        },
      "txt_total_cost": {
          "text": this.txtTotalCost,
          "max_width": this.txtTotalCostMaxWidth,
          "stroke_style": this.txtTotalCostStrokeStyle,
          "fill_style": this.txtTotalCostFillStyle,
          "line_width": this.txtTotalCostLineWidth,
          "position": {
            "x": this.txtTotalCostPositionX,
            "y": this.txtTotalCostPositionY
          },
          "font": this.txtTotalCostFont,
          "line_height:": this.txtTotalCostLineHeight
        },
      "txt_name": {
          "text": this.txtName,
          "max_width": this.txtNameMaxWidth,
          "stroke_style": this.txtNameStrokeStyle,
          "fill_style": this.txtNameFillStyle,
          "line_width": this.txtNameLineWidth,
          "position": {
            "x": this.txtNamePositionX,
            "y": this.txtNamePositionY
          },
          "font": this.txtNameFont,
          "line_height:": this.txtNameLineHeight
        },
      "txt_main": {
          "text": this.txtMain,
          "max_width": this.txtMainMaxWidth,
          "stroke_style": this.txtMainStrokeStyle,
          "fill_style": this.txtMainFillStyle,
          "line_width": this.txtMainLineWidth,
          "position": {
            "x": this.txtMainPositionX,
            "y": this.txtMainPositionY
          },
          "font": this.txtMainFont,
          "line_height:": this.txtMainLineHeight
        },
      "txt_type": {
          "text": this.txtType,
          "max_width": this.txtTypeMaxWidth,
          "stroke_style": this.txtTypeStrokeStyle,
          "fill_style": this.txtTypeFillStyle,
          "line_width": this.txtTypeLineWidth,
          "position": {
            "x": this.txtTypePositionX,
            "y": this.txtTypePositionY
          },
          "font": this.txtTypeFont,
          "line_height:": this.txtTypeLineHeight
        },
      "txt_subtype": {
          "text": this.txtSubType,
          "max_width": this.txtSubTypeMaxWidth,
          "stroke_style": this.txtSubTypeStrokeStyle,
          "fill_style": this.txtSubTypeFillStyle,
          "line_width": this.txtSubTypeLineWidth,
          "position": {
            "x": this.txtSubTypePositionX,
            "y": this.txtSubTypePositionY
          },
          "font": this.txtSubTypeFont,
          "line_height:": this.txtSubTypeLineHeight
        },
      "txt_flavor": {
          "text": this.txtFlavor,
          "max_width": this.txtFlavorMaxWidth,
          "stroke_style": this.txtFlavorStrokeStyle,
          "fill_style": this.txtFlavorFillStyle,
          "line_width": this.txtFlavorLineWidth,
          "position": {
            "x": this.txtFlavorPositionX,
            "y": this.txtFlavorPositionY
          },
          "font": this.txtFlavorFont,
          "line_height:": this.txtFlavorLineHeight
        },
      "txt_bottom": {
          "text": this.txtBottom,
          "max_width": this.txtBottomMaxWidth,
          "stroke_style": this.txtBottomStrokeStyle,
          "fill_style": this.txtBottomFillStyle,
          "line_width": this.txtBottomLineWidth,
          "position": {
            "x": this.txtBottomPositionX,
            "y": this.txtBottomPositionY
          },
          "font": this.txtBottomFont,
          "line_height:": this.txtBottomLineHeight
        },
      "txt_force": {
          "text": this.txtForce,
          "max_width": this.txtForceMaxWidth,
          "stroke_style": this.txtForceStrokeStyle,
          "fill_style": this.txtForceFillStyle,
          "line_width": this.txtForceLineWidth,
          "position": {
            "x": this.txtForcePositionX,
            "y": this.txtForcePositionY
          },
          "font": this.txtForceFont,
          "line_height:": this.txtForceLineHeight
        },
      "txt_vitality": {
          "text": this.txtVitality,
          "max_width": this.txtVitalityMaxWidth,
          "stroke_style": this.txtVitalityStrokeStyle,
          "fill_style": this.txtVitalityFillStyle,
          "line_width": this.txtVitalityLineWidth,
          "position": {
            "x": this.txtVitalityPositionX,
            "y": this.txtVitalityPositionY
          },
          "font": this.txtVitalityFont,
          "line_height:": this.txtVitalityLineHeight
        },
      "cardtype": this.cardtype,
      "affinity_selected": this.affinityselected,
      "subtype_selected": this.subtype_selected,
      "canvas_property_selected": this.canvasPropertySelected,
      "canvas_width": this.width,
      "canvas_height": this.height,
      "image_width": this.imageWidth,
      "image_height": this.imageHeight,
      "card_frame": this.cardFrame,
      "card_image_width": this.cardImageWidth,
      "card_image_height": this.cardImageHeight,
      "card_image_positionX": this.cardImagePositionX,
      "card_image_positionY": this.cardImagePositionY,
      "card_frame_chkbx": this.cardFrameCheckbox,
      "card_image_apsect_percentage": this.cardImageAspectPercentage
      }
    },
  async setArrays() {
    //Remove first index from arrPositionX and arrPositionY because its dumby data from the v-model settings. 
    this.arrPositionX.shift();
    this.arrPositionY.shift();
    
    var dataKey
    var numKeys = 0
    var dataKeys = Object.keys(this.$data)
    //// console.log(dataKeys)
    //// console.log(dataKeys[2])
    for (dataKey in dataKeys) {
        var currentDataKey = dataKeys[numKeys]
        //// console.log(currentDataKey)
        if(currentDataKey.startsWith("txt", 0)) {
          //// console.log(numKeys)
          //// console.log(currentDataKey)
          //set properties in the arrays 
          switch(true) {
            case (currentDataKey.includes("MaxWidth")):
                //// console.log("MaxWidth")
                this.arrMaxWidth.push(this.$data[currentDataKey])
                break;
            case (currentDataKey.includes("StrokeStyle")):
                //// console.log("StrokeStyle")
                this.arrStrokeStyle.push(this.$data[currentDataKey])
                break;
            case (currentDataKey.includes("FillStyle")):
                //// console.log("FillStyle")
                this.arrFillStyle.push(this.$data[currentDataKey])
                break;
            case (currentDataKey.includes("LineWidth")):
                //// console.log("LineWidth")
                this.arrLineWidth.push(this.$data[currentDataKey])
                break;
            case (currentDataKey.includes("PositionX")):
                // // console.log(currentDataKey + "PositionX")
                // // console.log(this.$data[currentDataKey])
                this.arrPositionX.push(this.$data[currentDataKey])
                break;
            case (currentDataKey.includes("PositionY")):
                // // console.log(currentDataKey + "PositionY")
                // // console.log(this.$data[currentDataKey])
                this.arrPositionY.push(this.$data[currentDataKey])
                break;
            case (currentDataKey.includes("Font")):
                //// console.log("Font")
                this.arrFont.push(this.$data[currentDataKey])
                break;
            case (currentDataKey.includes("LineHeight")):
                //// console.log("LineHeight")
                this.arrLineHeight.push(this.$data[currentDataKey])
                break;
            default:
                //// console.log("Text Value")
          }
          }
        numKeys++  
        }
        
      }, 
  async setCostTotal() {
    var light = Number(this.txtLightCost)
    var dark = Number(this.txtDarkCost)
    var fire = Number(this.txtFireCost)
    var water = Number(this.txtWaterCost)
    var nature = Number(this.txtNatureCost)
    var air = Number(this.txtAirCost)
    var basic = Number(this.txtBasicCost)
    
    var total = light + dark + fire + water + nature + basic
    this.txtTotalCost = String(total)
    },
  async onCardDataChange() {
    
    let file = this.cardData;
    if(!file || file.type !== 'application/json') return;
    // Credit: https://stackoverflow.com/a/754398/52160
    let reader = new FileReader();
    reader.readAsText(file, "UTF-8");
    var jsonData = ''
    reader.onload =  evt => {
      var obj = JSON.parse(event.target.result);
      try {
        //Set card data 
        var key
        var numKeys = 0
        var keys = Object.keys(obj)
        for (key in keys) {
          var currentKey = keys[numKeys]
          if(currentKey.startsWith("txt", 0))
          {
            //// console.log(currentKey)
            this.$data[stringService.convertCamel(currentKey)] = obj[currentKey].text
            //// console.log([stringService.convertCamel(currentKey)])
            this.$data[stringService.convertCamel(currentKey) + "MaxWidth"] = obj[currentKey].max_width
            //// console.log(this.$data[stringService.convertCamel(currentKey) + "MaxWidth"])
            this.$data[stringService.convertCamel(currentKey) + "StrokeStyle"] = obj[currentKey].stroke_style
            //// console.log(this.$data[stringService.convertCamel(currentKey) + "StrokeStyle"])
            this.$data[stringService.convertCamel(currentKey) + "FillStyle"] = obj[currentKey].fill_style
            //// console.log(this.$data[stringService.convertCamel(currentKey) + "FillStyle"])
            this.$data[stringService.convertCamel(currentKey) + "LineWidth"] = obj[currentKey].line_width
            //// console.log(this.$data[stringService.convertCamel(currentKey) + "LineWidth"])
            this.$data[stringService.convertCamel(currentKey) + "PositionX"] = obj[currentKey].position.x
            //// console.log(this.$data[stringService.convertCamel(currentKey) + "PositionX"])
            this.$data[stringService.convertCamel(currentKey) + "PositionY"] = obj[currentKey].position.y
            //// console.log(this.$data[stringService.convertCamel(currentKey) + "PositionY"])
            this.$data[stringService.convertCamel(currentKey) + "Font"] = obj[currentKey].font
            //// console.log(this.$data[stringService.convertCamel(currentKey) + "Font"])
            this.$data[stringService.convertCamel(currentKey) + "LineHeight"] = obj[currentKey].line_height
            //// console.log(this.$data[stringService.convertCamel(currentKey) + "LineHeight"])
          }
          numKeys++
        }
      //add single attribute variables
      this.cardtype = obj.cardtype
      this.affinityselected = obj.affinity_selected
      this.subtype_selected = obj.subtype_selected
      this.canvasPropertySelected = obj.canvas_property_selected
      this.width = obj.canvas_width = obj.canvas_width
      this.height = obj.canvas_height
      this.imageWidth = obj.image_width
      this.imageHeight = obj.image_height
      this.cardFrame = obj.card_frame
      this.cardImageWidth = obj.card_image_width
      this.cardImageHeight = obj.card_image_height
      this.cardImagePositionX = obj.card_image_positionX
      this.cardImagePositionY = obj.card_image_positionY
      this.cardFrameCheckbox = obj.card_frame_chkbx
      this.cardImageAspectPercentage = obj.card_image_apsect_percentage
            
      } catch(e) {
        alert("Sorry, your file doesn't appear to be valid JSON data.");
        alert(e)
      }
    }
            
      reader.onerror = evt => {
        console.error(evt);
      }
    }, 
  async onImageChange() {
    //var files = event.target.files || event.dataTransfer.files;
    //if (!selectedImage.length)
      //return;
    //this.createImage(files[0]);
    //// console.log(files[0])
    // console.log(this.selectedImage.name)
    var vm = this
    let reader = new FileReader();
    reader.readAsDataURL(this.selectedImage);
    reader.onload = evt => {
      let img = new Image();
      img.onload = function(event) {
        vm.cardImageWidth = img.width;
        vm.cardImageHeight = img.height;
        vm.imageWidth = vm.cardImageWidth
        vm.imageHeight = vm.cardImageHeight
      };
      
      img.onerror = function() {
        alert( "not a valid file: " + file.type);
      };
      img.src = evt.target.result;
    }
    let img = new Image();
    this.createImage(this.selectedImage)
    },
    

  async onSizeChange(event) {
    //Get percentage of width and height
    this.cardImageWidth = mathService.GetPercentage(this.imageWidth, this.cardImageAspectPercentage)
    this.cardImageHeight = mathService.GetPercentage(this.imageHeight, this.cardImageAspectPercentage)
    this.repaint();
    },
  async createImage(file) { 
    var reader = new FileReader();
    reader.onload = evt => {
      var image = new Image();
    }
    var vm = this;
    reader.onload = function(event) {
      
      vm.image = event.target.result;
      vm.paint();
    };
    reader.readAsDataURL(file);
    },
  
  
  // Draw Image Methods
    async setImage(url) {
      this.image = url;
      this.paint();
      },
    async setImageToCanvas(url, callback, callback2) {
          var vm = this; 
          var ctx = this.getContext();
          var background = new Image();
          background.src = url
          background.onload = function() {
            ctx.drawImage(background, vm.cardImagePositionX, vm.cardImagePositionY, vm.cardImageWidth, vm.cardImageHeight);
            if ( typeof callback == 'function' ) {
            callback();
          }
          if ( typeof callback2 == 'function' ) {
            callback2();
          }
        };
      },    
    async setImageToCanvasFirst(url, callback, callback2) {
          var vm = this;
          var ctx = this.getContext();
          var background = new Image();
          background.src = url
          background.onload = function() {
            ctx.drawImage(background, 0, 0);
            if ( typeof callback == 'function' ) {
            callback();
          }
          if ( typeof callback2 == 'function' ) {
            callback2();
          }
          
        };
      },
    async setCardFrameToCanvas() {
      if(this.cardFrameCheckbox == true) {
          var vm = this;
          var ctx = this.getContext();
          var background = new Image();
          background.src = vm.presets[0]
          ctx.drawImage(background, 0, 0, vm.width, vm.height);
        }
      },
    async setTextToCanvas(text) {
        var context = this.getContext();
        var textProperty
        var numProperties = 0
        var textProperties = Object.keys(this.textProperties)
        for (textProperty in this.textProperties)
        {
          var currentContextProperty = this.textProperties[textProperty]
          context.font = this.$data[currentContextProperty + "Font"];
          context.fillStyle = this.$data[currentContextProperty + "FillStyle"];
          context.wrapFillText(this.$data[currentContextProperty], this.$data[currentContextProperty + "PositionX"], 
          this.$data[currentContextProperty + "PositionY"], this.$data[currentContextProperty + "MaxWidth"], this.$data[currentContextProperty + "LineHeight"]);
          context.strokeStyle = this.$data[currentContextProperty + "StrokeStyle"];
          context.lineWidth = this.$data[currentContextProperty + "LineWidth"];
          context.wrapStrokeText(this.$data[currentContextProperty], this.$data[currentContextProperty + "PositionX"], 
          this.$data[currentContextProperty + "PositionY"], this.$data[currentContextProperty + "MaxWidth"], this.$data[currentContextProperty + "LineHeight"]);
        }
      },
    async setTextProperty(setfont, setfillStyle, settxt, setx, sety, setmaxWidth, setlineHeight, setstrokeStyle, setlineWidth) {
      var context = this.getContext();
      
      context.font = setfont;
      context.fillStyle = setfillStyle;
      context.wrapFillText(settxt, setx, sety, setmaxWidth, setlineHeight);
      context.strokeStyle = setstrokeStyle;
      context.lineWidth = setlineWidth;
      context.wrapStrokeText(settxt, setx, sety, setmaxWidth, setlineHeight);
        },
  
    async paint() {
        var vm = this;
        if ( this.image == '' )
          this.setTextToCanvas(this.text);
        this.getContext().clearRect(0, 0, this.width, this.height);
        
        this.setImageToCanvasFirst(this.image, function(){
            vm.setCardFrameToCanvas(); }, function() {
            vm.setTextToCanvas(vm.text);
          }
        );
      },  
    async repaint() {
      var vm = this;
      if ( this.image == '' )
        this.setTextToCanvas(this.text);
      this.getContext().clearRect(0, 0, this.width, this.height);
      this.setImageToCanvas(this.image, function(){
      vm.setCardFrameToCanvas(); }, function() {
          vm.setTextToCanvas(vm.text);
    });
      this.setDataSnapShot()
    },
  // User Button Methods
    async reset() {
      this.deck = []
      this.sortedDeck = [...new Set(this.deck)];
      this.getSortedDeckQuantity(this.sortedDeck)
      },
    async info(event) {
      /* var dt = document.getElementById(this.canvasElementId).toDataURL('image/png');
      // console.log("current image" + dt) */
      console.log(this.$data)
        /*  var numProperties = 0
        var textProperties = Object.keys(this.textProperties)
        for (textProperty in this.textProperties) 
        {
          // console.log(this.textProperties[textProperty])
          // console.log(this.textProperties[textProperty] + "Font")
        } */
      },
    async downloadDeckData(sortedDeck, sortedDeckQty) {
        var deckListData = await this.createDeckListData(sortedDeck, sortedDeckQty)
        this.downloadDeckListData(deckListData)
      },
    async downloadDeckListData(deckListData) {
      let filename = (this.txtDeckName) ? (this.txtDeckName + ".json") : "deck.json"
      let jsonData = ''
      jsonData = JSON.stringify(deckListData, null, 2)
      let blob = new Blob([jsonData], { type: 'application/json' })
      if (navigator.msSaveBlob) { // IE 10+
        navigator.msSaveBlob(blob, filename)
      } else {
        let link = document.createElement('a')
        if (link.download !== undefined) { // feature detection
          // Browsers that support HTML5 download attribute
          let url = URL.createObjectURL(blob)
          link.setAttribute('href', url)
          link.setAttribute('download', filename)
          link.style.visibility = 'hidden'
          document.body.appendChild(link)
          link.click()
          document.body.removeChild(link)
          } 
        }
      },
  // Card Collection Methods
    async getCardCollection() {
      const CardCollection = await cardService.fetchCollection()
      this.cardCollection = CardCollection
    },
  // Deck List Bar Methods
    async addToDeck(card){
      this.deck.push(card)
      console.log(this.deck)
      this.sortedDeck = [...new Set(this.deck)];
      console.log(this.sortedDeck)
      this.getSortedDeckQuantity(this.sortedDeck)
      console.log(this.sortedDeckQty)
      },
    async increaseCardQty(card) {
      this.deck.push(card)
      this.sortedDeck = [...new Set(this.deck)];
      this.getSortedDeckQuantity(this.sortedDeck)
      },
    async decreaseCardQty(card) {
      arrayService.removeItemOnce(this.deck, card)
      this.sortedDeck = [...new Set(this.deck)];
      this.getSortedDeckQuantity(this.sortedDeck)
      },
    async getSortedCardSet(currentCard) {
      let sortedCardSet = {
        "card_name": currentCard.txtName,
        "affinity_cost_total": currentCard.txtTotalCost,
        "affinity_cost_light": currentCard.txtLightCost,
        "affinity_cost_dark": currentCard.txtDarkCost,
        "affinity_cost_fire": currentCard.txtFireCost,
        "affinity_cost_water": currentCard.txtWaterCost,
        "affinity_cost_nature": currentCard.txtNatureCost,
        "affinity_cost_air": currentCard.txtAirCost,
        "affinity_cost_basic": currentCard.txtBasicCost,
        "card_type": currentCard.txtType,
        "card_subtypes": currentCard.txtSubtype,
        "card_maintext": currentCard.txtMain,
        "card_flavortext": currentCard.txtFlavor,
        "card_bottomtext": currentCard.txtBottom,
        "card_forcetext": currentCard.txtForce,
        "card_vitalitytext": currentCard.txtVitality,
        "card_serialnumber": currentCard.card_serialnumber,
        "card_set": currentCard.card_set,
        "player_profile": currentCard.player_profile,
        "description": currentCard.description,
        "img_url": currentCard.imgUrl,
        "cardimg_url": currentCard.cardImgUrl,
        "card_data": currentCard.cardData,
        "extra_data": currentCard.extra_data,
        "uuid": currentCard.uuid,
        "qty": 1
      }

      return sortedCardSet
      }, 
    async sortDeck(deck) {
      for(var currentCard in deck) {
        var newSortedCardSet = this.getSortedCardSet(currentCard)
        
        
        if(this.sortedDeck != "") 
        {
          for(var currentSortedCardSet in this.sortedDeck)
          {  
          if(newSortedCardSet.uuid == currentSortedCardSet.uuid) 
            {
              var currentIndex = this.sortedDeck.indexOf(currentSortedCardSet)
              this.sortedDeck[currentIndex].qty = this.sortedDeck[currentIndex].qty + 1
            }
            else
            {
              this.sortedDeck.push(newSortedCardSet)
            }
          }
        }
        else
        {
          this.sortedDeck.push(newSortedCardSet)
        }
      }
      },
    async getSortedDeckQuantity(sortedDeck) {
      var newSortedDeckQty = []
      for(var cardSet in sortedDeck) {
        console.log(this.sortedDeck[cardSet].card_name)
        console.log(this.deck.filter(x => x=== this.sortedDeck[cardSet]).length)
        newSortedDeckQty.push(this.deck.filter(x => x=== this.sortedDeck[cardSet]).length)
      }

      this.sortedDeckQty = newSortedDeckQty
      },
    async createDeckListData(sortedDeck, sortedDeckQty) {
      // For each card in sortedDeck 
      var deckListData = []
      for(var cardSetIndex in sortedDeck) {
        let currentCardSet = {
        "name": sortedDeck[cardSetIndex].card_name,
        "uuid": sortedDeck[cardSetIndex].uuid,
        "qty": sortedDeckQty[cardSetIndex]
        }
        deckListData.push(currentCardSet)
      }
      return deckListData
    },
  // Deck service methods
    async updateCurrentDeck() {

      },
    async publishDeck() {
      console.log("You published the deck")
      },
    async postDeck(sortedDeck, sortedDeckQty) {
      var deckListData = await this.createDeckListData(sortedDeck, sortedDeckQty)
      let newDeck = {
          "deck_name": this.txtDeckName,
          "player_profile_id": this.user.player_profile_id,
          "card_list": deckListData
          }  
      const response = await deckService.createDeck(newDeck)
      .then((response) =>{
        switch(response.status) {
          case (200): 
            this.displayNotification('authentication', 'Success!.', newDeck.deck_name + ' was created successfully' , 'success')
            break;
          case (201): 
            this.displayNotification('authentication', 'Success!.', newDeck.deck_name + ' was created successfully' , 'success')
            break;
          case (400): 
            this.displayNotification('authentication', 'Bad Request!', response, 'warn')
            break;
          case (500): 
            this.displayNotification('authentication', 'Internal server error', 'Something went wrong on our end', 'error')
            break;   
          }
        });

      },
    async patchDeck() {
      // Call Deckservice
        const response = await deckService.updateDeck(this.deckId, payload)
        .then((response) =>{
        switch(response.status) {
          case (200): 
            console.log("Success patched!")
            this.displayNotification('authentication', 'Deck saved.', this.active[0].Name + ' was updated successfully' , 'success')
            break;
          case (404): 
            this.displayNotification('authentication', 'Deck NOT found!', 'Please try creating a new Deck first', 'warn')
            break;
          case (500): 
            this.displayNotification('authentication', 'Internal server error', 'Something went wrong on our end', 'error')
            break;   
          }
        });
      },
    
    async saveDeck() {
        // deck logic
        this.patchDeck()
      },
    async delDeck() {
      await deckService.deleteDeck(this.deckId, payload)
      },
  },
watch: {
  cardFrameCheckbox(cardFrameCheckbox) {
    // console.log("Card frame change detected")
    this.setCardFrameToCanvas();
    this.repaint();
    },
  cardtype(cardtype) {
    switch(cardtype) {
      case ('Creature'):
        this.txtType = cardtype
        this.creature_enabled = true
        this.repaint();
        break;
      case ('Construct'):
        this.txtType = cardtype
        this.creature_enabled = false
        this.repaint();
        break;
      case ('Spell'):
        this.txtType = cardtype
        this.creature_enabled = false
        this.repaint();
        break;
      case ('Immortal'):
        this.txtType = cardtype
        this.creature_enabled = false
        this.repaint();
        break;  
      case ('Construct Creature'):
        this.txtType = cardtype
        this.creature_enabled = true
        this.repaint();
        break;
      default:
        this.creature_enabled = false
        break;
      }
    },
  cardImagePositionX(cardImagePositionX) {
    this.repaint()
    },
  cardImagePositionY(cardImagePositionY) {
    this.repaint()
    },
  textPropertySelected(textPropertySelected) {
      var currentIndex = (this.textProperties.indexOf(textPropertySelected))
      this.arrIndex = currentIndex    
    },
  arrMaxWidth(arrMaxWidth) {
      // console.log("MaxWidth Change detected")
      this.$data[this.textPropertySelected + "MaxWidth"] = arrMaxWidth[this.arrIndex]
      this.repaint();
    },
  arrStrokeStyle(arrStrokeStyle) {
      // console.log("StrokeStyle Change detected")
      this.$data[this.textPropertySelected + "StrokeStyle"] = arrStrokeStyle[this.arrIndex]
      this.repaint();
    },
  arrFillStyle(arrFillStyle) {
      // console.log("FillStyle Change detected")
      this.$data[this.textPropertySelected + "FillStyle"] = arrFillStyle[this.arrIndex]
      this.repaint();
    },
  arrLineWidth(arrLineWidth) {
      // console.log("LineWidth Change detected")
      this.$data[this.textPropertySelected + "LineWidth"] = arrLineWidth[this.arrIndex]
      this.repaint();
    },
  arrPositionX(arrPositionX) {
      // console.log("Change detected x")
      this.$data[this.textPropertySelected + "PositionX"] = this.arrPositionX[this.arrIndex]
      this.repaint();
    },
  arrPositionY(arrPositionY) {
      // console.log("Change detected y")
      this.$data[this.textPropertySelected + "PositionY"] = this.arrPositionY[this.arrIndex]
      this.repaint();
    },
  arrFont(arrFont) {
      // console.log("Font Change detected")
      this.$data[this.textPropertySelected + "Font"] = arrFont[this.arrIndex]
      this.repaint();
    },
  arrLineHeight(arrLineHeight) {
      // console.log("Line Height Change detected")
      this.$data[this.textPropertySelected + "LineHeight"] = arrLineHeight[this.arrIndex]
      this.repaint();
    },  
  txtLightCost(txtLightCost) {
    this.setCostTotal();
    this.repaint();
    },
  txtDarkCost(txtDarkCost) {
    this.setCostTotal();
    this.repaint();
    },
  txtFireCost(txtFireCost) {
    this.setCostTotal();
    this.repaint();
    },
  txtWaterCost(txtWaterCost) {
    this.setCostTotal();
    this.repaint();
    },
  txtNatureCost(txtNatureCost) {
    this.setCostTotal();
    this.repaint();
    },
  txtAirCost(txtAirCost) {
    this.setCostTotal();
    this.repaint();
    },
  txtBasicCost(txtBasicCost) {
    this.setCostTotal();
    this.repaint();
    },
  txtName(txtName) {
    this.repaint();
    },
  txtMain(txtMain) {
    this.repaint();
    },
  txtType(txtType) {
    this.repaint();
    },
  txtFlavor(txtFlavor) {
    this.repaint();
    },
  txtBottom(txtBottom) {
    this.repaint();
    },
  txtForce(txtForce) {
    this.repaint();
    },
  txtVitality(txtVitality) {
    this.repaint();
    },
  
  subtype_selected(subtype_selected) {
      var currentSubTypeItems = ""
      for (var subType in this.subtype_selected) {
        // console.log(this.subtype_items[subType].text)
        currentSubTypeItems = currentSubTypeItems + (this.subtype_items[subType].text + " ")
      }
      this.txtSubType = currentSubTypeItems
      //this.repaint();
    }
    },
computed: {
    user: {
      get() {
        return JSON.parse(this.$store.state.authenticatedUser)
        }
      },
    allsubtype_selected () {
      return this.subtype_selected.length === this.subtype_items.length
      },
    categories () {
      const subtypes = this.subtypes.toLowerCase()
      if (!subtypes) return this.subtype_items
      return this.subtype_items.filter(item => {
        const text = item.text.toLowerCase()
        return text.indexOf(subtypes) > -1
      })
      },
    subtype_selections () {
      const subtype_selections = []
      for (const subtype_selection of this.subtype_selected) {
        subtype_selections.push(this.subtype_items[subtype_selection])
        // console.log(this.subtype_items[subtype_selection])
      }
      
      return subtype_selections
      },
  }
}
</script>



<style scoped>
.wrap-subtitle {
  -webkit-line-clamp: unset !important;
}

.wrap-title {
  white-space: normal;
}

.heading {
  margin-bottom: 1em !important;
}

.fixed {
  position: fixed;
}

.title {
  margin-bottom: 7em !important;
}

a {
  color: #fff !important;
  text-decoration: none;
}

.decklistbar {
  width: 450px;
  height: 500px;
  overflow-y: scroll;
}

.preset img {
  width: 100%;
  height: auto;
}

#canvas {
  background-color: rgba(160, 160, 160, 0.685);
}

.v-card {
  width: 200px;
  height: 280px;
  margin-bottom: 2em;

}

#collection {
  display: flex;
  flex-flow: row wrap;
}

.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.5;
  position: absolute;
}
</style>