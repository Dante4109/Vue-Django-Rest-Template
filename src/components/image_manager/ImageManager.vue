<!-- Image Manager --> 
<template>
  <v-main>
    <v-layout row justify-center>
    <v-dialog
      class="imageManager"
      v-model="showImageManager"
      scrollable
      max-width="1000"
      max-height="800"
      >
      <v-card
      >
        <v-card-title class="headline">Select File</v-card-title>
        <v-divider></v-divider>
        <v-card-text>
        <v-row>
        <v-col class="text-left">
          <v-icon 
          v-if="imageManagerSelectedItems.length >= 1"
          @click="onClickDelImageManager()"
          size="30px"
          >
          mdi-delete
          </v-icon>
        </v-col>
        <v-col class="text-right" cols="12">
          
          
          <v-btn
          @click="goBackCurrentImageDir()"
          >
            Back
          </v-btn>
          
          <v-btn
          @click="addFolderImageManager()"
          >
            + Folder
          </v-btn>

            <v-btn
            v-if="!imageManagerSelect"
            @click="imageManagerSelect=true"
            >
              Select
            </v-btn>

          
          
          <v-btn 
          v-else
          @click="imageManagerSelect=false, imageManagerSelectedItems=[]"

          >
            Cancel
          </v-btn>

          <v-btn 
          v-if="activeImageItem"
          @click.stop="imageRenameDialog = true"
          >
          Rename
          </v-btn>
          <v-dialog
            v-model="imageRenameDialog"
            max-width="290"
              >
            <v-card 
            v-if="activeImageItem">
              <v-card-title class="headline">Enter Name</v-card-title>
      
              <v-col cols="12">
                <v-text-field v-model="activeImageItem.Name"
                @keyup="onRenameObject"
                > 
                
                </v-text-field>
              </v-col>
      
              <v-card-actions> 
                <div class="text-center">
                  <div class="my-2">
                <v-btn
                  color="green darken-1"
                  text
                  @click="imageRenameDialog = false"
                >
                  OK
                </v-btn>
                  </div>
                </div>
              </v-card-actions>
            </v-card>
          </v-dialog>

          <v-btn
          v-if="!imageManagerSelect"
          >
            <v-file-input
            v-model="uploadedImage"
            @change="onImageUpload(uploadedImage)"
            accept="image/*"
            hide-input="true"           
            prepend-icon="mdi-camera"
            loading
              >
              </v-file-input>
          </v-btn>

        </v-col>
        </v-row>

        <v-col cols="12">
          <p>{{ imageManagerSelectedItems.Name }}</p>
          <v-label
          left
          >
            Bread crumbs go here
          </v-label>
        </v-col>
        </v-card-text>
          <v-card-text style="height: 300px;">
            <v-row>
              
              <!-- Folders -->
                <v-col cols="12">
                  <v-row>
                    <v-hover
                    v-slot:default="{ hover }" 
                    v-for="(Item) in imageManagerItems"
                    :key="Item.FolderId"
                    >
                      <v-col 
                      v-if="!Item.file"
                      tile
                      md="2"
                      >

                      <v-checkbox
                      v-if="imageManagerSelect" 
                      v-model="imageManagerSelectedItems" 
                      v-bind:value="Item"
                      >
                      </v-checkbox>
                      <v-card 
                      :elevation="hover ? 16 : 2"
                      @click="activeImageItem=Item"
                      >
                      <v-icon
                      size="100px"
                      color="grey darken"
                      @click="changeCurrentImageDir(imageSelectorItems, Item.FolderId)"
                      >
                      mdi-folder
                      
                      </v-icon>
                      <v-expand-transition>
                      <div
                        v-if="hover"
                        class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-3 white--text"
                        style="height: 100%;">
                      </div>
                    </v-expand-transition>
                      <v-col
                      >
                      <span 
                      v-on:dblclick="getCurrentImageItem(Item)"
                      center>{{ Item.Name }}</span>
                      </v-col>
                      </v-card>
                      </v-col>
                <!-- End folders -->

              <v-col 
              v-else
              tile
              md="2"
              >

              <v-checkbox 
              v-if="imageManagerSelect" 
              v-model="imageManagerSelectedItems" 
              v-bind:value="Item"
              >
              </v-checkbox>

              <v-card 
              :elevation="hover ? 16 : 2"
              @click="activeImageItem=Item"
              >
              <v-img 
              :src= Item.url 
              aspect-ratio="1.0" 
              contain class="image"
              size="100px"
              />
              <v-expand-transition>
              <div
                v-if="hover"
                class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-3 white--text"
                style="height: 100%;">
              </div>
            </v-expand-transition>
                <v-col
                >
                <span 
                center>{{ Item.Name }}</span>
                </v-col>
                </v-card>
              </v-col>
              </v-hover>
              </v-row>
              </v-col>
              <!-- End Files -->
            
            </v-row>
          </v-card-text>
            <v-divider></v-divider>
        <v-card-actions>
          <v-col class="text-right" cole="12"> 
          <div class="text-right">
            <div class="my-2">
          <v-btn
            color="green darken-1"
            text
            @click="imageManagerSelect=false, imageManagerSelectedItems=[], showImageManager = false, updateCurrentImage()"
          >
            OK
          </v-btn>
          <v-btn
            right
            color="red darken-1"
            text
            @click="imageManagerSelect=false, imageManagerSelectedItems=[], showImageManager = false"
          >
            Cancel
          </v-btn>
            </div>
          </div>
          </v-col>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
  </v-main>
