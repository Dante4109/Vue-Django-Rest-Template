<template>
  <v-container>    
    <h2 class="text-h4 mb-6">Current Folder: {{currentImageFolder.Name}}</h2>
    <v-col cols="12">
      <v-row>
        <v-hover v-slot="{ isHovering, props }"
        v-for="(Item, index) in photoManagerItems"
        :key="Item.FolderId"
        >
        <v-col
        v-if="Item.file"
        cols="12"
        sm="6"
        md="4"
        lg="3"
        >
          <v-card
            v-bind="props"
            @click="openLightbox(index)"
            :elevation="isHovering ? 16 : 2"
            :class="{ 'on-hover': isHovering }"
            class="transition-fast-in-fast-out"
          >
            <v-img              
              :src="Item.url"
              :alt="Item.name"
              aspect-ratio="1.0"
              size="100px"
              class="align-end"
            >
              <v-card-title class="text-white bg-black bg-opacity-50">
                {{ Item.Name }}
              </v-card-title>
            </v-img>
          </v-card>
        </v-col>
      </v-hover>
    </v-row>
  </v-col>

    <v-dialog v-model="lightbox" fullscreen transition="dialog-bottom-transition">
      <v-card>
        <v-toolbar dark color="primary">
          <v-toolbar-title>{{ photoManagerItems[currentIndex].Name }}</v-toolbar-title>
          <v-btn icon dark @click="prevPhoto" :disabled="currentIndex === 0">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-btn icon dark @click="nextPhoto" :disabled="currentIndex === photoManagerItems.length - 1">
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn icon dark @click="lightbox = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-img
          :src="photoManagerItems[currentIndex].url"
          :alt="photoManagerItems[currentIndex].Name"
          max-height="calc(100vh - 64px)"
          contain
          class="bg-grey-darken-4"
        ></v-img>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>

export default {
  data() {
    return {
      lightbox: false,
      currentIndex: 0,
      photoManagerItems: [],
      currentImageFolder: ""
    }
  },
  methods: {
    // #region Gallery Methods
    openLightbox(index) {
      this.currentIndex = index
      this.lightbox = true
    },
    nextPhoto() {
      if (this.currentIndex < this.photoManagerItems.length - 1) {
        this.currentIndex++
      }
    },
    prevPhoto() {
      if (this.currentIndex > 0) {
        this.currentIndex--
      }
    },
    // #endregion
  },
  // #region Computed
  computed: {
    user: {
      get() {
        return JSON.parse(this.$store.state.authenticatedUser)
      }
    },
  },
  // #endregion Computed
  // #region Created
  created (){
    // Updates the current photo directory from the image manager
    this.emitter.on('changeImageDirParent', (data) => {
      this.photoManagerItems = data.imageManagerItems
      this.currentImageFolder = data.currentImageFolder
    })
  }
  // #endregion
}
  
</script>

<style scoped>
.v-card.on-hover {
  transform: scale(1.05);
}
</style>