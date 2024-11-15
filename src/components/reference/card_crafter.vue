 <template>
 <v-main>
  <v-container fluid>
    <v-row align="center">
      
    <v-col cols="12">
      <div 
      align="center"
      class="title"
      >
        <h1>Card Crafter
        <v-icon color="white">mdi-tools</v-icon>
        </h1>
        
      </div>
    </v-col>
  
  </v-row>
<!-- Card Info -->  
  <!-- Buttons -->
        <v-col :cols="0">
        <v-row justify="center"
          >
          <v-btn
          @click.stop="dialogCardId = true"
          >
              Load Card 
            </v-btn>
          <!-- Pop Up -->
            <v-dialog
                    v-model="dialogCardId"
                    max-width="290"
                      >
                    <v-card>
                      <v-card-title class="headline">Enter Card Id</v-card-title>
              
                      <v-col cols="12">
                        <v-text-field v-model="cardId"></v-text-field>
                      </v-col>
              
                      <v-card-actions> 
                        <div class="text-center">
                          <div class="my-2">
                        <v-btn
                          color="green darken-1"
                          text
                          @click="dialogCardId = false"
                        >
                          OK
                        </v-btn>
                          </div>
                        </div>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
          
          <v-btn @click="publishCard">
              Publish Card 
            </v-btn>
          <v-btn @click="deleteCard">
              Delete Card
            </v-btn>
          <v-btn @click="saveCard">
              Save Card
            </v-btn>
          <v-btn @click="downloadCardData">
              Download Card Data
            </v-btn>
          <v-btn download="Card.png" @click="downloadCardImage" id="downloadCardImage" href="#">
            Download Card Image
            </v-btn>
          <v-btn @click="reset">
            Reset
            </v-btn>
          <v-btn @click="info">
            Info
            </v-btn>
          <v-btn @click.stop="showImageManager = true"
            >
            Upload Image
            </v-btn> 
        </v-row>
        </v-col>

  <!-- Card Info Tabs -->
    <v-col :cols="0">
    <v-layout>
      <v-form
        ref="form"
        style="width:100%;"
      >
    <v-tabs 
      background-color="primary"
      centered
      slider-color="white"

      >
  <!-- Card GUID -->
    <v-tab>ID</v-tab>
      <v-tab-item>    
      <div v-if="active[0]">
      <v-text-field
        v-model="active[0].GUID"
        disabled
        solo-inverted
        color="white"
        label="Card ID"
        >
      </v-text-field>
      </div>
      <div v-else-if="!active[0]">
      <v-text-field
        v-model="noCardSelectedMsg"
        disabled
        solo-inverted
        color="white"
        label="Card ID"
        >
      </v-text-field>
      </div>
    </v-tab-item>
  <!-- Card Name -->
    <v-tab>Name</v-tab>
      <v-tab-item>    
      <v-text-field
        v-model="txtName"
        solo-inverted
        color="white"
        label="Name"
        @keyup="onTextChange"
        >
      </v-text-field>
    </v-tab-item>
  <!-- Affinity List -->
    <v-tab>Affinities</v-tab>
      <v-tab-item>
    <v-col cols="12">
      <v-row>
        <v-text-field 
              v-model="txtLightCost" 
              type="text" 
              label="Light"> 
        </v-text-field>
        
        <v-text-field 
              v-model="txtDarkCost" 
              type="text" 
              label="Dark"> 
        </v-text-field>

        <v-text-field 
              v-model="txtFireCost" 
              type="text" 
              label="Fire"> 
        </v-text-field>
        
        <v-text-field 
              v-model="txtWaterCost" 
              type="text" 
              label="Water"> 
        </v-text-field>

        <v-text-field 
              v-model="txtNatureCost" 
              type="text" 
              label="Nature"> 
        </v-text-field>

        <v-text-field 
              v-model="txtAirCost" 
              type="text" 
              label="Air"> 
        </v-text-field>

        <v-text-field 
              v-model="txtBasicCost" 
              type="text" 
              label="Basic"> 
        </v-text-field>

        <v-text-field 
              v-model="txtTotalCost" 
              type="number" 
              label="Total"
              disabled=""
              > 
        </v-text-field>
      </v-row>
    </v-col>
    </v-tab-item>
  <!-- Types -->
    <v-tab>Types</v-tab>
      <v-tab-item>
      <div>
        <v-container fluid>
          <v-row align="center">
            <v-col cols="6">
              <v-subheader>Card Type</v-subheader>
            </v-col>
            <v-col cols="6">
              <v-select
                v-model="cardtype"
                :items="card_types"
                menu-props="auto"
                hide-details
                label="Select Type"
                single-line
              ></v-select>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </v-tab-item>
  <!-- Subtypes -->
    <v-tab>Sub-Types</v-tab>
      <v-tab-item>
      <v-container fluid>

        <v-combobox
        v-model="subtype_selected"
        :filter="filter"
        :hide-no-data="!search"
        :items="subtype_items"
        :search-input.sync="search"
        hide-selected
        label="Search for an option"
        multiple
        solo
      >
        <template v-slot:no-data>
          <v-list-item>
            <span class="subheading">Press Enter to Create</span>
            <v-chip
              class="ma-2"
              :color="`${colors[nonce - 1]} lighten-3`"
              large
            >
              {{ search }}
            </v-chip>
          </v-list-item>
        </template>
        <template v-slot:selection="{ attrs, item, parent, selected }">
          <v-chip
            v-if="item === Object(item)"
            v-bind="attrs"
            :color="`${item.color} lighten-3`"
            :input-value="selected"
            large
          >
            <span class="pr-2">
              {{ item.text }}
            </span>
            <v-icon
              small
              @click="parent.selectItem(item)"
            >
              $delete
            </v-icon>
          </v-chip>
        </template>
        <template v-slot:item="{ index, item }">
          <v-text-field
            v-if="editing === item"
            v-model="editing.text"
            autofocus
            flat
            background-color="transparent"
            hide-details
            solo
            @keyup.enter="edit(index, item)"
          ></v-text-field>
          <v-chip
            v-else
            :color="`${item.color} lighten-3`"
            dark
            large
          >
            {{ item.text }}
          </v-chip>
          <v-spacer></v-spacer>
          <v-list-item-action @click.stop>
            <v-btn
              icon
              @click.stop.prevent="edit(index, item)"
            >
              <v-icon>{{ editing !== item ? 'mdi-pencil' : 'mdi-check' }}</v-icon>
            </v-btn>
          </v-list-item-action>
        </template>
      </v-combobox>
        </v-container>
    </v-tab-item>
  <!-- Set Name -->
    <v-tab>Set Name</v-tab>
      <v-tab-item>    
      <v-text-field
        v-model="txtSetname"
        solo-inverted
        color="white"
        label="Set Name"
        @keyup="onTextChange"
        >
      </v-text-field>
    </v-tab-item>
  <!-- Main Text Box -->
    <v-tab>Main Text</v-tab>
      <v-tab-item>
    <div>
      <v-container fluid>
        <v-textarea
          v-model="txtMain"
          clearable
          clear-icon="cancel"
          counter
          @keyup="onTextChange"
          label="Main Text"
         >
        </v-textarea>
      </v-container>
    </div>
    </v-tab-item>
  <!-- Full Text Box -->
    <v-tab>Full Text</v-tab>
      <v-tab-item>
    <div>
      <v-container fluid>
        <v-textarea
          v-model="txtFull"
          clearable
          clear-icon="cancel"
          counter
          @keyup="onTextChange"
          label="Full Text"
         >
        </v-textarea>
      </v-container>
    </div>
    </v-tab-item>
  <!-- Flavor Text -->     
    <v-tab>Flavor Text</v-tab>
      <v-tab-item>
    <div>
      <v-container fluid>
        <v-textarea
          v-model="txtFlavor"
          clearable
          clear-icon="cancel"
          counter
          @keyup="onTextChange"
          label="Flavor Text"
          :rules="flavor_text_rules"
        >
        </v-textarea>
      </v-container>
    </div>
   </v-tab-item> 
  <!-- Bottom Text -->     
    <v-tab>Bottom Text</v-tab>
      <v-tab-item>
    <div>
      <v-container>
        <v-text-field
          v-model="txtBottom"
          solo-inverted
          clearable
          clear-icon="cancel"
          @keyup="onTextChange"
          label="Bottom Text"
        >
        </v-text-field>
      </v-container>
    </div>
    </v-tab-item>
  <!-- Serial Number -->
  <!-- Force/Vitality --> 
    <v-tab>For/Vit</v-tab>
      <v-tab-item>
    <div v-if="creature_enabled === true">
        <v-container fluid>
          <v-text-field 
                v-model="txtForce" 
                type="text" 
                label="Force"> 
          </v-text-field>

          <v-text-field 
                v-model="txtVitality" 
                type="text" 
                label="Vitality"> 
          </v-text-field>
      </v-container>
    </div>
    </v-tab-item>

  <!-- Immortal Abilities -->

    </v-tabs>
  
  <!-- End Form -->
          </v-form>
      </v-layout>
      </v-col>
