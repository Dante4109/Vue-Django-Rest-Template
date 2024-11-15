<template>
  <div style="padding:2em;">
    <v-container>
      <v-layout column class="white--text">
        <v-row>
          <v-col cols="12">
            <!-- Login or User profile icon -->
              <div>
                  <v-row>
                    
                    <v-btn @click="openImageManager">
                    Upload photos and change the folder      
                        </v-btn>
                    </v-row>
                  </div>
              <ImageManager />
              <PhotoGallery />
          </v-col>
        </v-row>
      </v-layout>
    </v-container>
  </div>
</template>

<script>

import PhotoGallery from '@/components/gallery/PhotoGallery.vue';
import ImageManager from '@/components/image_manager/ImageManager.vue';

export default {
  name: "Image Manager",
  methods: {
    openImageManager() {      
      console.log("Clicked open manager")
      this.emitter.emit('image_manager');
    }
  },
};
</script>