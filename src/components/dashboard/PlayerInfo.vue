<template>
    <V-container >
        <v-col cols="12">
            <h1>Player Info</h1>
        </v-col>
    <v-row>

        
        
        <v-col :cols="cols">
        <div>
            <v-file-input
                v-model="selectedImage"
                accept="image/*" 
                @change="onImageSelected"
                label="Upload Photo"
                filled
                prepend-icon="mdi-camera"
            ></v-file-input>
        </div>
        </v-col>
        <v-col :cols="cols">
        <div>
            <v-btn large
                label="Submit"
                raised
                outlined
                color="white"
                @click="onUpload()" 
                style="center"
                >Submit
            </v-btn>
        </div>
        </v-col>
        
        </v-row>
        <v-row>
        <v-col :cols="cols">
        



        <div v-if="player.ImgUrl">
            <v-img :src="playerImage" aspect-ratio="1.0" contain class="image" />
        </div>
            
        <div v-if="!(player.ImgUrl)"> 
            <h2>Player image not found</h2>
        </div>
        
        

        </v-col>
        <v-col :cols="cols">
            <div v-if="player">
                <h2>username: {{ player.username }} </h2>
                <h2>Name: {{ player.first_name + " " +  player.last_name }} </h2>
                <h2>Date of Birth: {{ player.age }} </h2>
                <h2>Pronouns: {{ player.pronouns }} </h2>
                <h2>Home Region: {{ player.region }} </h2>
                <h2>Games: {{ player.games }} </h2>
                <h2>Personal Best Record: {{ player.records }} </h2>
                <h2>Fun Facts: {{ player.facts }} </h2>
            </div>

            <div v-if="!player">
                <h2>Player not found</h2>
            </div>
        </v-col>
        </v-row>
    </V-container>   
</template>

<script>
import userService from '@/services/userService'
import fileService from '@/services/fileService'

export default {
            
props: [],         
data: () => ({
        player: [],
        playerImage: null,
        selectedImage: null
        //playerImage: ("http://127.0.0.1:8000/static/playerimages/Maria.jpg"),
    }),
   
mounted() {
        this.players = this.getPlayer(this.user.player_profile_id);
    },

methods: {
    async getPlayer(playerKey) {
        //let assetsPath = require.context('./assets/PlayerImages/', false, /\.(png|jpe?g|svg)$/);
        const Player = await userService.fetchPlayerProfile(playerKey)
        this.player = Player
        
        //for loading images from assets folder
        //const fileName = Player.ImgUrl.toString();
        //this.playerImage = require(`@/assets/PlayerImages/${fileName}`);

        //for loading images from url
        this.playerImage = Player.ImgUrl
        },
    async onImageSelected() {
        // eslint-disable-next-line no-console
        console.log(this.selectedImage.name)
        },
    async updateProfilePic(data) {
        let payload = {"ImgUrl": data}
        await userService.updatePlayerProfile(this.user.player_profile_id, payload)
            .then (res => {
                if (res.status == 200) {
                    this.getPlayer(this.user.player_profile_id)
                      
                }
            })
        },
    async onUpload() {
        await fileService.ImageBlob(this.selectedImage)
            .then (res => {
                this.updateProfilePic(res.data.image)
                    
            })
        },
    },
watch: {},
computed: {
    cols() {
      const {
        mdAndUp,
        mdAndDown
      } = this.$vuetify.breakpoint
      return mdAndUp ? 6 : mdAndDown ? 12 : 12
    },
user: {
        get() {
        return JSON.parse(this.$store.state.authenticatedUser)
        }
    },
  },
};
    
</script>

<style scoped>
h1 {
color: rgb(255, 255, 255)
}

.full
{
height: 892px;
width: 990px;
Color: red;


}
</style>