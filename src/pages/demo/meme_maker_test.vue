<template>
  <v-app>
    <v-main>
      <v-container fluid class="pa-4">
        <v-row>
          <v-col cols="12">
            <h1 class="text-h4 text-center mb-6">Meme Maker</h1>
          </v-col>
        </v-row>

        <v-row>
          <!-- Controls Panel -->
          <v-col cols="12" md="4">
            <v-card class="pa-4">
              <v-card-title>Controls</v-card-title>
              
              <!-- Image Upload -->
              <v-file-input
                v-model="imageFile"
                label="Upload Image"
                accept="image/*"
                prepend-icon="mdi-camera"
                @change="handleImageUpload"
                class="mb-4"
              ></v-file-input>

              <!-- Text Input -->
              <v-text-field
                v-model="newText"
                :label="selectionState.selectedIndex >= 0 ? 'Edit selected text' : 'Enter new text'"
                @keyup.enter="selectionState.selectedIndex >= 0 ? updateSelectedText() : addText()"
                @input="updateTextRealTime"
                class="mb-2"
              ></v-text-field>

              <v-row class="mb-4">
                <v-col cols="6">
                  <v-select
                    v-model="textStyle.fontSize"
                    :items="fontSizes"
                    label="Font Size"
                    dense
                    @update:model-value="updateSelectedTextStyle"
                  ></v-select>
                </v-col>
                <v-col cols="6">
                  <v-color-picker
                    v-model="textStyle.color"
                    hide-inputs
                    mode="hexa"
                    class="ma-2"
                    @update:model-value="updateSelectedTextStyle"
                  ></v-color-picker>
                </v-col>
              </v-row>

              <v-btn
                @click="selectionState.selectedIndex >= 0 ? updateSelectedText() : addText()"
                :color="selectionState.selectedIndex >= 0 ? 'warning' : 'primary'"
                block
                class="mb-4"
                :disabled="!newText.trim()"
              >
                {{ selectionState.selectedIndex >= 0 ? 'Update Text' : 'Add Text' }}
              </v-btn>

              <v-btn
                v-if="selectionState.selectedIndex >= 0"
                @click="deselectText"
                color="secondary"
                block
                class="mb-4"
                outlined
              >
                Cancel Edit
              </v-btn>

              <!-- Text List -->
              <v-card v-if="textElements.length > 0" outlined class="mb-4">
                <v-card-title class="text-subtitle-1">Text Elements</v-card-title>
                <v-list dense>
                  <v-list-item
                    v-for="(text, index) in textElements"
                    :key="index"
                    class="px-2"
                  >
                    <v-list-item-content>
                      <v-list-item-title class="text-caption">
                        {{ text.content }}
                      </v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-btn
                        @click="removeText(index)"
                        icon
                        small
                        color="error"
                      >
                        <v-icon small>mdi-delete</v-icon>
                      </v-btn>
                    </v-list-item-action>
                  </v-list-item>
                </v-list>
              </v-card>

              <!-- Export Button -->
              <v-btn
                @click="exportMeme"
                color="success"
                block
                :disabled="!uploadedImage"
              >
                <v-icon left>mdi-download</v-icon>
                Export Meme
              </v-btn>
            </v-card>
          </v-col>

          <!-- Canvas Area -->
          <v-col cols="12" md="8">
            <v-card class="pa-4">
              <div
                ref="canvasContainer"
                class="canvas-container"
                :style="containerStyle"
                @click="handleCanvasClick"
              >
                <!-- Background Image -->
                <img
                  v-if="uploadedImage"
                  :src="uploadedImage"
                  class="background-image"
                  @load="onImageLoad"
                />

                <!-- Draggable Text Elements -->
                <div
                  v-for="(text, index) in textElements"
                  :key="index"
                  class="draggable-text"
                  :class="{ 'selected-text': selectionState.selectedIndex === index }"
                  :style="{
                    left: text.x + 'px',
                    top: text.y + 'px',
                    fontSize: text.fontSize + 'px',
                    color: text.color,
                    fontWeight: 'bold',
                    textShadow: '2px 2px 4px rgba(0,0,0,0.8)',
                    cursor: 'move',
                    userSelect: 'none',
                    position: 'absolute',
                    zIndex: 10,
                    border: selectionState.selectedIndex === index ? '2px solid #2196F3' : '2px solid transparent',
                    borderRadius: '4px',
                    padding: '4px'
                  }"
                  @mousedown="startDrag($event, index)"
                  @touchstart="startDrag($event, index)"
                  @click="selectText(index)"
                >
                  {{ text.content }}
                </div>

                <!-- Placeholder when no image -->
                <div
                  v-if="!uploadedImage"
                  class="placeholder"
                >
                  <v-icon size="64" color="grey">mdi-image-plus</v-icon>
                  <p class="text-h6 grey--text mt-4">Upload an image to start creating your meme</p>
                </div>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue'