<!-- Card Preview -->  
  <!-- Title -->
      <v-row justify="center"> 
        <v-card color="primary" class="pa-4"> 
        <v-col cols="12">
          <div>
            <v-flex>
            <h1>Card Preview</h1>
            </v-flex>
          </div>

  
  <!-- Cavas Settinngs -->
    
    <!-- Canvas Display -->
          <canvas id="canvas" v-bind:width="canvasWidth" v-bind:height="canvasHeight"></canvas>
    <!--  Settings -->
        <div class="row">
          <div class="col-sm-12">

        <v-checkbox
          :label="`Card Frame: ${cardFrameCheckbox.toString()}`"
          v-model="cardFrameCheckbox"
        ></v-checkbox>      
          
        <!-- Image Manager --> 
          <v-layout row justify-center>
            <v-dialog
                    v-model="showImageManager"
                    scrollable
                    max-width="728"
                    max-height="332"
                    
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
                        @click="goBackCurrentImageDir"
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
                          @click="imageManagerSelect=false, imageManagerSelectedItems=[], showImageManager = false, updateCurrentCardImage()"
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

          <!-- Input Options -->
            <div class="form-group">
                <v-file-input
                  v-model="selectedImage"
                  accept="image/*" 
                  @change="onImageChange"
                  label="Upload Custom Image"
                  filled
                  prepend-icon="mdi-camera"
              ></v-file-input>
              </div>

              <div class="form-group">
                <v-file-input
                  v-model="cardData"
                  accept="json/*" 
                  @change="onCardDataChange"
                  label="Upload Card Data"
                  filled
              ></v-file-input>
              </div>
            </div>
          </div>
          </v-col>
          </v-card>
    <!-- Select -->
      <v-card color="primary" class="pa-4"> 
        <v-col cols="auto">
          <v-flex class="heading">
            <h1>Card Text</h1>
          </v-flex>
            <div>
              <v-select
                v-model="canvasPropertySelected"
                :items="canvasProperties"
                :error-messages="selectErrors"
                label="Canvas Properties"
                required        
                >
              </v-select>
            </div>
    <!-- Canvas Sliders -->      
        <div v-if="canvasPropertySelected === 'Canvas Size'">
          <v-slider label="canvas width" thumb-color="white"  color="blue" v-model="canvasWidth" min="200" max="1000" step="1" @change="onTextChange">
            <template v-slot:append>
                      <v-text-field
                        v-model="canvasWidth"
                        class="mt-0 pt-0"
                        hide-details
                        single-line
                        type="number"
                        style="width: 60px"
                      ></v-text-field>
            </template>
          </v-slider>
          <v-slider label="canvas height" thumb-color="white"  color="blue" v-model="canvasHeight" min="200" max="1000" step="1" @change="onTextChange">
            <template v-slot:append>
                      <v-text-field
                        v-model="canvasHeight"
                        class="mt-0 pt-0"
                        hide-details
                        single-line
                        type="number"
                        style="width: 60px"
                      ></v-text-field>
            </template>
          </v-slider>
        </div>
    <!-- Canvas CardImage Apspect Sliders-->
        <div v-if="canvasPropertySelected === 'Image Size'">
          <v-slider label="image size" thumb-color="white"  color="blue" v-model="cardImageAspectPercentage" min="0" max="200" step="1" @change="onSizeChange">
            <template v-slot:append>
                  <v-text-field
                    v-model="cardImageAspectPercentage"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 60px"
                    @change="onSizeChange"
                  ></v-text-field>
                </template>
          </v-slider>
    <!-- Canvas CardImage H/W Sliders -->
          <v-slider label="image width" thumb-color="white"  color="blue" v-model="cardImageWidth" min="0" max="5000" step="1" @change="onTextChange">
            <template v-slot:append>
                      <v-text-field
                        v-model="cardImageWidth"
                        class="mt-0 pt-0"
                        hide-details
                        single-line
                        type="number"
                        style="width: 60px"
                        @change="onTextChange"
                      ></v-text-field>
            </template>
          </v-slider>

          <v-slider label="image height" thumb-color="white"  color="blue" v-model="cardImageHeight" min="0" max="5000" step="1" @change="onTextChange">
            <template v-slot:append>
                      <v-text-field
                        v-model="cardImageHeight"
                        class="mt-0 pt-0"
                        hide-details
                        single-line
                        type="number"
                        style="width: 60px"
                        @change="onTextChange"
                      ></v-text-field>
            </template>
          </v-slider>
        </div>
    <!-- Canvas CardImage X/Y Sliders -->
        <div v-if="canvasPropertySelected === 'Image Position'">
          <v-slider label="image position horizontal" thumb-color="white"  color="blue" v-model="cardImagePositionX" min="-1000" max="1000" step="1" @change="onTextChange">
            <template v-slot:append>
                      <v-text-field
                        v-model="cardImagePositionX"
                        class="mt-0 pt-0"
                        hide-details
                        single-line
                        type="number"
                        style="width: 60px"
                      ></v-text-field>
            </template>
          </v-slider>
          <v-slider label="image position vertical" thumb-color="white"  color="blue" v-model="cardImagePositionY" min="-1000" max="1000" step="1" @change="onTextChange">
            <template v-slot:append>
                      <v-text-field
                        v-model="cardImagePositionY"
                        class="mt-0 pt-0"
                        hide-details
                        single-line
                        type="number"
                        style="width: 60px"
                      ></v-text-field>
            </template>
          </v-slider>
        </div>   
  <!-- Text Settings -->
    <!-- Text Pos/Size Settings -->
        <!-- Select -->
          <v-col cols="12">
            <div>
              <v-select
                v-model="textPropertySelected"
                :items="textProperties"
                :error-messages="selectErrors"
                label="Text Properties"
                required        
                >
              </v-select>
            </div>
          
        <!-- Text Propeties -->            
                  <div>
                    <v-text-field
                      v-model="arrFont[arrIndex]"
                      color="white"
                      type="text"
                      label="Font"
                      @change="onTextChange"
                      >
                    </v-text-field>

                    <v-text-field
                      v-model="arrMaxWidth[arrIndex]"
                      color="white"
                      label="MaxWidth"
                      @change="onTextChange"
                      >
                    </v-text-field>

                    <v-text-field
                      v-model="arrLineWidth[arrIndex]"
                      color="white"
                      label="LineWidth"
                      @change="onTextChange"
                      >
                    </v-text-field>

                    <v-text-field
                      v-model="arrLineHeight[arrIndex]"
                      color="white"
                      label="LineHeight"
                      @change="onTextChange"
                      >
                    </v-text-field>
                    
                    <v-slider label="Pos X" thumb-color="white"  color="blue" v-model="arrPositionX[arrIndex]" min="-1000" max="1000" step="1" @change="onTextChange">
                      <template v-slot:append>
                            <v-text-field
                              v-model="arrPositionX[arrIndex]"
                              class="mt-0 pt-0"
                              hide-details
                              single-line
                              type="number"
                              style="width: 60px"
                              @change="onTextChange"
                            ></v-text-field>
                          </template>
                      </v-slider>

                      <v-slider label="Pos Y" thumb-color="white"  color="blue" v-model="arrPositionY[arrIndex]" min="-1000" max="1000" step="1" @change="onTextChange">
                      <template v-slot:append>
                            <v-text-field
                              v-model="arrPositionY[arrIndex]"
                              class="mt-0 pt-0"
                              hide-details
                              single-line
                              type="number"
                              style="width: 60px"
                              @change="onTextChange"
                            ></v-text-field>
                          </template>
                      </v-slider>

                  <div class="col-sm-6">
                    <div class="form-group">
                      <label for="textStrokeStyle" class="control-label">
                        Stroke
                      </label>
                      <input type="color" id="textStrokeStyle" v-model="arrStrokeStyle[arrIndex]" @change="onTextChange">
                    </div>

                    <div class="form-group">
                      <label for="textFillStyle" class="control-label">
                        Fill
                      </label>
                      <input type="color" id="textFillStyle" v-model="arrFillStyle[arrIndex]" @change="onTextChange">
                    </div>
                  </div>
                </div>
                </v-col>                           
        <!-- Submit Button -->
            <v-btn
              label="Submit"
              color="white"
              outlined
              @click="submit()" 
              right
              style="margin-left: auto;"
              >Submit</v-btn>
        
      </v-col>
      </v-card>
<!-- Card Selector --->   
      <v-card color="primary" class="pa-4">
          <v-col>
            <v-flex class="heading">
            <h1>Card Selector</h1>
          </v-flex>
          </v-col>
        <v-row>
              <v-col>
                <v-btn @click="onChoiceTest">
                  <span>Info</span>
                  </v-btn>
                <v-btn @click="onClickDel">
                  <span>Delete</span>
                  </v-btn>
                <v-btn @click="addFolder">
                  <span>Add Folder</span>
                  </v-btn>
                <v-btn @click="addCard">
                  <span>Add Card</span>
                  </v-btn>
                <v-btn @click="cloneCard">
                  <span>Clone Card</span>
                  </v-btn>
                <v-btn @click="onClickCopy">
                  <span>Copy</span>
                  </v-btn>
                <v-btn @click.stop="dialogRename = true"
                  v-if="active[0]"  >
                    <span>
                    Rename
                    </span>
                  </v-btn>
                    <v-dialog
                        v-model="dialogRename"
                        max-width="290"
                          >
                        <v-card 
                        v-if="active[0]">
                          <v-card-title class="headline">Enter Name</v-card-title>
                  
                          <v-col cols="12">
                            <v-text-field v-model="active[0].Name"
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
                              @click="dialogRename = false"
                            >
                              OK
                            </v-btn>
                              </div>
                            </div>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
                <v-btn @click.stop="dialogImport = true" > Import
                  </v-btn>
                  <v-dialog
                      v-model="dialogImport"
                      max-width="320"
                        >
                      <v-card >
                        <v-card-title class="headline">Enter Card UUID</v-card-title>
                        <v-checkbox label="MultiCard Import" v-model="multiCardImport"></v-checkbox>
                        <v-col cols="12">
                          <v-text-field 
                            maxlength="36"
                            counter
                            :rules="[rules.required, rules.counter]"
                            v-if="!multiCardImport" 
                            v-model="importUUID"
                          > 
                          </v-text-field>
                          <v-text-field 
                            v-if="multiCardImport"
                            disabled
                            label="Number of cards to import"
                            v-model="importUUIDLineCount">
                          </v-text-field>
                          <v-textarea
                            v-if="multiCardImport"  
                            label ="'Card UUID List"
                            no-resize
                            rows="5"
                            v-model="importUUID">
                          </v-textarea> 
                        </v-col>
                
                        <v-card-actions> 
                          <div class="text-center">
                            <div class="my-2">
                          <v-btn
                            v-if="importUUID"
                            color="green darken-1"
                            text
                            @click="dialogImport = false, importCard(importUUID), importUUID=''"
                          >
                            OK
                          </v-btn>
                          <v-btn
                            color="red darken-1"
                            text
                            @click="dialogImport = false, importUUID=''"
                          >
                            CANCEL
                          </v-btn>
                            </div>
                          </div>
                        </v-card-actions>
                      </v-card>
                    </v-dialog>
                </v-col>
              </v-row>
        
        <v-col cols="auto">
          <v-layout>
                <v-treeview
                class ="cardlistbar"
                :active.sync="active"
                :items="cardSelectorItems"
                @update:active="onTreeSelection"
                item-key="FolderId"
                item-text="Name"
                item-children="Children"
                :open.sync="open"
                activatable
                color="warning"
                dense
                hoverable
                transition
                return-object
                >
                
                <template v-slot:label="{ item, open }">
                  <draggable :list="cardSelectorItems" group="node" :id="item.FolderId" :data-parent="item.ParentId" @start="checkStart" @end="checkEnd">
                      <label>
                          <!-- <v-label> {{ "F" + item.FolderId }}</v-label>
                          <v-label> {{ "P" + item.ParentId }}</v-label> -->
                          <v-icon v-if="!item.file">
                          {{ open ? 'mdi-folder-open' : 'mdi-folder' }}
                        </v-icon>
                        <v-icon v-else>
                          {{ cardSelectorFiles[item.file] }}
                        </v-icon>
                          <i class="fas fa-user mr-3" />
                          <span id="item.FolderId" >{{item.Name}}</span>
                          <v-label v-if="!item.file"> {{ ":&nbsp;&nbsp;" + item.Children.length }}</v-label>
                      </label>  
                  </draggable>
                </template>
              </v-treeview>
          </v-layout>
        </v-col>
      </v-card>
    </v-row>
  </v-container>
 </v-main>  
</template>


<script>
//import axios from 'axios';
import userService from '@/services/userService'
import apiService from '@/services/apiService'
import cardService from '@/services/cardService'
import imageService from '@/services/imageService'
import fileService from '@/services/fileService'
import canvasService from '@/services/canvasService'
import mathService from '@/services/mathService'
import stringService from '@/services/stringService'
import draggable from 'vuedraggable'
import FileInput from '@/components/managers/image_manager/FileInput';
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'

