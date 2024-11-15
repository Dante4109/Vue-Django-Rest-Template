<template>
  <v-container fluid>
    <v-row align="center">
      
    <v-col cols="12">
      <div 
      align="center"
      class="title"
      >
        <h1>Card Creator</h1>
      </div>
    </v-col>
  
  </v-row>
  </V-container>  
</template>

<script>
//import axios from 'axios';
import userService from '@/services/userService';
import canvasService from '@/services/canvasService'
import mathService from '@/services/mathService'

//#region Card Preview Canvas Scripts
  /**
   * @credits http://stackoverflow.com/questions/5026961/html5-canvas-ctx-filltext-wont-do-line-breaks
   *
   * @param text
   * @param x
   * @param y
   * @param maxWidth
   * @param lineHeight
   */  

  CanvasRenderingContext2D.prototype.wrapFillText = function (text, x, y, maxWidth, lineHeight) {

      var lines = text.split("\n");

      for (var i = 0; i < lines.length; i++) {

        var words = lines[i].split(' ');
        var line = '';

        for (var n = 0; n < words.length; n++) {
          var testLine = line + words[n] + ' ';
          var metrics = this.measureText(testLine);
          var testWidth = metrics.width;
          if (testWidth > maxWidth && n > 0) {
            this.fillText(line, x, y);
            line = words[n] + ' ';
            y += lineHeight;
          }
          else {
            line = testLine;
          }
        }

        this.fillText(line, x, y);
        y += lineHeight;
      }
    }

  /**
   * @credits http://stackoverflow.com/questions/5026961/html5-canvas-ctx-filltext-wont-do-line-breaks
   *
   * @param text
   * @param x
   * @param y
   * @param maxWidth
   * @param lineHeight
   */
  CanvasRenderingContext2D.prototype.wrapStrokeText = function (text, x, y, maxWidth, lineHeight) {

    var lines = text.split("\n");

    for (var i = 0; i < lines.length; i++) {

      var words = lines[i].split(' ');
      var line = '';

      for (var n = 0; n < words.length; n++) {
        var testLine = line + words[n] + ' ';
        var metrics = this.measureText(testLine);
        var testWidth = metrics.width;
        if (testWidth > maxWidth && n > 0) {
          this.strokeText(line, x, y);
          line = words[n] + ' ';
          y += lineHeight;
        }
        else {
          line = testLine;
        }
      }

      this.strokeText(line, x, y);
      y += lineHeight;
    }
  }

export default {
  name: 'Profile',
  components: {},
  data: () => ({
    name: "",

  //#region Card Type
    cardtype: '',
    card_types: [
        'Creature', 'Construct', 'Spell', 'Immortal', 'Construct Creature' 
      ],
    creature_enabled: false,
  //#endregion
  //#region AffinityList
    affinityselect: null,
    AffinityList: ['fire', 'water', 'nature', 'air', 'dark', 'light'],
  //#endregion
  //#region AffinityCost
  //#endregion 
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
      ],
    loading: false,
    subtypes: '',
    subtype_selected: [], 
    cost_light: 0,
    cost_dark: 0,
    cost_fire: 0,
    cost_water: 0,
    cost_nature: 0,
    cost_air: 0,
    cost_null: 0,
  value: "",
  rules: [],
  //#region Textboxes
  textbox: "",
  textbox_value: "",
  textbox_rules: [],
  flavor_text: "",
  flavor_text_value: "",
  flavor_text_rules: [],
  //#region Card Preview variables 
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
    text: '',
    textMaxWidth: 250,
    textStrokeStyle: '#000000',
    textFillStyle: '#FFFFFF',
    textLineWidth: 2,
    textPosition: {
      x: 20,
      y: 60
    },
    textFont: '48px "Impact", sans-serif',
    textLineHeight: 60,
    
  //#end region
  //#region Other
    selectErrors: [],
    Force: "",
    Vitality: "",
  //#endregion
  


  }),