</template>

<script>
// Components
import FileInput from '@/components/image_manager/FileInput.vue';

// Services
import userService from '@/services/userService';
import imageService from '@/services/imageService';

// Business Logic
import tree_item_logic from '@/utilities/tree_item_logic';

export default {
  name: "ImageManager",
  components: {
    FileInput
  },
  data: () => ({
  // #region User Properties

  // endregion
  // #region Image Manager Properties
    activeImageItem: [],
    imageRenameDialog: false,
    showImageManager: false,
    imageFolderIdList: [],
    maxImageFolderId: 0,
    imageManagerSelectedItems: [],
    imageSelectorFiles: {
      html: 'mdi-language-html5',
      js: 'mdi-nodejs',
      json: 'mdi-json',
      md: 'mdi-markdown',
      pdf: 'mdi-file-pdf',
      png: 'mdi-file-image',
      txt: 'mdi-file-document-outline',
      xls: 'mdi-file-excel',
      crd: 'mdi-file-image',
    },
    imageSelectorItems: [
      {
        Name: 'Root',
        ParentId: null,
        FolderId: 1,
        Children: []
      },
    ],
    selectedItems: [],
    selectedFiles: [],
    imageManagerSelect: false,
    imageManagerFiles: [],
    imageManagerDirs: [],
    imageManagerItems: [],
    currentImageFolder: [],
    previousImageFolder: [],
    uploadedImage: null,
    // #endregion
  }),
  mounted() {
    this.checkProfile(this.user)
  },
  // #region All Methods
    methods: {
    // #region Dialog Methods
      next() {
      this.loading = true

      setTimeout(() => {
        this.subtypes = ''
        this.subtype_selected = []
        this.loading = false
      }, 2000)
      },
      closeDialog(){
      this.dialog = false
      },
      openDialog() {
        this.dialog = true;

      if(data.next) {
        this.next = data.next
      }
      },
    // #endregion Dialog Methods
    // #region Profile Methods
    async getProfile(payload) {
              // TO-DO This should eventually be part of layout not the manager itself.          
              const profile = await userService.fetchProfile(payload)
              this.profile = profile
              this.first = this.profile.first_name
              this.last = this.profile.last_name
              this.username = this.profile.username
              this.date = this.profile.age
              this.pronouns = this.profile.pronouns
              this.region = this.profile.region
              this.records = this.profile.records
              this.facts = this.profile.facts
              this.email = this.user.email
              this.ImgUrl = this.profile.ImgUrl

              /* //Check if Profile has any cards in collection
              if(!this.profile.card_collection.length < 1 || this.profile.card_collection == undefined) 
                { this.cardSelectorItems = this.profile.card_collection
                } */
              //Check if Profile has uploaded any images
              if(!this.profile.image_collection.length < 1 || this.profile.image_collection == undefined) 
                { this.imageSelectorItems = this.profile.image_collection
                  this.changeCurrentImageDir(this.imageSelectorItems, 1);
                }
              this.maxImageFolderId = (Math.max(...this.getFolderIdList(this.imageSelectorItems, [])))
              // this.maxCardFolderId = this.getTreeItemsList(this.cardSelectorItems)
              //this.imageManagerTest()
        },
    async newProfile(user_id) {
        let id = {  
          "id": user_id
        }
        let payload = {
          "user": id
        }
        // console.log(payload)
        await userService.createProfile(payload)
        this.refreshUser()
        this.checkProfile(user)
      },
    async checkProfile(user) {
          if(user.profile_id != null) {
          this.profile = await this.getProfile(user.profile_id)
          this.profile_id = user.profile_id
          // this.updateCardCollection()
          this.updateImageCollection()
        }
          else {
          this.newProfile(this.user.id)
        }
      },
    // #endregion profile methods
    // #region File Tree Methods
    // TO-DO Separate logic to tree item logic js file. 
    findTreeItem(items, id) {
      if (!items) {
        return;
      }
      for (var i = 0; i < items.length; i++) {
        var item = items[i];
        // Test current object
        if (item.FolderId === id) {
          return item;
        }
        // Test children recursively
        const child = this.findTreeItem(item.Children, id);
        if (child) {
          return child;
        }
      }
    },
    getFolderIdList(items, folderIdList) {
      if (items.length > 0) {

        for (var i = 0; i < items.length; i++) {
          var item = items[i];
          // Test current object
          //console.log("Name: " + item.Name + " Folder: " + item.FolderId)
          folderIdList.push(item.FolderId)
          // Test children recursively
          // Only run if item has as folderId
          if (item.folderId) {
            const child = this.getFolderIdList(item.Children, folderIdList);
          }
        }
      }

      return folderIdList
    },  
    getTreeItemsList(items) {
        if (!items) {
            // Do nothing
            return;
        }
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            // Test current object
              //console.log("Name: " + item.Name + " Folder: " + item.FolderId)
              // this.imageFolderIdList.push(item.FolderId)
            // Test children recursively
            const child = this.getTreeItemsList(item.Children);
        }
        return (Math.max(...this.imageFolderIdList))
      },
    async delActiveTreeObject(itemSelected) {
          var self = this;   
          var fromParent = itemSelected.ParentId ? self.findTreeItem(self.cardSelectorItems, itemSelected.ParentId) : null;
          var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;

          if(itemSelected && itemSelected.Children && itemSelected.FolderId != 1) 
          {
              //Delete all items in the folder. Cards and folders. 
              this.delFolder(itemSelected, objFrom)        
          }
          else if (itemSelected && itemSelected.FolderId != 1) 
          {
              //Delete card or other object
              this.delObject(itemSelected, objFrom)
          }
          else
          {
          
          }
      },
    async delFolder(itemSelected, objFrom) {
        if(itemSelected.Children[0])
        {
          //Confirm if you want to delete all items in the folder. 
          //insert if condition
          //Recurssively delete all children items first. 
          var items = itemSelected.Children
          for (var i = 0; i < items.length; i++) {
            var item = items[i];
            this.delActiveTreeObject(item)
          }
        }
        //Delete actual folder
        this.delObject(itemSelected, objFrom)
      },
    async delObject(itemSelected, objFrom) {
        console.log("Deleted: " + itemSelected.Name + " FolderId: " + itemSelected.FolderId)
        objFrom.splice(objFrom.indexOf(itemSelected), 1);
      },
    // #endregion File Tree Methods
    // #region Image Manager Methods
    getCurrentImageItem(item) {
      (item.Children) ?
      console.log("Name: " + item.Name + " FolderID: " + item.FolderId + "Type: Folder") : 
      console.log("Name: " + item.Name + " FolderId: " + item.FolderId + "Type: File");
      },
    alertTest() {
      alert("Rename Test")
      },
    imageManagerTest: function() {
        //console.log("Max folderID: " + Math.max(...this.cardFolderIdList))
        //console.log("Min FolderID: " + Math.min(...this.cardFolderIdList))
        var self = this;
        console.log("Root folder: ")
        this.changeCurrentImageDir(this.imageSelectorItems, 1);
        this.printImageDirectories()
        console.log("Navigate to first folder")
        console.log("Current Folder: " + self.imageManagerDirs[0].Name)
        this.changeCurrentImageDir(this.imageSelectorItems, self.imageManagerDirs[0].FolderId);
        this.printImageDirectories()
        console.log("Previous Image Folder: " + self.previousImageFolder)
        console.log("Simulate going back in the directoy with the back button")
        //this.goBackCurrentImageDir()        
      },
    printImageDirectories() {
      console.log("Image Folders: ")
      console.log(this.imageManagerDirs)
      console.log("Image Files: ")
      console.log(this.imageManagerFiles)
      },
    goBackCurrentImageDir() {
       if(this.currentImageFolder.ParentId) 
        this.changeCurrentImageDir(this.imageSelectorItems, this.currentImageFolder.ParentId)
      },
    changeCurrentImageDir(items, dirId) {
      this.currentImageFolder = this.findTreeItem(items, dirId);
      this.setFolderChildren(this.currentImageFolder.Children)

      // Emitter to other components that rely on this.
      // This should eventually just be global using a store.

      // this.emitter.emit('changeImageDirParent', { items: items, dirId: dirId });
      this.emitter.emit('changeImageDirParent', { imageManagerItems: this.imageManagerItems, currentImageFolder: this.currentImageFolder })

      },
    sortFileItemsList: function(items) {
        if (!items) {
            // Do nothing
            return;
        }
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            // Deterimine current object file or dir? 
              (item.Children) ?
              console.log("Name: " + item.Name + " FolderID: " + item.FolderId + "Type: Folder") : console.log("Name: " + item.Name + " FolderId: " + item.FolderId + "Type: File");
            // Test children recursively
            const child = this.sortFileItemsList(item.Children);
        }
      },
    setFolderChildren: function(items) {
      this.imageManagerItems = []
      if (!items) {
            // Do nothing
            console.log("Nothing was found")
            return;
        }
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            // Deterimine current object file or dir? 
              if (item.Children) {
              console.log("Name: " + item.Name + " Folder Id: " + item.FolderId +  " Type: Folder") 
              this.imageManagerItems.push(item)
              }
              else {
              /* console.log("Name: " + item.Name + " Folder: " + item.FolderId + " Type: File");
              this.imageManagerFiles.push(item) */
            }
        }

        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            // Deterimine current object file or dir? 
              if (item.Children) {
              /* console.log("Name: " + item.Name + " Folder: " + item.FolderId +  " Type: Folder") 
              this.imageManagerDirs.push(item) */
              }
              else {
              console.log("Name: " + item.Name + " Folder Id: " + item.FolderId + " Type: File");
              this.imageManagerItems.push(item)
            }
        }
      },
    addFolderImageManager: function() {
      var self = this;
      self.maxImageFolderId = (Math.max(...this.getFolderIdList(this.imageSelectorItems, [])))
      const newId = self.maxImageFolderId + 1
      var newFolderName = "New Folder"
      var parentId = self.currentImageFolder.FolderId
      var children = []
      var newFolder = {
            FolderId: newId,
            Name: newFolderName,
            ParentId: parentId,
            Children: children,
      }


      // this.imageFolderIdList = this.getFolderIdList(self.imageSelectorItems, [])
      var toParent = self.findTreeItem(self.imageSelectorItems, parentId)
      toParent.Children.push(newFolder)
      self.maxImageFolderId = self.maxImageFolderId + 1
      self.setFolderChildren(self.imageSelectorItems)
      self.changeCurrentImageDir(self.imageSelectorItems, parentId);
      this.updateImageCollection(this.imageSelectorItems)
      },
    addImageFileImageManager: function(imageData) {
       var self = this;
       const newId = self.maxImageFolderId + 1
       var newName = imageData.name
       var imageUrl = imageData.img_url 
       var parentId = self.currentImageFolder.FolderId           
       var children = []
       var newImageFile = {
            FolderId: newId,
            Name: newName,
            file: "img",
            url: imageUrl,
            ParentId: parentId,
       }

       var toParent = self.findTreeItem(self.imageSelectorItems, parentId)
       toParent.Children.push(newImageFile)
       self.maxImageFolderId++
       self.setFolderChildren(self.imageSelectorItems)
       self.changeCurrentImageDir(self.imageSelectorItems, parentId);
       this.updateImageCollection(this.imageSelectorItems)
      },
    async updateCardImage() { 
      //Update S3 Card Image
        var dt = document.getElementById(this.canvasElementId).toDataURL('image/png');
        var blob = fileService.dataURItoBlob(dt);
        var file = fileService.blobToFile(blob, (this.txtName + ".png"))
        const uploadedImage = await this.uploadImage(file)
        return uploadedImage
      },
    async onClickDelImageManagerOld() { 
        var self = this;
        if(self.activeImageItem) {
          this.delActiveImageManagerObject((self.activeImageItem), self.imageSelectorItems)
        }
        else
        {
          //Nothing was chosen or root was selected 
          console.log("No item selected to delete")  
        }
        self.setFolderChildren(self.imageSelectorItems)
        self.changeCurrentImageDir(self.imageSelectorItems, self.activeImageItem.ParentId);
        this.updateImageCollection(this.imageSelectorItems)

      },
    async onClickDelImageManager(items) { 
        var currentItems = this.imageManagerSelectedItems
        var itemCount = currentItems.length
        var selectedItem
        var i = 0;
        for (i = 0; i < itemCount; i++) {
            selectedItem = currentItems[i];
            this.delActiveImageManagerObject((selectedItem), this.imageSelectorItems)
          }
        this.setFolderChildren(this.imageSelectorItems)
        this.changeCurrentImageDir(this.imageSelectorItems, selectedItem.ParentId);
        this.updateImageCollection(this.imageSelectorItems)
        
        for (i = 0; i < itemCount; i++) {
            this.imageManagerSelectedItems.splice(this.imageManagerSelectedItems.indexOf(selectedItem), 1);
          }
      },
    async delActiveImageManagerObject(itemSelected, selectorItems) {
          var self = this;
          var fromParent = itemSelected.ParentId ? self.findTreeItem(selectorItems, itemSelected.ParentId) : null;
          var objFrom = fromParent ? fromParent.Children : selectorItems;

          if(itemSelected && itemSelected.Children && itemSelected.FolderId != 1)
          {
              //Delete all items in the folder. Cards and folders.
              this.delFolder(itemSelected, objFrom)
          }
          else if (itemSelected && itemSelected.FolderId != 1)
          {
              //Delete card or other object
              this.delObject(itemSelected, objFrom)
          }
          else
          {
          
          }
        },
    async updateImageCollection() {
        this.maxImageFolderId = this.getTreeItemsList(this.imageSelectorItems)
        let payload = {
          "image_collection": this.imageSelectorItems,
        }
        if(this.imageSelectorItems[0].Children)
        await userService.updateProfile(this.user.profile_id, payload)
      },
      async updateCurrentImage() {
        //Get active image item
        /* if(this.active[0].file === "crd" && this.activeImageItem.file === "img")
        {
        console.log("It worked")
        this.drawImageFrmBlob(this.activeImageItem.url)
        this.imgUrl = this.activeImageItem.url
        }
        else
        {
          console.log("It didn't work")
        } */
        this.emitter.emit('updateCurrentImageParent', { activeImage: this.activeImageItem } )
      
      },
    async uploadImage(imageFile) {
      // Create bodyFormData
        var bodyFormData = new FormData();
        bodyFormData.append('img_url', imageFile);
        bodyFormData.append('profile_id', this.user.profile_id);
        bodyFormData.append('name', imageFile.name);
        bodyFormData.append('filetype', imageFile.type);
        bodyFormData.append('size', imageFile.size);
    
      // Call Image Service
        const uploadedImage = await imageService.postImage(bodyFormData)
        return uploadedImage
      },
    async deleteImage() {
      await cardService.deleteCard(imageId, payload)
      },
    async onImageUpload(imageFile) {
      // Post image to DB
      console.log(imageFile) 
      const uploadedImage = await this.uploadImage(imageFile)
      // Add image file to image_collection
      this.addImageFileImageManager(uploadedImage)
      },
    async onRenameObject(event) {
        console.log("Object was renamed")
        this.updateImageCollection(this.imageSelectorItems)
      },
    // #endregion Image Manager Methods
  },
  // #endregion
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
    created() {
      this.emitter.on('image_manager', data => {
        console.log("Received emitter for image_manager")
        this.showImageManager = true;
    })
  }
  // #endregion Created
}
</script>