export default {
  name: 'Cardcreator',
  components: {
  draggable,
  FileInput,
  Splitpanes, 
  Pane
  },
  data: () => ({
    dataSnapShot: "",
    name: "",
    player_profile: "",
    cardId: 0,
    cardGUID: "",
    importUUID: "",
    dialogCardId: false,
    cardData: [],
  //#region Card Type
    cardtype: '',
    card_types: [
        'Spell',
        'Destined Spell', 
        'Creature',
        'Destined Creature', 
        'Construct',
        'Destined Construct', 
        'Location',
        'Destined Location',
        'Immortal', 
        'Construct Creature',
        'Destined Construct Creature',      
      ],
    creature_enabled: false,
  // #region AffinityList
    affinityselected: null,
    AffinityList: ['Light', 'Dark', 'Fire', 'Water', 'Nature', 'Air', 'Basic'],
  // #regiopn Subtypes
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
      'txtFull',
      'txtName',
      'txtType', //9
      'txtSubtype', //10
      'txtSetname',
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
      canvasWidth: 375,
      canvasHeight: 523,
      canvasImageWidth: 0,
      canvasImageHeight: 0,
      cardImage: "",
      selectedImage: null,
      cardFrame: '',
      cardImageWidth: 0,
      cardImageHeight: 0,
      cardImagePositionX: 0,
      cardImagePositionY: 0,
      cardFrameCheckbox: false,
      cardImageAspectPercentage: 100,
      cardFramePresets: [
        require('@/assets/CardFrame-Air-Construct Creature.png'),
        require('@/assets/CardFrame-Air-Construct.png'),
        require('@/assets/CardFrame-Air-Creature.png'),
        require('@/assets/CardFrame-Air-Destined Construct Creature.png'),
        require('@/assets/CardFrame-Air-Destined Construct.png'),
        require('@/assets/CardFrame-Air-Destined Creature.png'),
        require('@/assets/CardFrame-Air-Destined Location.png'),
        require('@/assets/CardFrame-Air-Destined Spell.png'),
        require('@/assets/CardFrame-Air-Immortal.png'),
        require('@/assets/CardFrame-Air-Location.png'),
        require('@/assets/CardFrame-Air-Spell.png'),
        require('@/assets/CardFrame-Air.png'),
        require('@/assets/CardFrame-AirCreature.png'),
        require('@/assets/CardFrame-Dark-Construct Creature.png'),
        require('@/assets/CardFrame-Dark-Construct.png'),
        require('@/assets/CardFrame-Dark-Creature.png'),
        require('@/assets/CardFrame-Dark-Destined Construct Creature.png'),
        require('@/assets/CardFrame-Dark-Destined Construct.png'),
        require('@/assets/CardFrame-Dark-Destined Creature.png'),
        require('@/assets/CardFrame-Dark-Destined Location.png'),
        require('@/assets/CardFrame-Dark-Destined Spell.png'),
        require('@/assets/CardFrame-Dark-Immortal.png'),
        require('@/assets/CardFrame-Dark-Location.png'),
        require('@/assets/CardFrame-Dark-Spell.png'),
        require('@/assets/CardFrame-Dark.png'),
        require('@/assets/CardFrame-DarkCreature.png'),
        require('@/assets/CardFrame-Fire-Construct Creature.png'),
        require('@/assets/CardFrame-Fire-Construct.png'),
        require('@/assets/CardFrame-Fire-Creature.png'),
        require('@/assets/CardFrame-Fire-Destined Construct Creature.png'),
        require('@/assets/CardFrame-Fire-Destined Construct.png'),
        require('@/assets/CardFrame-Fire-Destined Creature.png'),
        require('@/assets/CardFrame-Fire-Destined Location.png'),
        require('@/assets/CardFrame-Fire-Destined Spell.png'),
        require('@/assets/CardFrame-Fire-Immortal.png'),
        require('@/assets/CardFrame-Fire-Location.png'),
        require('@/assets/CardFrame-Fire-Spell.png'),
        require('@/assets/CardFrame-Fire.png'),
        require('@/assets/CardFrame-FireCreature.png'),
        require('@/assets/CardFrame-Gold-Construct Creature.png'),
        require('@/assets/CardFrame-Gold-Construct.png'),
        require('@/assets/CardFrame-Gold-Creature.png'),
        require('@/assets/CardFrame-Gold-Destined Construct Creature.png'),
        require('@/assets/CardFrame-Gold-Destined Construct.png'),
        require('@/assets/CardFrame-Gold-Destined Creature.png'),
        require('@/assets/CardFrame-Gold-Destined Location.png'),
        require('@/assets/CardFrame-Gold-Destined Spell.png'),
        require('@/assets/CardFrame-Gold-Immortal.png'),
        require('@/assets/CardFrame-Gold-Location.png'),
        require('@/assets/CardFrame-Gold-Spell.png'),
        require('@/assets/CardFrame-Gold.png'),
        require('@/assets/CardFrame-GoldCreature.png'),
        require('@/assets/CardFrame-Light-Construct Creature.png'),
        require('@/assets/CardFrame-Light-Construct.png'),
        require('@/assets/CardFrame-Light-Creature.png'),
        require('@/assets/CardFrame-Light-Destined Construct Creature.png'),
        require('@/assets/CardFrame-Light-Destined Construct.png'),
        require('@/assets/CardFrame-Light-Destined Creature.png'),
        require('@/assets/CardFrame-Light-Destined Location.png'),
        require('@/assets/CardFrame-Light-Destined Spell.png'),
        require('@/assets/CardFrame-Light-Immortal.png'),
        require('@/assets/CardFrame-Light-Location.png'),
        require('@/assets/CardFrame-Light-Spell.png'),
        require('@/assets/CardFrame-Light.png'),
        require('@/assets/CardFrame-LightCreature.png'),
        require('@/assets/CardFrame-Nature-Construct Creature.png'),
        require('@/assets/CardFrame-Nature-Construct.png'),
        require('@/assets/CardFrame-Nature-Creature.png'),
        require('@/assets/CardFrame-Nature-Destined Construct Creature.png'),
        require('@/assets/CardFrame-Nature-Destined Construct.png'),
        require('@/assets/CardFrame-Nature-Destined Creature.png'),
        require('@/assets/CardFrame-Nature-Destined Location.png'),
        require('@/assets/CardFrame-Nature-Destined Spell.png'),
        require('@/assets/CardFrame-Nature-Immortal.png'),
        require('@/assets/CardFrame-Nature-Location.png'),
        require('@/assets/CardFrame-Nature-Spell.png'),
        require('@/assets/CardFrame-Nature.png'),
        require('@/assets/CardFrame-NatureCreature.png'),
        require('@/assets/CardFrame-Void-Construct Creature.png'),
        require('@/assets/CardFrame-Void-Construct.png'),
        require('@/assets/CardFrame-Void-Creature.png'),
        require('@/assets/CardFrame-Void-Destined Construct Creature.png'),
        require('@/assets/CardFrame-Void-Destined Construct.png'),
        require('@/assets/CardFrame-Void-Destined Creature.png'),
        require('@/assets/CardFrame-Void-Destined Location.png'),
        require('@/assets/CardFrame-Void-Destined Spell.png'),
        require('@/assets/CardFrame-Void-Immortal.png'),
        require('@/assets/CardFrame-Void-Location.png'),
        require('@/assets/CardFrame-Void-Spell.png'),
        require('@/assets/CardFrame-Void.png'),
        require('@/assets/CardFrame-VoidCreature.png'),
        require('@/assets/CardFrame-Water-Construct Creature.png'),
        require('@/assets/CardFrame-Water-Construct.png'),
        require('@/assets/CardFrame-Water-Creature.png'),
        require('@/assets/CardFrame-Water-Destined Construct Creature.png'),
        require('@/assets/CardFrame-Water-Destined Construct.png'),
        require('@/assets/CardFrame-Water-Destined Creature.png'),
        require('@/assets/CardFrame-Water-Destined Location.png'),
        require('@/assets/CardFrame-Water-Destined Spell.png'),
        require('@/assets/CardFrame-Water-Immortal.png'),
        require('@/assets/CardFrame-Water-Location.png'),
        require('@/assets/CardFrame-Water-Spell.png'),
        require('@/assets/CardFrame-Water.png'),
        require('@/assets/CardFrame-WaterCreature.png')
        /* 
        require('@/assets/CardFrame-Light-Location.png'),
        require('@/assets/CardFrame-Dark-Location.png'),
        require('@/assets/CardFrame-Fire-Location.png'),
        require('@/assets/CardFrame-Water-Location.png'),
        require('@/assets/CardFrame-Nature-Location.png'),
        require('@/assets/CardFrame-Air-Location.png'),
        require('@/assets/CardFrame-Void-Location.png'),
        require('@/assets/CardFrame-Gold-Location.png'),
        require('@/assets/CardFrame-LightConstruct.png'),
        require('@/assets/CardFrame-DarkConstruct.png'),
        require('@/assets/CardFrame-FireConstruct.png'),
        require('@/assets/CardFrame-WaterConstruct.png'),
        require('@/assets/CardFrame-NatureConstruct.png'),
        require('@/assets/CardFrame-AirConstruct.png'),
        require('@/assets/CardFrame-VoidConstruct.png'),
        require('@/assets/CardFrame-GoldConstruct.png'),
        require('@/assets/CardFrame-LightImmortal.png'),
        require('@/assets/CardFrame-DarkImmortal.png'),
        require('@/assets/CardFrame-FireImmortal.png'),
        require('@/assets/CardFrame-WaterImmortal.png'),
        require('@/assets/CardFrame-NatureImmortal.png'),
        require('@/assets/CardFrame-AirImmortal.png'),
        require('@/assets/CardFrame-VoidImmortal.png'),
        require('@/assets/CardFrame-GoldImmortal.png'),
        require('@/assets/CardFrame-LightSell.png'),
        require('@/assets/CardFrame-DarkSell.png'),
        require('@/assets/CardFrame-FireSell.png'),
        require('@/assets/CardFrame-WaterSell.png'),
        require('@/assets/CardFrame-NatureSell.png'),
        require('@/assets/CardFrame-AirSell.png'),
        require('@/assets/CardFrame-VoidSell.png'),
        require('@/assets/CardFrame-GoldSell.png'),
        require('@/assets/CardFrame-LightConstructCreature.png'),
        require('@/assets/CardFrame-DarkConstructCreature.png'),
        require('@/assets/CardFrame-FireConstructCreature.png'),
        require('@/assets/CardFrame-WaterConstructCreature.png'),
        require('@/assets/CardFrame-NatureConstructCreature.png'),
        require('@/assets/CardFrame-AirConstructCreature.png'),
        require('@/assets/CardFrame-VoidConstructCreature.png'),
        require('@/assets/CardFrame-GoldConstructCreature.png') */
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
      txtLightCostFillStyle: '#000000',
      txtLightCostLineWidth: 1,
      txtLightCostPositionX: 51,
      txtLightCostPositionY: 33,
      txtLightCostFont: '15px "Amiri", serif',
      txtLightCostLineHeight: 60,
    //#region DarkCostTextVariables
      txtDarkCost: "0",
      txtDarkCostMaxWidth: 250,
      txtDarkCostStrokeStyle: '#000000',
      txtDarkCostFillStyle: '#000000',
      txtDarkCostLineWidth: 1,
      txtDarkCostPositionX: 51,
      txtDarkCostPositionY: 85,
      txtDarkCostFont: '15px "Amiri", serif',
      txtDarkCostLineHeight: 60,
    //#region FireCostTextVariables
      txtFireCost: "0",
      txtFireCostMaxWidth: 250,
      txtFireCostStrokeStyle: '#000000',
      txtFireCostFillStyle: '#000000',
      txtFireCostLineWidth: 1,
      txtFireCostPositionX: 30,
      txtFireCostPositionY: 45,
      txtFireCostFont: '15px "Amiri", serif',
      txtFireCostLineHeight: 60,
    //#region WaterCostTextVariables
      txtWaterCost: "0",
      txtWaterCostMaxWidth: 250,
      txtWaterCostStrokeStyle: '#000000',
      txtWaterCostFillStyle: '#000000',
      txtWaterCostLineWidth: 1,
      txtWaterCostPositionX: 72,
      txtWaterCostPositionY: 45,
      txtWaterCostFont: '15px "Impact", sans-serif',
      txtWaterCostLineHeight: 60,
    //#region NatureCostTextVariables
      txtNatureCost: "0",
      txtNatureCostMaxWidth: 250,
      txtNatureCostStrokeStyle: '#000000',
      txtNatureCostFillStyle: '#000000',
      txtNatureCostLineWidth: 1,
      txtNatureCostPositionX: 72,
      txtNatureCostPositionY: 74,
      txtNatureCostFont: '15px "Impact", sans-serif',
      txtNatureCostLineHeight: 60,
    //#region AirCostTextVariables
      txtAirCost: "0",
      txtAirCostMaxWidth: 250,
      txtAirCostStrokeStyle: '#000000',
      txtAirCostFillStyle: '#000000',
      txtAirCostLineWidth: 1,
      txtAirCostPositionX: 29,
      txtAirCostPositionY: 74,
      txtAirCostFont: '15px "Impact", sans-serif',
      txtAirCostLineHeight: 60,
    //#region BasicCostTextVariables
      txtBasicCost: "0",
      txtBasicCostMaxWidth: 250,
      txtBasicCostStrokeStyle: '#000000',
      txtBasicCostFillStyle: '#000000',
      txtBasicCostLineWidth: 1,
      txtBasicCostPositionX: -25,
      txtBasicCostPositionY: 30,
      txtBasicCostFont: '15px "Impact", sans-serif',
      txtBasicCostLineHeight: 60,
    //#region TotalCostTextVariables
      txtTotalCost: "0",
      txtTotalCostMaxWidth: 250,
      txtTotalCostStrokeStyle: '#000000',
      txtTotalCostFillStyle: '#000000',
      txtTotalCostLineWidth: 1,
      txtTotalCostPositionX: 50,
      txtTotalCostPositionY: 61,
      txtTotalCostFont: '20px "Amiri", serif',
      txtTotalCostLineHeight: 60,
    //#region MainTextVariables 8
      txtMain: '',
      txtMainMaxWidth: 250,
      txtMainStrokeStyle: '#000000',
      txtMainFillStyle: '#000000',
      txtMainLineWidth: 1,
      txtMainPositionX: 38,
      txtMainPositionY: 355,
      txtMainFont: '20px "Amiri", serif',
      txtMainLineHeight: 60,    
    //#region MainTextVariables 8
      txtFull: '',
      txtFullMaxWidth: 250,
      txtFullStrokeStyle: '#000000',
      txtFullFillStyle: '#000000',
      txtFullLineWidth: 1,
      txtFullPositionX: 579,
      txtFullPositionY: 514,
      txtFullFont: '15px "Amiri", serif',
      txtFullLineHeight: 60, 
    //#region NameTextVariables
      txtName: '',
      txtNameMaxWidth: 250,
      txtNameStrokeStyle: '#000000',
      txtNameFillStyle: '#000000',
      txtNameLineWidth: 0.5,
      txtNamePositionX: 97,
      txtNamePositionY: 38,
      txtNameFont: 'Bold 17px "Amiri", serif',
      txtNameLineHeight: 60,
    //#region TypeTextVariables
        txtType: '',
        txtTypeMaxWidth: 250,
        txtTypeStrokeStyle: '#000000',
        txtTypeFillStyle: '#000000',
        txtTypeLineWidth: 0.5,
        txtTypePositionX: 34,
        txtTypePositionY: 319,
        txtTypeFont: 'Bold 20px "Amiri", serif',
        txtTypeLineHeight: 60,
    //#region SubtypeTextVariables
      txtSubtype: '',
      txtSubtypeMaxWidth: 250,
      txtSubtypeStrokeStyle: '#000000',
      txtSubtypeFillStyle: '#000000',
      txtSubtypeLineWidth: 0.5,
      txtSubtypePositionX: 197,
      txtSubtypePositionY: 319,
      txtSubtypeFont: 'Bold 20px "Amiri", serif',
      txtSubtypeLineHeight: 60,
    //#region Set Name Text Variables
      txtSetname: '',
      txtSetnameMaxWidth: 250,
      txtSetnameStrokeStyle: '#000000',
      txtSetnameFillStyle: '#000000',
      txtSetnameLineWidth: 0.5,
      txtSetnamePositionX: 206,
      txtSetnamePositionY: 504,
      txtSetnameFont: '10px "Amiri", serif',
      txtSetnameLineHeight: 60,
    //#region FlavorTextVariables
      txtFlavor: '',
      txtFlavorMaxWidth: 250,
      txtFlavorStrokeStyle: '#000000',
      txtFlavorFillStyle: '#000000',
      txtFlavorLineWidth: 0.5,
      txtFlavorPositionX: 45,
      txtFlavorPositionY: 471,
      txtFlavorFont: '15px "Amiri", serif',
      txtFlavorLineHeight: 60,
    //#region BottomInfoVariables
      txtBottom: '',
      txtBottomMaxWidth: 250,
      txtBottomStrokeStyle: '#000000',
      txtBottomFillStyle: '#000000',
      txtBottomLineWidth: 1,
      txtBottomPositionX: 29,
      txtBottomPositionY: 504,
      txtBottomFont: '10px "Amiri", serif',
      txtBottomLineHeight: 60,
    //#region ForceTextVariables
      txtForce: '',
      txtForceMaxWidth: 250,
      txtForceStrokeStyle: '#000000',
      txtForceFillStyle: '#000000',
      txtForceLineWidth: 1,
      txtForcePositionX: 282,
      txtForcePositionY: 492,
      txtForceFont: 'Bold 30px "Amiri", serif',
      txtForceLineHeight: 60,
    //#region VitalityTextVariables
      txtVitality: '',
      txtVitalityMaxWidth: 250,
      txtVitalityStrokeStyle: '#000000',
      txtVitalityFillStyle: '#000000',
      txtVitalityLineWidth: 1,
      txtVitalityPositionX: 322,
      txtVitalityPositionY: 492,
      txtVitalityFont: 'Bold 30px "Amiri", serif',
      txtVitalityLineHeight: 60,
  //#region Other
    player_profile: "",
    player_profile_id: 0,
    selectErrors: [],
    noCardSelectedMsg: "No card selected",
    imgUrl: "None",
    cardImgUrl: "None",
    multiCardImport: false,
    importUUIDList: [],
  //#region Subtype Selector
    activator: null,
    attach: null,
    colors: ['green', 'purple', 'indigo', 'cyan', 'teal', 'orange'],
    editing: null,
    editingIndex: -1,
    nonce: 1,
    menu: false,
    x: 0,
    search: null,
    y: 0,
    subtype_items: [],
  //#region Card Selector
    cardFolderIdList: [],
    maxCardFolderId: 0,
    dialogRename: false,
    dialogImport: false,
    active: [],
    open: [],
    cloneCardGUID: "none",
    cardSelectorFiles: {
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
    cardSelectorItems: [ 
        {
          Name: 'Root',
          ParentId: null,
          FolderId: 1,
          Children: [] 
        }, 
      ],
    selectedItems: [],
  //#region Image Manager
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
  //#endregion
  }),
mounted() 
    {
    this.checkPlayerProfile(this.user)
    //this.getCardCollection()
    //this.setImage(this.framePreset)
    
    //this.arrIndex = (this.textProperties.indexOf(this.textPropertySelected))
    this.setArrays()
    this.setDataSnapShot()
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
  // UI Methods
    displayNotification(group, title, text, type) {
        this.$notify({
                    group: group,
                    title: title,
                    text: text,
                    type: type
                  })
      },
  // #region PlayerProfile Methods
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

              //Check if PlayerProfile has any cards in collection
              if(!this.player_profile.card_collection.length < 1 || this.player_profile.card_collection == undefined) 
                { this.cardSelectorItems = this.player_profile.card_collection
                }
              //Check if PlayerProfile has uploaded any images
              if(!this.player_profile.image_collection.length < 1 || this.player_profile.image_collection == undefined) 
                { this.imageSelectorItems = this.player_profile.image_collection
                  this.changeCurrentImageDir(this.imageSelectorItems, 1);
                }
              this.maxImageFolderId = this.getTreeItemsList(this.imageSelectorItems)
              this.maxCardFolderId = this.getTreeItemsList(this.cardSelectorItems)
              //this.imageManagerTest()
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
    async checkPlayerProfile(user) {
          if(user.player_profile_id != null) {
          this.player_profile = await this.getPlayerProfile(user.player_profile_id)
          this.player_profile_id = user.player_profile_id
          this.updateCardCollection()
          this.updateImageCollection()
        }
          else {
          this.newPlayerProfile(this.user.id)
        }
      },
    // #endregion profile methods
    // Data Store Methods
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
      var arrayAffinities = [
        this.txtLightCost,
        this.txtDarkCost,
        this.txtFireCost,
        this.txtWaterCost,
        this.txtNatureCost,
        this.txtAirCost,
        this.txtBasicCost
      ] 

      var affinityContainsX = false 

      for (var i = 0; i < arrayAffinities.length; i++) {
          var currentAffinity = (arrayAffinities[i])
          console.log(currentAffinity)
          if (stringService.isNumeric(currentAffinity)) {
            // do nothing 
          } else {
            affinityContainsX = true 
            }      
      }

      if(affinityContainsX) {
        this.txtTotalCost = 'X'
      }
      else {
      var light = Number(this.txtLightCost)
      var dark = Number(this.txtDarkCost)
      var fire = Number(this.txtFireCost)
      var water = Number(this.txtWaterCost)
      var nature = Number(this.txtNatureCost)
      var air = Number(this.txtAirCost)
      var basic = Number(this.txtBasicCost)
      
      
      var total = light + dark + fire + water + nature + air + basic
      this.txtTotalCost = String(total)
        }
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
    async loadCardSubTypesPublic() {
      const subTypeList = await apiService.fetchDataPublicList('/public/cardsubtype/') 
      for(var index in subTypeList) {
          var currentSubType = subTypeList[index]
          let subtTypeItem = { "text": currentSubType.name }
          if(currentSubType.private === false) {
            this.subtype_items.push(subtTypeItem)
            console.log("added" + subtTypeItem.text + "public")
          }
        }
      let subTypeItemHeader = { header: 'Select an option or create one' }
      this.subtype_items.push(subTypeItemHeader)

      },
    async loadCardSubTypesPrivate(user) {
      const subTypeList = await apiService.fetchCollection('cardsubtype') 
      for(var index in subTypeList) {
          var currentSubType = subTypeList[index]
          let subtTypeItem = { "text": currentSubType.name }
          console.log(currentSubType)
          console.log(currentSubType.player_profile.id)
          if(currentSubType.player_profile.id === user.player_profile_id) {
            if(currentSubType.private === true) {
              console.log("Should be added to subtype itmes")
            }
          }
        }
        // Sort subtypes in alphabetiacal order 
        this.subtype_items.sort((a, b) => (a.text > b.text) ? 1 : -1)
      },
  // Card Preview Methods
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
          //store default image size from blob 
          if(vm.cardImageWidth == 0 && vm.cardImageHeight == 0)
          {
          vm.cardImageWidth = img.width;
          vm.cardImageHeight = img.height;
          }

          //Set canvas to card image size
          vm.canvasImageWidth = vm.cardImageWidth
          vm.canvasImageHeight = vm.cardImageHeight
          
          
          
          
        };
        
        img.onerror = function() {
          alert( "not a valid file: " + file.type);
        };
        img.src = evt.target.result;
      }

      let img = new Image();
      this.createImage(this.selectedImage)
      },
    async onTextChange(event) {
      window.requestAnimationFrame(this.repaint);
      },
    async onSizeChange(event) {
      //Get percentage of width and height
      this.cardImageWidth = mathService.GetPercentage(this.canvasImageWidth, this.cardImageAspectPercentage)
      this.cardImageHeight = mathService.GetPercentage(this.canvasImageHeight, this.cardImageAspectPercentage)
      window.requestAnimationFrame(this.repaint);
      },
    async createImage(file) { 
      var reader = new FileReader();
      reader.onload = evt => {
        var image = new Image();
      }
      var vm = this;

      reader.onload = function(event) {
        
        vm.cardImage = event.target.result;
        vm.repaint();
      };

      reader.readAsDataURL(file);
      },

  // Card Data Methods
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
              
              //Developer note. Make sure vairables in card data confrom to the following. Failure will result in duplicate code.
              
              /* GOOD   "txt_subtype" = "this.txtSubtype" */              
              /* BAD   "txt_subtype" = "this.txtSubType" */

              //console.log(currentKey)
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
        this.canvasWidth = obj.canvas_width = obj.canvas_width
        this.canvasHeight = obj.canvas_height
        this.canvasImageWidth = obj.image_width
        this.canvasImageHeight = obj.image_height
        this.cardFrame = obj.card_frame
        this.cardImageWidth = obj.card_image_width
        this.cardImageHeight = obj.card_image_height
        this.cardImagePositionX = obj.card_image_positionX
        this.cardImagePositionY = obj.card_image_positionY
        this.cardFrameCheckbox = obj.card_frame_chkbx
        this.cardImageAspectPercentage = obj.card_image_apsect_percentage

        //add text property variables
        for(var textProperty in this.textProperties) 
        {
        var currentIndex = Number(textProperty)
        this.$data[this.textProperties[currentIndex] + "MaxWidth"] = this.arrMaxWidth[currentIndex]
        this.$data[this.textProperties[currentIndex] + "FillStyle"] = this.arrFillStyle[currentIndex]
        this.$data[this.textProperties[currentIndex] + "LineWidth"] = this.arrLineWidth[currentIndex]
        this.$data[this.textProperties[currentIndex] + "PositionX"] = this.arrPositionX[currentIndex]
        this.$data[this.textProperties[currentIndex] + "PositionY"] = this.arrPositionY[currentIndex]
        this.$data[this.textProperties[currentIndex] + "Font"] = this.arrFont[currentIndex]
        this.$data[this.textProperties[currentIndex] + "LineHeight"] = this.arrLineHeight[currentIndex]
        }

        //clear text property arrays 
        this.arrMaxWidth = []
        this.arrStrokeStyle = []
        this.arrFillStyle = []
        this.arrLineWidth = []
        this.arrPositionX =[]
        this.arrPositionY = []
        this.arrFont = []
        this.arrLineHeight = []

        //add text property variables
        for(var textProperty in this.textProperties) 
        {
        var currentIndex = Number(textProperty)
        this.arrMaxWidth.push((this.$data[this.textProperties[currentIndex] + "MaxWidth"]))
        this.arrStrokeStyle.push(this.$data[this.textProperties[currentIndex] + "StrokeStyle"])  
        this.arrFillStyle.push(this.$data[this.textProperties[currentIndex] + "FillStyle"])  
        this.arrLineWidth.push(this.$data[this.textProperties[currentIndex] + "LineWidth"])  
        this.arrPositionX.push(this.$data[this.textProperties[currentIndex] + "PositionX"])  
        this.arrPositionY.push(this.$data[this.textProperties[currentIndex] + "PositionY"])  
        this.arrFont.push(this.$data[this.textProperties[currentIndex] + "Font"]) 
        this.arrLineHeight.push(this.$data[this.textProperties[currentIndex] + "LineHeight"]) 
        }
        
              
        } catch(e) {
          alert("Sorry, your file doesn't appear to be valid JSON data.");
          alert(e)
        }
      }
              
        reader.onerror = evt => {
          console.error(evt);
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
        "txt_full": {
            "text": this.txtFull,
            "max_width": this.txtFullMaxWidth,
            "stroke_style": this.txtFullStrokeStyle,
            "fill_style": this.txtFullFillStyle,
            "line_width": this.txtFullLineWidth,
            "position": {
              "x": this.txtFullPositionX,
              "y": this.txtFullPositionY
            },
            "font": this.txtFullnameFont,
            "line_height:": this.txtFullnameLineHeight
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
            "text": this.txtSubtype,
            "max_width": this.txtSubtypeMaxWidth,
            "stroke_style": this.txtSubtypeStrokeStyle,
            "fill_style": this.txtSubtypeFillStyle,
            "line_width": this.txtSubtypeLineWidth,
            "position": {
              "x": this.txtSubtypePositionX,
              "y": this.txtSubtypePositionY
            },
            "font": this.txtSubtypeFont,
            "line_height:": this.txtSubtypeLineHeight
          },
        "txt_setname": {
            "text": this.txtSetname,
            "max_width": this.txtSetnameMaxWidth,
            "stroke_style": this.txtSetnameStrokeStyle,
            "fill_style": this.txtSetnameFillStyle,
            "line_width": this.txtSetnameLineWidth,
            "position": {
              "x": this.txtSetnamePositionX,
              "y": this.txtSetnamePositionY
            },
            "font": this.txtSetnameFont,
            "line_height:": this.txtSetnameLineHeight
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
        "canvas_width": this.canvasWidth,
        "canvas_height": this.canvasHeight,
        "image_width": this.canvasImageWidth,
        "image_height": this.canvasImageHeight,
        "card_frame": this.cardFrame,
        "card_image_width": this.cardImageWidth,
        "card_image_height": this.cardImageHeight,
        "card_image_positionX": this.cardImagePositionX,
        "card_image_positionY": this.cardImagePositionY,
        "card_frame_chkbx": this.cardFrameCheckbox,
        "card_image_apsect_percentage": this.cardImageAspectPercentage
        }
      },
    async onCardDataChangeFromId(currentCardData) {
        var obj = currentCardData
        try {
          //Set card data 
          var key
          var numKeys = 0
          var keys = Object.keys(obj)
          for (key in keys) {
            var currentKey = keys[numKeys]
            if(currentKey.startsWith("txt", 0))
            {
              //console.log(currentKey)
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
        this.canvasWidth = obj.canvas_width
        this.canvasHeight = obj.canvas_height
        this.canvasImageWidth = obj.image_width
        this.canvasImageHeight = obj.image_height
        this.cardFrame = obj.card_frame
        this.cardImageWidth = obj.card_image_width
        this.cardImageHeight = obj.card_image_height
        this.cardImagePositionX = obj.card_image_positionX
        this.cardImagePositionY = obj.card_image_positionY
        this.cardFrameCheckbox = obj.card_frame_chkbx
        this.cardImageAspectPercentage = obj.card_image_apsect_percentage
        
        //clear text property arrays 
        this.arrMaxWidth = []
        this.arrStrokeStyle = []
        this.arrFillStyle = []
        this.arrLineWidth = []
        this.arrPositionX =[]
        this.arrPositionY = []
        this.arrFont = []
        this.arrLineHeight = []

        //add text property variables
        for(var textProperty in this.textProperties) 
        {
        var currentIndex = Number(textProperty)
        this.arrMaxWidth.push((this.$data[this.textProperties[currentIndex] + "MaxWidth"]))
        this.arrStrokeStyle.push(this.$data[this.textProperties[currentIndex] + "StrokeStyle"])  
        this.arrFillStyle.push(this.$data[this.textProperties[currentIndex] + "FillStyle"])  
        this.arrLineWidth.push(this.$data[this.textProperties[currentIndex] + "LineWidth"])  
        this.arrPositionX.push(this.$data[this.textProperties[currentIndex] + "PositionX"])  
        this.arrPositionY.push(this.$data[this.textProperties[currentIndex] + "PositionY"])  
        this.arrFont.push(this.$data[this.textProperties[currentIndex] + "Font"]) 
        this.arrLineHeight.push(this.$data[this.textProperties[currentIndex] + "LineHeight"]) 
        }

        } catch(e) {
          alert("Sorry, your file doesn't appear to be valid JSON data.");
          alert(e)
        }
      },
    async loadCardFromUUID(cardUUID) {
        this.resetCanvas();
        const currentCard = await cardService.fetchCardFromUUID(cardUUID)
        if(currentCard.card_data) 
        {
          //console.log("Success: Card Id " + cardUUID + " was found!")
          this.cardId = currentCard.id
          if(currentCard.img_url != "None")
          { this.drawImageFrmBlob(currentCard.img_url) }
          this.imgUrl = currentCard.img_url
          this.onCardDataChangeFromId(currentCard.card_data);
        }
        else
        {
          this.cardId = 0
          this.imgUrl = "None"
          this.displayNotification('authentication', 'Card NOT found!', 'Please delete this card and create a new one', 'warn')
          //console.log("Error: Card Id " + cardUUID + " was not found!")
        }
      },
    getBlankCard: function() {
      this.imgUrl = "https://django-obelisk-static.s3.amazonaws.com/media/UserProfiles/a73e1cf2-5331-4fd1-8418-31c3bfbc14b7/Images/Card_No_Image.png"

      let cardData = {
          "txt_full": {
			"font": "20px sans-serif",
			"text": "",
			"position": {
				"x": 579,
				"y": 514
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_main": {
			"font": "20px 'Amiri', serif",
			"text": "",
			"position": {
				"x": 38,
				"y": 355
			},
			"max_width": 300,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_name": {
			"font": "Bold 17px 'Amiri', serif",
			"text": "None",
			"position": {
				"x": 97,
				"y": 38
			},
			"max_width": "250",
			"fill_style": "#000000",
			"line_width": "0.5",
			"stroke_style": "#000000"
		},
		"txt_type": {
			"font": "Bold 20px 'Amiri', serif",
			"text": "",
			"position": {
				"x": 34,
				"y": 319
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": "0.5",
			"stroke_style": "#000000"
		},
		"txt_force": {
			"font": "Bold 30px 'Amiri', serif",
			"text": "",
			"position": {
				"x": 282,
				"y": 492
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_bottom": {
			"font": "10px 'Amiri', serif",
			"text": "",
			"position": {
				"x": 29,
				"y": 504
			},
			"max_width": 300,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_flavor": {
			"font": "Italic 15px 'Amiri', serif",
			"text": "",
			"position": {
				"x": 41,
				"y": 452
			},
			"max_width": 300,
			"fill_style": "#000000",
			"line_width": "0.5",
			"stroke_style": "#000000"
		},
		"txt_setname": {
			"font": "10px 'Amiri', serif",
			"text": "",
			"position": {
				"x": 206,
				"y": 504
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": "0.5",
			"stroke_style": "#000000"
		},
		"txt_subtype": {
			"font": "Bold 20px 'Amiri', serif",
			"text": "",
			"position": {
				"x": 197,
				"y": 319
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": "0.5",
			"stroke_style": "#000000"
		},
		"txt_air_cost": {
			"font": "15px 'Amiri', serif",
			"text": "0",
			"position": {
				"x": 29,
				"y": 74
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_vitality": {
			"font": "Bold 30px 'Amiri', serif",
			"text": "",
			"position": {
				"x": 322,
				"y": 492
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_dark_cost": {
			"font": "15px 'Amiri', serif",
			"text": "0",
			"position": {
				"x": 51,
				"y": 85
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_fire_cost": {
			"font": "15px 'Amiri', serif",
			"text": "0",
			"position": {
				"x": 30,
				"y": 45
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_basic_cost": {
			"font": "15px \"Impact\", sans-serif",
			"text": "0",
			"position": {
				"x": -25,
				"y": 33
			},
			"max_width": 250,
			"fill_style": "#FFFFFF",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_light_cost": {
			"font": "15px 'Amiri', serif",
			"text": "0",
			"position": {
				"x": 51,
				"y": 33
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_total_cost": {
			"font": "Bold 20px 'Amiri', serif",
			"text": "0",
			"position": {
				"x": 50,
				"y": 61
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_water_cost": {
			"font": "15px 'Amiri', serif",
			"text": "0",
			"position": {
				"x": 72,
				"y": 45
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
		"txt_nature_cost": {
			"font": "15px 'Amiri', serif",
			"text": "0",
			"position": {
				"x": 72,
				"y": 74
			},
			"max_width": 250,
			"fill_style": "#000000",
			"line_width": 1,
			"stroke_style": "#000000"
		},
          "cardtype": "",
          "affinity_selected": null,
          "subtype_selected": [],
          "canvas_property_selected": "",
          "canvas_width": 375,
          "canvas_height": 523,
          "image_width": 0,
          "image_height": 0,
          "card_frame": "",
          "card_image_width": 0,
          "card_image_height": 0,
          "card_image_positionX": 0,
          "card_image_positionY": 0,
          "card_frame_chkbx": false,
          "card_image_apsect_percentage": 100
        }

      let blankCard = {
        "card_name": "None",
        "affinity_cost_total": "0",
        "affinity_cost_light": "0",
        "affinity_cost_dark": "0",
        "affinity_cost_fire": "0",
        "affinity_cost_water": "0",
        "affinity_cost_nature": "0",
        "affinity_cost_air": "0",
        "affinity_cost_basic": "0",
        "card_type": "",
        "card_subtypes": "",
        "card_maintext": "",
        "card_fulltext": "",
        "card_flavortext": "",
        "card_bottomtext": "",
        "card_forcetext": "",
        "card_vitalitytext": "",
        "card_serialnumber": null,
        "card_set_id": null,
        "card_set_name": this.txtSetname,
        "player_profile_id": this.player_profile_id, 
        "description": "none",
        "img_url": this.imgUrl,
        "cardimg_url": "None",
        "card_data": cardData,
        "extra_data": []
      }
      
      return blankCard

      },
    getCurrentCard: function() {
      // Create card data
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
        "txt_full": {
            "text": this.txtFull,
            "max_width": this.txtFullMaxWidth,
            "stroke_style": this.txtFullStrokeStyle,
            "fill_style": this.txtFullFillStyle,
            "line_width": this.txtFullLineWidth,
            "position": {
              "x": this.txtFullPositionX,
              "y": this.txtFullPositionY
            },
            "font": this.txtFullnameFont,
            "line_height:": this.txtFullnameLineHeight
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
            "text": this.txtSubtype,
            "max_width": this.txtSubtypeMaxWidth,
            "stroke_style": this.txtSubtypeStrokeStyle,
            "fill_style": this.txtSubtypeFillStyle,
            "line_width": this.txtSubtypeLineWidth,
            "position": {
              "x": this.txtSubtypePositionX,
              "y": this.txtSubtypePositionY
            },
            "font": this.txtSubtypeFont,
            "line_height:": this.txtSubtypeLineHeight
          },
        "txt_setname": {
            "text": this.txtSetname,
            "max_width": this.txtSetnameMaxWidth,
            "stroke_style": this.txtSetnameStrokeStyle,
            "fill_style": this.txtSetnameFillStyle,
            "line_width": this.txtSetnameLineWidth,
            "position": {
              "x": this.txtSetnamePositionX,
              "y": this.txtSetnamePositionY
            },
            "font": this.txtSetnameFont,
            "line_height:": this.txtSetnameLineHeight
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
        "canvas_width": this.canvasWidth,
        "canvas_height": this.canvasHeight,
        "image_width": this.canvasImageWidth,
        "image_height": this.canvasImageHeight,
        "card_frame": this.cardFrame,
        "card_image_width": this.cardImageWidth,
        "card_image_height": this.cardImageHeight,
        "card_image_positionX": this.cardImagePositionX,
        "card_image_positionY": this.cardImagePositionY,
        "card_frame_chkbx": this.cardFrameCheckbox,
        "card_image_apsect_percentage": this.cardImageAspectPercentage
        }

      // Create current card to save to database 
      let currentCard = {
        "card_name": this.txtName,
        "affinity_cost_total": this.txtTotalCost,
        "affinity_cost_light": this.txtLightCost,
        "affinity_cost_dark": this.txtDarkCost,
        "affinity_cost_fire": this.txtFireCost,
        "affinity_cost_water": this.txtWaterCost,
        "affinity_cost_nature": this.txtNatureCost,
        "affinity_cost_air": this.txtAirCost,
        "affinity_cost_basic": this.txtBasicCost,
        "card_type": this.txtType,
        "card_subtypes": this.txtSubtype,
        "card_maintext": this.txtMain,
        "card_fulltext": this.txtFull,
        "card_flavortext": this.txtFlavor,
        "card_bottomtext": this.txtBottom,
        "card_forcetext": this.txtForce,
        "card_vitalitytext": this.txtVitality,
        "card_serialnumber": null,
        "card_set_id": null,
        "card_set_name": this.txtSetname,
        "player_profile_id": this.user.player_profile_id, 
        "description": "none",
        "img_url": this.imgUrl,
        "cardimg_url": this.cardImgUrl,
        "card_data": cardData,
        "extra_data": []
      }

      return currentCard
      },
  // Card Service Methods
    async updateCardCollection() {
        this.maxCardFolderId = this.getTreeItemsList(this.cardSelectorItems)
        let payload = {
          "card_collection": this.cardSelectorItems,
        }
        if(this.cardSelectorItems[0].Children[0])
        await userService.updatePlayerProfile(this.user.player_profile_id, payload)
      },
    async publishCard() {
      console.log("You published ")
      },
    async postCard(newCard) {
      const currentCard = await cardService.createCard(newCard)
      return currentCard
      },
    async patchCard() {
      // Create CardData
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
          "txt_full": {
              "text": this.txtFull,
              "max_width": this.txtFullMaxWidth,
              "stroke_style": this.txtFullStrokeStyle,
              "fill_style": this.txtFullFillStyle,
              "line_width": this.txtFullLineWidth,
              "position": {
                "x": this.txtFullPositionX,
                "y": this.txtFullPositionY
              },
              "font": this.txtFullFont,
              "line_height:": this.txtFullLineHeight
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
              "text": this.txtSubtype,
              "max_width": this.txtSubtypeMaxWidth,
              "stroke_style": this.txtSubtypeStrokeStyle,
              "fill_style": this.txtSubtypeFillStyle,
              "line_width": this.txtSubtypeLineWidth,
              "position": {
                "x": this.txtSubtypePositionX,
                "y": this.txtSubtypePositionY
              },
              "font": this.txtSubtypeFont,
              "line_height:": this.txtSubtypeLineHeight
            },
          "txt_setname": {
              "text": this.txtSetname,
              "max_width": this.txtSetnameMaxWidth,
              "stroke_style": this.txtSetnameStrokeStyle,
              "fill_style": this.txtSetnameFillStyle,
              "line_width": this.txtSetnameLineWidth,
              "position": {
                "x": this.txtSetnamePositionX,
                "y": this.txtSetnamePositionY
              },
              "font": this.txtSetnameFont,
              "line_height:": this.txtSetnameLineHeight
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
          "canvas_width": this.canvasWidth,
          "canvas_height": this.canvasHeight,
          "image_width": this.canvasImageWidth,
          "image_height": this.canvasImageHeight,
          "card_frame": this.cardFrame,
          "card_image_width": this.cardImageWidth,
          "card_image_height": this.cardImageHeight,
          "card_image_positionX": this.cardImagePositionX,
          "card_image_positionY": this.cardImagePositionY,
          "card_frame_chkbx": this.cardFrameCheckbox,
          "card_image_apsect_percentage": this.cardImageAspectPercentage
          }

      // Create payload to save to databse 
        
        let payload = {
          "card_name": this.txtName,
          "affinity_cost_total": this.txtTotalCost,
          "affinity_cost_light": this.txtLightCost,
          "affinity_cost_dark": this.txtDarkCost,
          "affinity_cost_fire": this.txtFireCost,
          "affinity_cost_water": this.txtWaterCost,
          "affinity_cost_nature": this.txtNatureCost,
          "affinity_cost_air": this.txtAirCost,
          "affinity_cost_basic": this.txtBasicCost,
          "card_type": this.txtType,
          "card_subtypes": this.txtSubtype,
          "card_maintext": this.txtMain,
          "card_fulltext": this.txtFull,
          "card_flavortext": this.txtFlavor,
          "card_bottomtext": this.txtBottom,
          "card_forcetext": this.txtForce,
          "card_vitalitytext": this.txtVitality,
          "card_serialnumber": null,
          "card_set_id": null,
          "card_set_name": this.txtSetname,
          "player_profile_id": this.user.player_profile_id, 
          "description": "none",
          "img_url": this.imgUrl,
          "cardimg_url": this.cardImgUrl,
          "card_data": cardData,
          "extra_data": []
        }
      // Call Cardservice
        const response = await cardService.updateCard(this.cardId, payload)
        .then((response) =>{
        switch(response.status) {
          case (200): 
            console.log("Success patched!")
            this.displayNotification('authentication', 'Card saved.', this.active[0].Name + ' was updated successfully' , 'success')
            break;
          case (404): 
            this.displayNotification('authentication', 'Card NOT found!', 'Please try creating a new card first', 'warn')
            break;
          case (500): 
            this.displayNotification('authentication', 'Internal server error', 'Something went wrong on our end', 'error')                                       
            break;   
          }
        });
      },
    
    async saveCard() {
        const cardImage = await this.updateCardImage()
        this.cardImgUrl = cardImage.img_url
        this.patchCard()
      },
    async deleteCard() {
      await cardService.deleteCard(this.cardId, payload)
      },
  // Subtype Methods 
    async sort_subTypes() {

      //Remove Header first
      this.subtype_items.splice(0,1)

      // Sort subtypes in alphabetiacal order 
      this.subtype_items.sort((a, b) => (a.text > b.text) ? 1 : -1)

      // Add header back
      let subTypeItemHeader = { header: 'Select an option or create one' }
      this.subtype_items.splice(0, 0, subTypeItemHeader)
    },
  // Draw Image Methods
    async drawImageFrmBlob(imgUrl) {
      if(imgUrl != "none")
        {
          console.log(imgUrl)
          const imgBlob = await fetch(imgUrl, 
          {
          method: 'GET',
          mode: 'cors',
          cache: 'no-cache',
          headers: {
              Origin: window.location.origin,
          },
          })
            .then(function(response) {
              return response.blob()
            })
            console.log(imgBlob)
            this.selectedImage = imgBlob
            this.onImageChange();
        }
        else
        {
          this.resetCanvas();
        }
      },
    async setImage(url) {

      this.cardImage = url;

      this.paint();

      },

    async setImageToCanvas(url, callback, callback2) {
          var vm = this; 
          var ctx = this.getContext();

          var tempCanvas = document.createElement('canvas'); // Create a new canvas as cache canvas
          var tempctx = tempCanvas.getContext('2d');
                    
          var background = new Image();
          background.src = url
          background.onload = function() {
          //Temp canvas first
              tempCanvas.width = vm.cardImageWidth; tempCanvas.height = vm.cardImageHeight; // setting width and height
              //Round card frame 
              roundedImage(tempctx, 0, 0, 375, 523, 16);
              tempctx.clip();
              tempctx.drawImage(background, vm.cardImagePositionX, vm.cardImagePositionY, vm.cardImageWidth, vm.cardImageHeight);
            
            
          //True Canvas
            //Round card frame 
              roundedImage(ctx, 0, 0, 375, 523, 16);
              ctx.clip();
              ctx.clearRect(0, 0, vm.canvasWidth, vm.canvasHeight);
              ctx.drawImage(tempCanvas, 0, 0);
            



            if ( typeof callback == 'function' ) {
            callback();
          }
          if ( typeof callback2 == 'function' ) {
            callback2();
          }
        };

        function roundedImage(ctx, x, y, width, height, radius) {
            ctx.beginPath();
            ctx.moveTo(x + radius, y);
            ctx.lineTo(x + width - radius, y);
            ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
            ctx.lineTo(x + width, y + height - radius);
            ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
            ctx.lineTo(x + radius, y + height);
            ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
            ctx.lineTo(x, y + radius);
            ctx.quadraticCurveTo(x, y, x + radius, y);
            ctx.closePath();
        }
      },    
    async setImageToCanvasFirst(url, callback, callback2) {

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
    async setCardFrameToCanvas() {
      if(this.cardFrameCheckbox == true) {
          var vm = this;
          var ctx = this.getContext();
          var frameCanvas = document.createElement('canvas'); // Create a new canvas as cache canvas
          var framectx = frameCanvas.getContext('2d');

          var background = new Image();
          
          //Looop through all 6 affintiies
              var cardFrameIndex
              var afffinitiesSelected = ""
              var affinityIndex
              var affinityElements = ['Light', 'Dark', 'Fire', 'Water', 'Nature', 'Air']
              for(affinityIndex in affinityElements)
              {
                console.log(vm.AffinityList[affinityIndex])
                var currentAffinityCost = "txt" + String(affinityElements[affinityIndex]) + "Cost" 
                if(this.$data[currentAffinityCost] != 0)
                {
                  afffinitiesSelected += String(affinityElements[affinityIndex])
                }
                console.log(currentAffinityCost)
                console.log(this.$data[currentAffinityCost])
              }
              
              if(afffinitiesSelected != "") 
              {
                console.log(afffinitiesSelected + " if")
                
                  try 
                  {
                    cardFrameIndex = (vm.cardFramePresets.indexOf(require('@/assets/CardFrame-' + afffinitiesSelected + '-' + vm.txtType + '.png')))
                  }
                      
                  catch 
                  {
                    console.log("Card Type not found")
                    
                    try 
                    {
                      cardFrameIndex = (vm.cardFramePresets.indexOf(require('@/assets/CardFrame-Gold-' + vm.txtType + '.png')))  
                    }
                    catch 
                    {
                      cardFrameIndex = (vm.cardFramePresets.indexOf(require('@/assets/CardFrame-Gold.png')))    
                    }
                    
                  }
              }
              else
              {
                console.log(afffinitiesSelected + " else")
                
                try 
                {
                  cardFrameIndex = (vm.cardFramePresets.indexOf(require('@/assets/CardFrame-Void' + '-' + vm.txtType + '.png')))  
                }
                catch 
                {
                  cardFrameIndex = (vm.cardFramePresets.indexOf(require('@/assets/CardFrame-Void.png')))    
                }
              }
              
              
              console.log(vm.cardFramePresets[cardFrameIndex])    
              background.src = vm.cardFramePresets[cardFrameIndex]
          
          //Temp canvas first
            frameCanvas.width = vm.canvasWidth; frameCanvas.height = vm.canvasHeight; // setting width and height
            framectx.drawImage(background, 0, 0, vm.canvasWidth, vm.canvasHeight);
          //True Canvas
            

            ctx.drawImage(frameCanvas, 0, 0);
            /*
            framectx.clearRect(0, 0, vm.canvasWidth, vm.canvasHeight);
            ctx.drawImage(background, 0, 0, vm.canvasWidth, vm.canvasHeight); */
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
    getContext() {

      return document.getElementById(this.canvasElementId).getContext("2d");

      },
    async paint() {
        console.log("Paint")
        var vm = this;

        if ( this.cardImage == '' )
          this.setTextToCanvas(this.text);

        this.getContext().clearRect(0, 0, this.canvasWidth, this.canvasHeight);
        this.setImageToCanvasFirst(this.cardImage, function(){
            vm.setCardFrameToCanvas(); }, function() {
            vm.setTextToCanvas(vm.text);
          }
        );

      },  

    async repaint() {
      console.log("Repaint")
      var vm = this;

      if ( this.cardImage == '' )
        this.setTextToCanvas(this.text);

      /* this.getContext().clearRect(0, 0, this.canvasWidth, this.canvasHeight); */
      this.setImageToCanvas(this.cardImage, function(){
      vm.setCardFrameToCanvas(); }, function() {
          vm.setTextToCanvas(vm.text);
        });
      //this.setDataSnapShot()
      },
    async roundedImage(x, y, width, height, radius) {
      ctx.beginPath();
      ctx.moveTo(x + radius, y);
      ctx.lineTo(x + width - radius, y);
      ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
      ctx.lineTo(x + width, y + height - radius);
      ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
      ctx.lineTo(x + radius, y + height);
      ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
      ctx.lineTo(x, y + radius);
      ctx.quadraticCurveTo(x, y, x + radius, y);
      ctx.closePath();
      },
  // User Button Methods
    async reset(event) {
      const blankCard = await this.getBlankCard()
      this.onCardDataChangeFromId(blankCard.card_data)
      this.resetCanvas()
      this.drawImageFrmBlob(this.imgUrl)      
      },
    async resetCanvas() {
        
      // Canvas Properties
        
        this.canvasWidth = 0;
        this.canvasHeight = 0;
        this.selectedImage = null;
        this.cardFrame = "";
        this.cardFrameCheckbox = false;
        this.text = '';
        this.canvasWidth = 375;
        this.canvasHeight = 523;

      // Card Image Properties 
        this.cardImage = '';
        this.cardImageHeight = 0;
        this.cardImageWidth = 0;
        this.cardImagePositionX = 0;
        this.cardImagePositionY = 0;
        this.cardImageAspectPercentage = 100;
        window.requestAnimationFrame(this.repaint);
        this.getContext().clearRect(0, 0, this.canvasWidth, this.canvasHeight);
      },
    
    
    async downloadCardImage(event) {

        var dt = document.getElementById(this.canvasElementId).toDataURL('image/png');

        /* Change MIME type to trick the browser to download the file instead of displaying it */
        dt = dt.replace(/^data:image\/[^;]*/, 'data:application/octet-stream');

        /* In addition to <a>'s "download" attribute, you can define HTTP-style headers */
        dt = dt.replace(/^data:application\/octet-stream/, 'data:application/octet-stream;headers=Content-Disposition%3A%20attachment%3B%20filename=Meme.png');
        
        document.getElementById('downloadCardImage').href = dt;
      },
    async downloadCardData() {
      let filename = "card.json"
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
      "txt_full": {
              "text": this.txtFull,
              "max_width": this.txtFullMaxWidth,
              "stroke_style": this.txtFullStrokeStyle,
              "fill_style": this.txtFullFillStyle,
              "line_width": this.txtFullLineWidth,
              "position": {
                "x": this.txtFullPositionX,
                "y": this.txtFullPositionY
              },
              "font": this.txtFullFont,
              "line_height:": this.txtFullLineHeight
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
          "text": this.txtSubtype,
          "max_width": this.txtSubtypeMaxWidth,
          "stroke_style": this.txtSubtypeStrokeStyle,
          "fill_style": this.txtSubtypeFillStyle,
          "line_width": this.txtSubtypeLineWidth,
          "position": {
            "x": this.txtSubtypePositionX,
            "y": this.txtSubtypePositionY
          },
          "font": this.txtSubtypeFont,
          "line_height:": this.txtSubtypeLineHeight
        },
      "txt_setname": {
          "text": this.txtSetname,
          "max_width": this.txtSetnameMaxWidth,
          "stroke_style": this.txtSetnameStrokeStyle,
          "fill_style": this.txtSetnameFillStyle,
          "line_width": this.txtSetnameLineWidth,
          "position": {
            "x": this.txtSetnamePositionX,
            "y": this.txtSetnamePositionY
          },
          "font": this.txtSetnameFont,
          "line_height:": this.txtSetnameLineHeight
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
      "canvas_width": this.canvasWidth,
      "canvas_height": this.canvasHeight,
      "image_width": this.canvasImageWidth,
      "image_height": this.canvasImageHeight,
      "card_frame": this.cardFrame,
      "card_image_width": this.cardImageWidth,
      "card_image_height": this.cardImageHeight,
      "card_image_positionX": this.cardImagePositionX,
      "card_image_positionY": this.cardImagePositionY,
      "card_frame_chkbx": this.cardFrameCheckbox,
      "card_image_apsect_percentage": this.cardImageAspectPercentage
      }
      let jsonData = ''
      jsonData = JSON.stringify(cardData, null, 2)
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
    
    
  // File Tree Methods
    findTreeItem: function (items, id) {
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
    isTreeItemChild: function (items, id) {
        if (!items) {
            return;
        }
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            // Test current object
            if (item.ParentId === id) {
                return true;
            }
            // Test children recursively
            const child = this.findTreeItem(item.Children, id);
            if (child) {
                return child;
            }
        }
        return false;
      },
    getTreeItemsList: function(items) {
        if (!items) {
            // Do nothing
            return;
        }
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            // Test current object
              //console.log("Name: " + item.Name + " Folder: " + item.FolderId)
              this.cardFolderIdList.push(item.FolderId)
            // Test children recursively
            const child = this.getTreeItemsList(item.Children);
        }
        return (Math.max(...this.cardFolderIdList))
      },
    getRootFolderId(cardFolderIdList) {
      return (Math.min(...cardFolderIdList))

      },
    checkStart: function (evt) {
        var self = this;
        self.active = [];
        self.active.push(self.findTreeItem(self.cardSelectorItems, Number(evt.from.id)))
        //console.log("Current active:" + self.active[0].Name)
        this.updateCardCollection(this.cardSelectorItems)
      },
    checkEnd: function (evt) {        
        var self = this;
        var itemSelected = self.active[0];
        var fromParent = itemSelected.ParentId ? self.findTreeItem(self.cardSelectorItems, itemSelected.ParentId) : null;
        var toParent = self.findTreeItem(self.cardSelectorItems, Number(evt.to.id));
        console.log("itemSelected: " + itemSelected.Name)
        console.log("toParent: " + toParent.Name)
        
        switch(true) {
          // Move File or Folder out of the file tree
          case(toParent.FolderId === itemSelected.FolderId) :
            console.log("Move File or Folder out of the file tree")
            console.log("Cannot move file or folder out of the file tree")
            break;
          // Move Root anywhere
          case(toParent.Children && itemSelected.ParentId === null) :
            console.log("Move Root anywhere")
            console.log("Cannot move root folder")
            break;  
          // Move File to current Parent Folder
          case(toParent.Children && itemSelected.file && itemSelected.ParentId === toParent.FolderId) :
            console.log("Move File to current Parent Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            itemSelected.ParentId = toParent.FolderId;
            console.log(itemSelected)
            console.log(toParent)
            toParent.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
            break;
            break;
          // Move File to Root Folder
          case(toParent.Children && itemSelected.file && toParent.ParentId === null) :
            console.log("Move File to Root Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            itemSelected.ParentId = toParent.FolderId;
            console.log(itemSelected)
            console.log(toParent)
            toParent.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
            break;
          // Move Folder to Root Folder
          case(toParent.Children && itemSelected.Children && toParent.ParentId === null) :
            console.log("Move Folder to Root Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            itemSelected.ParentId = 1
            console.log(itemSelected)
            console.log(toParent)
            toParent.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
            break;
          // Move File to Folder not in Parent Folder    
          case(itemSelected.file && toParent.Children && itemSelected.ParentId != toParent.FolderId) :
            console.log("Move File to Folder not in Parent Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            itemSelected.ParentId = toParent.FolderId;
            console.log(itemSelected)
            console.log(toParent)
            toParent.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
            break;
          // Move File to File in current Folder 
          case(toParent.file && itemSelected.file && itemSelected.ParentId === toParent.ParentId) :
            console.log("Move File to File in current Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            console.log(toParent.Name + " is Not a folder")
            var toParentIndex = objFrom.indexOf(toParent)
            var itemSelectedIndex = objFrom.indexOf(itemSelected)
            console.log("toParentIndex: " + toParentIndex)
            console.log("itemSelectedIndex: " + itemSelectedIndex)
            // Remove item selected 
            objFrom.splice(itemSelectedIndex, 1);
            // Insert itemSelected at index of toParent
            objFrom.splice(toParentIndex, 0, itemSelected)
            console.log(objFrom.indexOf(itemSelected))
            break;
          // Move File to File not in Parent Folder
          case(itemSelected.file && toParent.file && itemSelected.ParentId != toParent.ParentId) :
            console.log("Move File to File in different Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            itemSelected.ParentId = toParent.ParentId;
            console.log(itemSelected)
            console.log(toParent)
            var ParentFolder = self.findTreeItem(self.cardSelectorItems, Number(toParent.ParentId));
            ParentFolder.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
            break;
          // Move Parent Folder to Child Folder
          case(itemSelected.Children && toParent.Children && itemSelected.FolderId === toParent.ParentId) :
            console.log("Cannot Move Parent Folder to Child Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            break;
          // Move Child Folder to Parent Folder
          case(itemSelected.Children && toParent.Children && itemSelected.ParentId === toParent.FolderId) :
            console.log("Child Folder is already child of current Parent Folder")
            console.log("Cannot Move Child Folder to Parent Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
             var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            itemSelected.ParentId = toParent.FolderId;
            console.log(itemSelected)
            console.log(toParent)
            toParent.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
            break;
          // Move Folder to Folder in current Parent Folder
          case(toParent.Children && itemSelected.Children && itemSelected.ParentId === toParent.ParentId) :
            console.log("Move Folder to Folder in current Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            itemSelected.ParentId = toParent.FolderId;
            console.log(itemSelected)
            console.log(toParent)
            toParent.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
            break;
          // Move Folder to Folder NOT in current Parent Folder
          case(toParent.Children && itemSelected.Children && itemSelected.ParentId != toParent.ParentId) :
            console.log("Move Folder to Folder in different Folder")
            
            //Check if toParent has the same Parent ID as selected Item. 
            if(itemSelected.FolderId)

            // Check if toParent is Nested Child Folder
            var toNestedChildFolder = this.isTreeItemChild(itemSelected.Children, toParent.FolderId)
            console.log(toNestedChildFolder)
            
            if(toNestedChildFolder) {
            console.log("Cannot move parent folder to nested child folder in child folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            }
            else {

            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            var newParentId
            toParent.ParentId > 1 ? newParentId = toParent.FolderId : newParentId = toParent.ParentId;
            console.log("new Parent Id: " + newParentId)
            console.log(itemSelected)
            console.log(toParent)
            itemSelected.ParentId = newParentId
            var ParentFolder = self.findTreeItem(self.cardSelectorItems, Number(newParentId));
            ParentFolder.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
              }
            break;
          // Move Parent Folder to Child Folder
          case(itemSelected.Children && toParent.Children && itemSelected.FolderId === toParent.ParentId) :
            console.log("Cannot Move Parent Folder to Child Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            break;
          // Move Folder to File NOT in current Parent Folder
          case(toParent.file && itemSelected.Children && itemSelected.ParentId != toParent.ParentId) :
            // Check if toParent is Nested Child Folder
            var toNestedChildFolder = this.isTreeItemChild(itemSelected.Children, toParent.FolderId)
            if(!toNestedChildFolder) { toNestedChildFolder = this.isTreeItemChild(itemSelected.Children, toParent.ParentId) }
            console.log(toNestedChildFolder)
            
            if(toNestedChildFolder) {
            console.log("Cannot move parent folder to nested child folder in child folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            }
            
            else {
            console.log("Move Folder to File NOT in current Parent Folder")
            console.log("Moved " + itemSelected.Name + " to " + toParent.Name + " in Folder " + toParent.ParentId)
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            console.log(objFrom)
            itemSelected.ParentId = toParent.ParentId;
            console.log(itemSelected)
            console.log(toParent)
            var ParentFolder = self.findTreeItem(self.cardSelectorItems, Number(toParent.ParentId));
            ParentFolder.Children.push(itemSelected);
            console.log(toParent.Children)
            console.log(self.cardSelectorItems)
            }
            break;
          // Move Folder to File in current Parent Folder
          case(toParent.file && itemSelected.Children && itemSelected.ParentId === toParent.ParentId):
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            console.log(toParent.Name + " is Not a folder")
            var toParentIndex = objFrom.indexOf(toParent)
            var itemSelectedIndex = objFrom.indexOf(itemSelected)
            console.log("toParentIndex: " + toParentIndex)
            console.log("itemSelectedIndex: " + itemSelectedIndex)
            // Remove item selected 
            objFrom.splice(itemSelectedIndex, 1);
            // Insert itemSelected at index of toParent
            objFrom.splice(toParentIndex, 0, itemSelected)
            console.log(objFrom.indexOf(itemSelected))
            break;
        }
        this.updateCardCollection(this.cardSelectorItems)
        self.active = [];
        return false;

        /* //Only change folder if toParent target is a folder and active is not Root. 
        if(toParent.Children && itemSelected.Name != "Root") {

          //Check to make sure active folder is not the parent of a child
          if (toParent.ParentId === itemSelected.FolderId) 
          {
              console.log("Item is parent of child")
              //DO NOTHING 
          }
          else
          {
            if(itemSelected != toParent) {
              var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
              console.log(objFrom)
              objFrom.splice(objFrom.indexOf(itemSelected), 1);
              console.log(objFrom)
              itemSelected.ParentId = toParent.FolderId;
              console.log(itemSelected)
              console.log(toParent)
              toParent.Children.push(itemSelected);
              console.log(toParent.Children)
              console.log(self.cardSelectorItems)
            }
          }
        this.updateCardCollection(this.cardSelectorItems)
        self.active = [];
        return false;
      }
      else
      {
        if(!itemSelected.Children) {
            var objFrom = fromParent ? fromParent.Children : self.cardSelectorItems;
            console.log(objFrom)
            console.log(toParent.Name + " is Not a folder")
            var toParentIndex = objFrom.indexOf(toParent)
            objFrom.splice(objFrom.indexOf(itemSelected), 1);
            objFrom.splice(toParentIndex, 0, itemSelected)
            this.updateCardCollection(this.cardSelectorItems)
            self.active = [];
            return false;
          }
        } */
      },
    fetchcardSelectorItems: function () {
        //load from api
      },
    saveUser: function (user) {
        //save 
      },
    async onTreeSelection() {
        if(this.active[0])
        {
          console.log(this.active[0].Name)
          console.log(this.active[0].GUID)
          if(this.active[0].GUID)
          {
            this.loadCardFromUUID(this.active[0].GUID)
          }
          else
          {
            console.log("else was triggered")
            this.reset()
          }
        }
        this.updateCardCollection(this.cardSelectorItems)
      },
    async onChoiceTest() {
      console.log(this.cardSelectorItems)
      },
    async onClickCopy() {
      var self = this;
        if(self.active[0]) {
          this.copyActiveTreeObject(self.active[0])
        }
        else
        {
          //Nothing was chosen or root was selected 
          console.log("No item selected to rename")  
        }
        this.updateCardCollection(this.cardSelectorItems)
      },
    async onClickDel() { 
        var self = this;
        if(self.active[0]) {
          this.delActiveTreeObject(self.active[0])
        }
        else
        {
          //Nothing was chosen or root was selected 
          console.log("No item selected to delete")  
        }
        this.updateCardCollection(this.cardSelectorItems)
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
    async addFolder() {
       var self = this;
       const newId = self.maxCardFolderId + 1
       var newFolderName = "New Folder"
       var parentId
       if(self.active[0])
       {
          if(self.active && self.active[0].Children) 
          {
              console.log("Nest into selected folder")
              parentId = self.active[0].FolderId           
          }
          else if (self.active) 
          {
              console.log("Added directly underneath active object")
              parentId = self.active[0].ParentId
          }
       }
       else
       {
          console.log("Added to root folder")
          parentId = 1
       }
       var children = []
       var newFolder = {
            FolderId: newId,
            Name: newFolderName,
            ParentId: parentId,
            Children: children,
       }

       var toParent = self.findTreeItem(self.cardSelectorItems, parentId)
       toParent.Children.push(newFolder)
       this.maxCardFolderId++
       this.updateCardCollection(this.cardSelectorItems)
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

    async cloneCard() {
      const cloneCard = this.getCurrentCard()
      const currentCard = await this.postCard(cloneCard)
      if(currentCard)
      {
        console.log(currentCard)
      }
      var self = this;
      const newId = self.maxCardFolderId + 1
      var newCardName = "New Card"
      var parentId
      if(self.active[0])
       {
        if(self.active && self.active[0].Children) 
        {
            console.log("Nest card into selected folder")
            parentId = self.active[0].FolderId           
        }
        else if (self.active) 
        {
            console.log("Added card directly underneath active object")
            parentId = self.active[0].ParentId
        }
       }
       else
       {
          console.log("Added card to root")
          parentId = 1
       }
       var children = []  
       var newCard = {
            FolderId: newId,
            Name: newCardName,
            ParentId: parentId,
            file: 'crd',
            GUID: currentCard.uuid,
       }

       var toParent = self.findTreeItem(self.cardSelectorItems, parentId)
       toParent.Children.push(newCard)
       this.maxCardFolderId++
       this.updateCardCollection(this.cardSelectorItems)
        },
    async addCard() {
      let blankCard = this.getBlankCard()
      const currentCard = await this.postCard(blankCard)
      if(currentCard)
      {
        console.log(currentCard)
      }
      var self = this;
      const newId = self.maxCardFolderId + 1
      var newCardName = "New Card"
      var parentId
      if(self.active[0])
       {
        if(self.active && self.active[0].Children) 
        {
            console.log("Nest card into selected folder")
            parentId = self.active[0].FolderId           
        }
        else if (self.active) 
        {
            console.log("Added card directly underneath active object")
            parentId = self.active[0].ParentId
        }
       }
       else
       {
          console.log("Added card to root")
          parentId = 1
       }
       var children = []  
       var newCard = {
            FolderId: newId,
            Name: newCardName,
            ParentId: parentId,
            file: 'crd',
            GUID: currentCard.uuid,
       }

       var toParent = self.findTreeItem(self.cardSelectorItems, parentId)
       toParent.Children.push(newCard)
       this.maxCardFolderId++
       this.updateCardCollection(this.cardSelectorItems)
        },
    async onRenameObject(event) {
        console.log("Object was renamed")
        this.updateCardCollection(this.cardSelectorItems)
        this.updateImageCollection(this.imageSelectorItems)
      },
    async importCardSingle(cardUUID) {
      const currentCard = await cardService.fetchCardFromUUID(cardUUID)
      if(currentCard)
      {
        console.log(currentCard)
      }
      var self = this;
      const newId = self.maxCardFolderId + 1
      var newCardName = currentCard.card_name
      var parentId
      if(self.active[0])
       {
        if(self.active && self.active[0].Children) 
        {
            console.log("Nest card into selected folder")
            parentId = self.active[0].FolderId           
        }
        else if (self.active) 
        {
            console.log("Added card directly underneath active object")
            parentId = self.active[0].ParentId
        }
       }
       else
       {
          console.log("Added card to root")
          parentId = 1
       }
       var children = []  
       var newCard = {
            FolderId: newId,
            Name: newCardName,
            ParentId: parentId,
            file: 'crd',
            GUID: currentCard.uuid,
       }

       var toParent = self.findTreeItem(self.cardSelectorItems, parentId)
       toParent.Children.push(newCard)
       this.maxCardFolderId++
       this.updateCardCollection(this.cardSelectorItems)
       this.importUUID = ""
      },
    async importCardMulti(cardUUID) {
      this.importUUIDList = cardUUID.split('\n')
      console.log(this.importUUIDList)
      for (var i in this.importUUIDList)
        this.importCardSingle(this.importUUIDList[i])
      },
    async importCard(cardUUID) {
      this.multiCardImport ? this.importCardMulti(cardUUID) :  this.importCardSingle(cardUUID)
      }, 
  // Image Manager Methods
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

       var toParent = self.findTreeItem(self.imageSelectorItems, parentId)
       toParent.Children.push(newFolder)
       self.maxImageFolderId++
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
        await userService.updatePlayerProfile(this.user.player_profile_id, payload)
      },
    async updateCurrentCardImage() {
        //Get active image item
        if(this.active[0].file === "crd" && this.activeImageItem.file === "img")
        {
        console.log("It worked")
        this.drawImageFrmBlob(this.activeImageItem.url)
        this.imgUrl = this.activeImageItem.url
        }
        else
        {
          console.log("It didn't work")
        }
      },
    async uploadImage(imageFile) {
      // Create bodyFormData
        var bodyFormData = new FormData();
        bodyFormData.append('img_url', imageFile);
        bodyFormData.append('player_profile_id', this.user.player_profile_id);
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
  // Developer Methods
    async info(event) {
      //var dt = document.getElementById(this.canvasElementId).toDataURL('image/png');
      //console.log("current image" + dt)
      console.log(this.$data)
      console.log(this.cardSelectorFiles)
        /* var numProperties = 0
        var textProperties = Object.keys(this.textProperties)
        for (textProperty in this.textProperties) 
        {
          // console.log(this.textProperties[textProperty])
          // console.log(this.textProperties[textProperty] + "Font")
        }  */
      },

    edit (index, item) {
      if (!this.editing) {
        this.editing = item
        this.editingIndex = index
      } else {
        this.editing = null
        this.editingIndex = -1
      }
    },
    filter (item, queryText, itemText) {
      if (item.header) return false

      const hasValue = val => val != null ? val : ''

      const text = hasValue(itemText)
      const query = hasValue(queryText)

      return text.toString()
        .toLowerCase()
        .indexOf(query.toString().toLowerCase()) > -1
    },
  },
  
watch: {
  active(active) {
    console.log("active item has changed yo!")
    this.updateCardCollection(this.cardSelectorItems)
    },
  cardSelectorItems(cardSelectorItems) {
    console.log("cardSelector items has changed yo!")
    this.updateCardCollection(this.cardSelectorItems)
    },
  cardId(cardId) {
    console.log("cardId has changed yo!")
    //this.loadCardFromID(this.cardId);
    },
  cardFrameCheckbox(cardFrameCheckbox) {
    console.log("Card frame change detected")
    this.setCardFrameToCanvas();
    window.requestAnimationFrame(this.repaint);
    },
  cardtype(cardtype) {
    switch(cardtype) {
      case ('Creature'):
        this.txtType = cardtype
        this.creature_enabled = true
        window.requestAnimationFrame(this.repaint);
        break;
      case ('Destined Creature'):
        this.txtType = cardtype
        this.creature_enabled = true
        window.requestAnimationFrame(this.repaint);
        break;
      case ('Construct'):
        this.txtType = cardtype
        this.creature_enabled = false
        window.requestAnimationFrame(this.repaint);
        break;
      case ('Spell'):
        this.txtType = cardtype
        this.creature_enabled = false
        window.requestAnimationFrame(this.repaint);
        break;
      case ('Destined Spell'):
        this.txtType = cardtype
        this.creature_enabled = false
        window.requestAnimationFrame(this.repaint);
        break;
      case ('Immortal'):
        this.txtType = cardtype
        this.creature_enabled = false
        window.requestAnimationFrame(this.repaint);
        break;  
      case ('Construct Creature'):
        this.txtType = cardtype
        this.creature_enabled = true
        window.requestAnimationFrame(this.repaint);
        break;
      default:
        this.txtType = cardtype
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
      window.requestAnimationFrame(this.repaint);
    },
  arrStrokeStyle(arrStrokeStyle) {
      // console.log("StrokeStyle Change detected")
      this.$data[this.textPropertySelected + "StrokeStyle"] = arrStrokeStyle[this.arrIndex]
      window.requestAnimationFrame(this.repaint);
    },
  arrFillStyle(arrFillStyle) {
      // console.log("FillStyle Change detected")
      this.$data[this.textPropertySelected + "FillStyle"] = arrFillStyle[this.arrIndex]
      window.requestAnimationFrame(this.repaint);
    },
  arrLineWidth(arrLineWidth) {
      // console.log("LineWidth Change detected")
      this.$data[this.textPropertySelected + "LineWidth"] = arrLineWidth[this.arrIndex]
      window.requestAnimationFrame(this.repaint);
    },
  arrPositionX(arrPositionX) {
      console.log("Change detected x")
      this.$data[this.textPropertySelected + "PositionX"] = this.arrPositionX[this.arrIndex]
      window.requestAnimationFrame(this.repaint);
    },
  arrPositionY(arrPositionY) {
      console.log("Change detected y")
      this.$data[this.textPropertySelected + "PositionY"] = this.arrPositionY[this.arrIndex]
      window.requestAnimationFrame(this.repaint);
    },
  arrFont(arrFont) {
      // console.log("Font Change detected")
      this.$data[this.textPropertySelected + "Font"] = arrFont[this.arrIndex]
      window.requestAnimationFrame(this.repaint);
    },
  arrLineHeight(arrLineHeight) {
      // console.log("Line Height Change detected")
      this.$data[this.textPropertySelected + "LineHeight"] = arrLineHeight[this.arrIndex]
      window.requestAnimationFrame(this.repaint);
    },  
  txtLightCost(txtLightCost) {
    this.setCostTotal();
    window.requestAnimationFrame(this.repaint);
    },
  txtDarkCost(txtDarkCost) {
    this.setCostTotal();
    window.requestAnimationFrame(this.repaint);
    },
  txtFireCost(txtFireCost) {
    this.setCostTotal();
    window.requestAnimationFrame(this.repaint);
    },
  txtWaterCost(txtWaterCost) {
    this.setCostTotal();
    window.requestAnimationFrame(this.repaint);
    },
  txtNatureCost(txtNatureCost) {
    this.setCostTotal();
    window.requestAnimationFrame(this.repaint);
    },
  txtAirCost(txtAirCost) {
    this.setCostTotal();
    window.requestAnimationFrame(this.repaint);
    },
  txtBasicCost(txtBasicCost) {
    this.setCostTotal();
    window.requestAnimationFrame(this.repaint);
    },
  txtName(txtName) {
    window.requestAnimationFrame(this.repaint);
    },
  txtMain(txtMain) {
    window.requestAnimationFrame(this.repaint);
    },
  txtFull(txtFull) {
    window.requestAnimationFrame(this.repaint);
    },
  txtType(txtType) {
    window.requestAnimationFrame(this.repaint);
    },
  txtSubtype(txtSubtype) {
    window.requestAnimationFrame(this.repaint);
    },
  txtSetname(txtSetname) {
    window.requestAnimationFrame(this.repaint);
    },
  txtFlavor(txtFlavor) {
    window.requestAnimationFrame(this.repaint);
    },
  txtBottom(txtBottom) {
    window.requestAnimationFrame(this.repaint);
    },
  txtForce(txtForce) {
    window.requestAnimationFrame(this.repaint);
    },
  txtVitality(txtVitality) {
    window.requestAnimationFrame(this.repaint);
    },

  
  subtype_selected(val, prev) {
      var currentSubtypeItems = ""
      for (const subType of val) {
        currentSubtypeItems = currentSubtypeItems + (subType.text + " ")
        }
      this.txtSubtype = currentSubtypeItems
      console.log(this.txtSubtype)
      console.log(this.$data)
      window.requestAnimationFrame(this.repaint);

      if (val.length === prev.length) return

      this.subtype_selected = val.map(v => {
        if (typeof v === 'string') {
          v = {
            text: v,
            color: this.colors[this.nonce - 1],
          }

          this.subtype_items.push(v)
          this.sort_subTypes()

          this.nonce++
        }

        return v
      })
      },
  multiCardImport(multiCardImport) {
      //console.log("Multi card import " + this.multicCardImport)
      this.importUUID = ""
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
        subtype_selections.push(subtype_selection)
        // console.log(this.subtype_items[subtype_selection])
      }

      
      return subtype_selections
      },
    selected() {
        if (!this.active.length) return undefined
        return this.active[0];
      },
    importUUIDLineCount() {
      // Return number of lines using regex if not empty
      return this.importUUID.length ? this.importUUID.split(/\r\n|\r|\n/).length : 0;
    }
  },
created() {
      this.loadCardSubTypesPublic()
      if(this.user) {
        console.log(this.user.player_profile_id)
        console.log(this.user.email)
        this.loadCardSubTypesPrivate(this.user)
      }
    }
  }
</script>

<style lang="css" scoped>
@import url('https://fonts.googleapis.com/css2?family=Amiri&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400;1,700&display=swap');

html,body{
    overflow-x: hidden;
}

p {
  color: #b2b4b2;
  margin: 0 1em;
  font-weight: 700;
}

.v-card {
  margin-bottom: 2em;
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

.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: .5;
  position: absolute;
}

.cardlistbar {
  width: 100%;
  height: 50vh;
  overflow-y: scroll;
}


/* Split Panes */
  .splitpanes {
    background-color: #f2f2f2;
  }
  .splitpanes__pane {
    justify-content: center;
    align-items: center;
    display: flex;
  }
  .splitpanes__splitter {
    background-color: #ccc;
    position: relative;
  }
  .splitpanes__splitter:before {
    content: '';
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    transition: 0.4s;
  }
  .splitpanes--vertical > .splitpanes__splitter:before {
    left: -30px;
    right: -30px;
  }
  .splitpanes--horizontal > .splitpanes__splitter:before {
    top: -30px;
    bottom: -30px;
  }
  .splitpanes__splitter:hover:before {
    background-color: rgba(255, 0, 0, 0.3);
  }

</style>