mounted() 
    {
    this.checkPlayerProfile(this.user)
    //this.setImage(this.framePreset)
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
  async increment(cost) {
      this.cost_fire = parseInt(this.cost_fire, 10) + 1
    },

  async decrement(cost) {
    this.cost_fire = parseInt(this.cost_fire, 10) - 1
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
    },

  
//#region Canvas methods
    onFileChange() {
      //var files = event.target.files || event.dataTransfer.files;

      //if (!selectedImage.length)
        //return;

      //this.createImage(files[0]);
      //console.log(files[0])
      console.log(this.selectedImage.name)
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
      

    onTextChange: function(event) {
      this.repaint();
      },
    onCardFrameChkbxChange() {
      this.setCardFrameToCanvas();

      },
    onSizeChange: function(event) {
      //Get percentage of width and height
      this.cardImageWidth = mathService.GetPercentage(this.imageWidth, this.cardImageAspectPercentage)
      this.cardImageHeight = mathService.GetPercentage(this.imageHeight, this.cardImageAspectPercentage)
      this.repaint();
      },
    createImage: function(file) { 
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

    setImage: function(url) {

      this.image = url;

      this.paint();

      },

    setImageToCanvas: function(url, callback, callback2) {

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
    setImageToCanvasFirst: function(url, callback, callback2) {

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
    setCardFrameToCanvas: function() {
      if(this.cardFrameCheckbox == true) {
          var vm = this;
          var ctx = this.getContext();
          var background = new Image();
          background.src = vm.presets[0]
          ctx.drawImage(background, 0, 0, vm.width, vm.height);
        }
      },
    setTextToCanvas: function(text) {

        var context = this.getContext();
        context.font = this.textFont;
        context.fillStyle = this.textFillStyle;
        context.wrapFillText(text, this.textPosition.x, this.textPosition.y, this.textMaxWidth, this.textLineHeight);
        context.strokeStyle = this.textStrokeStyle;
        context.lineWidth = this.textLineWidth;
        context.wrapStrokeText(text, this.textPosition.x, this.textPosition.y, this.textMaxWidth, this.textLineHeight);

      },

    getContext: function() {

      return document.getElementById(this.canvasElementId).getContext("2d");

      },
    paint: function() {

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
    
    repaint: function() {

        var vm = this;

        if ( this.image == '' )
          this.setTextToCanvas(this.text);

        this.getContext().clearRect(0, 0, this.width, this.height);
        this.setImageToCanvas(this.image, function(){
        vm.setCardFrameToCanvas(); }, function() {
            vm.setTextToCanvas(vm.text);
      });
        
      },

    reset: function (event) {
        this.image = '';
        this.imageWidth = 0;
        this.imageHeight = 0;
        this.selectedImage = null;
        this.text = '';
        this.width = 375;
        this.height = 523;
        this.cardImageHeight = 0;
        this.cardImageWidth = 0;
        this.cardImageAspectPercentage = 100;
        this.textStrokeStyle = '#000000';
        this.textFillStyle = '#FFFFFF';
        this.repaint();
        this.getContext().clearRect(0, 0, this.width, this.height);
      },
    info: function (event) {
      var dt = document.getElementById(this.canvasElementId).toDataURL('image/png');
      console.log("current image" + dt)
      },
    download: function(event) {

        var dt = document.getElementById(this.canvasElementId).toDataURL('image/png');

        /* Change MIME type to trick the browser to download the file instead of displaying it */
        dt = dt.replace(/^data:image\/[^;]*/, 'data:application/octet-stream');

        /* In addition to <a>'s "download" attribute, you can define HTTP-style headers */
        dt = dt.replace(/^data:application\/octet-stream/, 'data:application/octet-stream;headers=Content-Disposition%3A%20attachment%3B%20filename=Meme.png');

        document.getElementById('download').href = dt;
      },
},
  
watch: {
  cardtype(cardtype) {
    switch(cardtype) {
      case ('Creature'):
        this.creature_enabled = true
        break;
      case ('Construct Creature'):
        this.creature_enabled = true
        break;
      default:
        this.creature_enabled = false
        break;
      }
    },

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
      }

      return subtype_selections
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

.title {
  margin-bottom: 7em !important;
}


a {
  color: #fff !important;
  text-decoration: none;
}

.v-list {
  height: 200px;
  overflow-y: scroll;
}

.preset img {
  width: 100%;
  height: auto;
}

#canvas {
  
  background-color: rgba(160, 160, 160, 0.685);
}

</style>