// Reactive data
const imageFile = ref(null)
const uploadedImage = ref(null)
const newText = ref('')
const textElements = ref([])
const canvasContainer = ref(null)
const imageWidth = ref(0)
const imageHeight = ref(0)

// Text styling options
const textStyle = reactive({
  fontSize: 32,
  color: '#FFFFFF'
})

const fontSizes = [16, 20, 24, 28, 32, 36, 40, 48, 56, 64]

// Drag state
const dragState = reactive({
  isDragging: false,
  dragIndex: -1,
  startX: 0,
  startY: 0,
  startTextX: 0,
  startTextY: 0
})

// Add after the dragState reactive object
const selectionState = reactive({
  selectedIndex: -1,
  isEditing: false
})

// Computed styles
const containerStyle = computed(() => ({
  width: imageWidth.value ? imageWidth.value + 'px' : '100%',
  height: imageHeight.value ? imageHeight.value + 'px' : '400px',
  position: 'relative',
  border: '2px dashed #ccc',
  borderRadius: '8px',
  overflow: 'hidden',
  backgroundColor: '#f5f5f5'
}))

// Methods
const handleImageUpload = (event) => {
  const file = event.target.files?.[0] || imageFile.value?.[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      uploadedImage.value = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const onImageLoad = (event) => {
  const img = event.target
  const container = canvasContainer.value
  const containerWidth = container.clientWidth
  const maxWidth = Math.min(containerWidth, 800)
  
  const aspectRatio = img.naturalHeight / img.naturalWidth
  imageWidth.value = maxWidth
  imageHeight.value = maxWidth * aspectRatio
}

const addText = () => {
  if (newText.value.trim()) {
    textElements.value.push({
      content: newText.value,
      x: 50,
      y: 50 + (textElements.value.length * 60),
      fontSize: textStyle.fontSize,
      color: textStyle.color
    })
    newText.value = ''
  }
}

const removeText = (index) => {
  textElements.value.splice(index, 1)
}

const startDrag = (event, index) => {
  event.preventDefault()
  event.stopPropagation()
  
  dragState.isDragging = true
  dragState.dragIndex = index
  
  const clientX = event.type === 'touchstart' ? event.touches[0].clientX : event.clientX
  const clientY = event.type === 'touchstart' ? event.touches[0].clientY : event.clientY
  
  dragState.startX = clientX
  dragState.startY = clientY
  dragState.startTextX = textElements.value[index].x
  dragState.startTextY = textElements.value[index].y
  
  document.addEventListener('mousemove', handleDrag)
  document.addEventListener('mouseup', stopDrag)
  document.addEventListener('touchmove', handleDrag, { passive: false })
  document.addEventListener('touchend', stopDrag)
}

const handleDrag = (event) => {
  if (!dragState.isDragging) return
  
  event.preventDefault()
  
  const clientX = event.type === 'touchmove' ? event.touches[0].clientX : event.clientX
  const clientY = event.type === 'touchmove' ? event.touches[0].clientY : event.clientY
  
  const deltaX = clientX - dragState.startX
  const deltaY = clientY - dragState.startY
  
  const newX = Math.max(0, Math.min(imageWidth.value - 100, dragState.startTextX + deltaX))
  const newY = Math.max(0, Math.min(imageHeight.value - 50, dragState.startTextY + deltaY))
  
  textElements.value[dragState.dragIndex].x = newX
  textElements.value[dragState.dragIndex].y = newY
}

const stopDrag = () => {
  const wasDragging = dragState.isDragging
  dragState.isDragging = false
  dragState.dragIndex = -1
  
  document.removeEventListener('mousemove', handleDrag)
  document.removeEventListener('mouseup', stopDrag)
  document.removeEventListener('touchmove', handleDrag)
  document.removeEventListener('touchend', stopDrag)
  
  // Small delay to prevent immediate selection after drag
  if (wasDragging) {
    setTimeout(() => {
      dragState.isDragging = false
    }, 100)
  }
}

const exportMeme = () => {
  const canvas = document.createElement('canvas')
  const ctx = canvas.getContext('2d')
  
  canvas.width = imageWidth.value
  canvas.height = imageHeight.value
  
  const img = new Image()
  img.crossOrigin = 'anonymous'
  img.onload = () => {
    // Draw background image
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
    
    // Draw text elements
    textElements.value.forEach(text => {
      ctx.font = `bold ${text.fontSize}px Arial`
      ctx.fillStyle = text.color
      ctx.strokeStyle = '#000000'
      ctx.lineWidth = 2
      ctx.textAlign = 'left'
      ctx.textBaseline = 'top'
      
      // Add text shadow effect
      ctx.strokeText(text.content, text.x, text.y)
      ctx.fillText(text.content, text.x, text.y)
    })
    
    // Download the meme
    const link = document.createElement('a')
    link.download = 'meme.png'
    link.href = canvas.toDataURL()
    link.click()
  }
  img.src = uploadedImage.value
}

// Cleanup event listeners
onUnmounted(() => {
  document.removeEventListener('mousemove', handleDrag)
  document.removeEventListener('mouseup', stopDrag)
  document.removeEventListener('touchmove', handleDrag)
  document.removeEventListener('touchend', stopDrag)
})

// Add these methods after the existing methods

const selectText = (index) => {
  if (!dragState.isDragging) {
    selectionState.selectedIndex = index
    selectionState.isEditing = true
    newText.value = textElements.value[index].content
    textStyle.fontSize = textElements.value[index].fontSize
    textStyle.color = textElements.value[index].color
  }
}

const deselectText = () => {
  selectionState.selectedIndex = -1
  selectionState.isEditing = false
  newText.value = ''
}

const updateSelectedText = () => {
  if (selectionState.selectedIndex >= 0 && newText.value.trim()) {
    textElements.value[selectionState.selectedIndex].content = newText.value.trim()
    deselectText()
  }
}

const updateTextRealTime = () => {
  if (selectionState.selectedIndex >= 0 && newText.value.trim()) {
    textElements.value[selectionState.selectedIndex].content = newText.value
  }
}

const updateSelectedTextStyle = () => {
  if (selectionState.selectedIndex >= 0) {
    textElements.value[selectionState.selectedIndex].fontSize = textStyle.fontSize
    textElements.value[selectionState.selectedIndex].color = textStyle.color
  }
}

// Add this method
const handleCanvasClick = (event) => {
  if (event.target === canvasContainer.value) {
    deselectText()
  }
}
</script>

<style scoped>
.canvas-container {
  min-height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.background-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  position: absolute;
  top: 0;
  left: 0;
}

.draggable-text {
  white-space: nowrap;
  font-family: 'Arial', sans-serif;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.draggable-text:hover {
  opacity: 0.8;
}

.placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
}

/* Mobile responsiveness */
@media (max-width: 768px) {
  .canvas-container {
    min-height: 300px;
  }
}

/* Prevent text selection during drag */
.draggable-text {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Touch-friendly drag targets */
@media (hover: none) and (pointer: coarse) {
  .draggable-text {
    padding: 8px;
    min-width: 44px;
    min-height: 44px;
    display: flex;
    align-items: center;
  }
}

/* Add this to the existing style section */
.selected-text {
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(33, 150, 243, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(33, 150, 243, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(33, 150, 243, 0);
  }
}

.draggable-text {
  transition: all 0.2s ease;
}

.draggable-text:hover {
  opacity: 0.8;
  transform: scale(1.05);
}
</style>