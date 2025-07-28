<template>
  <v-app>
    <!-- App Bar -->
    <v-app-bar color="primary" dark app>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>SocialConnect</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-bell</v-icon>
        <v-badge color="error" content="3" offset-x="10" offset-y="10" dot></v-badge>
      </v-btn>
      <v-avatar class="ml-2" size="36">
        <v-img src="https://randomuser.me/api/portraits/women/85.jpg"></v-img>
      </v-avatar>
    </v-app-bar>

    <v-main class="bg-grey-lighten-4">
      <v-container>
        <v-row>
          <!-- Left Sidebar -->
          <v-col cols="12" md="3" class="d-none d-md-block">
            <v-card class="mb-4">
              <v-list>
                <v-list-item prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg" title="Jane Smith" subtitle="@janesmith"></v-list-item>
                <v-divider></v-divider>
                <v-list-item prepend-icon="mdi-account" title="Profile"></v-list-item>
                <v-list-item prepend-icon="mdi-account-group" title="Friends"></v-list-item>
                <v-list-item prepend-icon="mdi-bookmark" title="Saved"></v-list-item>
                <v-list-item prepend-icon="mdi-calendar" title="Events"></v-list-item>
                <v-list-item prepend-icon="mdi-image-multiple" title="Photos"></v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <!-- Main Content -->
          <v-col cols="12" md="6">
            <!-- Post Status -->
            <v-card class="mb-4">
              <v-card-text>
                <v-textarea
                  v-model="newPostContent"
                  label="What's on your mind?"
                  auto-grow
                  rows="2"
                  variant="outlined"
                  hide-details
                ></v-textarea>
                <v-row class="mt-2">
                  <v-col>
                    <v-btn prepend-icon="mdi-image" variant="text" color="primary">Photo</v-btn>
                    <v-btn prepend-icon="mdi-video" variant="text" color="primary">Video</v-btn>
                    <v-btn prepend-icon="mdi-emoticon" variant="text" color="primary">Feeling</v-btn>
                  </v-col>
                  <v-col cols="auto">
                    <v-btn 
                      color="primary" 
                      :disabled="!newPostContent.trim()" 
                      @click="addNewPost"
                    >
                      Post
                    </v-btn>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>

            <!-- News Feed -->
            <v-card v-for="(post, index) in posts" :key="index" class="mb-4">
              <v-card-title class="d-flex align-center">
                <v-avatar size="40" class="mr-3">
                  <v-img :src="post.avatar"></v-img>
                </v-avatar>
                <div>
                  <div class="font-weight-bold">{{ post.username }}</div>
                  <div class="text-caption text-grey">{{ post.time }}</div>
                </div>
                <v-spacer></v-spacer>
                <v-menu>
                  <template v-slot:activator="{ props }">
                    <v-btn icon v-bind="props">
                      <v-icon>mdi-dots-horizontal</v-icon>
                    </v-btn>
                  </template>
                  <v-list>
                    <v-list-item title="Save Post"></v-list-item>
                    <v-list-item title="Hide Post"></v-list-item>
                    <v-list-item title="Report"></v-list-item>
                  </v-list>
                </v-menu>
              </v-card-title>

              <v-card-text>
                <p>{{ post.content }}</p>
                <v-img 
                  v-if="post.image" 
                  :src="post.image" 
                  class="mt-2 rounded-lg" 
                  cover
                  max-height="400"
                ></v-img>
              </v-card-text>

              <v-divider></v-divider>

              <v-card-actions>
                <v-btn 
                  variant="text" 
                  prepend-icon="mdi-heart" 
                  :color="post.liked ? 'error' : ''" 
                  @click="toggleLike(index)"
                >
                  {{ post.likes }} Like{{ post.likes !== 1 ? 's' : '' }}
                </v-btn>
                <v-btn variant="text" prepend-icon="mdi-comment">
                  {{ post.comments.length }} Comment{{ post.comments.length !== 1 ? 's' : '' }}
                </v-btn>
                <v-btn variant="text" prepend-icon="mdi-share">Share</v-btn>
              </v-card-actions>

              <v-divider></v-divider>

              <!-- Comments -->
              <v-list v-if="post.showComments">
                <v-list-item v-for="(comment, commentIndex) in post.comments" :key="commentIndex">
                  <template v-slot:prepend>
                    <v-avatar size="36">
                      <v-img :src="comment.avatar"></v-img>
                    </v-avatar>
                  </template>
                  <v-list-item-title class="font-weight-bold">{{ comment.username }}</v-list-item-title>
                  <v-list-item-subtitle>{{ comment.content }}</v-list-item-subtitle>
                </v-list-item>
              </v-list>

              <!-- Add Comment -->
              <v-card-text class="pt-0">
                <v-row no-gutters align="center">
                  <v-avatar size="36" class="mr-3">
                    <v-img src="https://randomuser.me/api/portraits/women/85.jpg"></v-img>
                  </v-avatar>
                  <v-text-field
                    v-model="post.newComment"
                    density="compact"
                    variant="outlined"
                    placeholder="Write a comment..."
                    append-inner-icon="mdi-send"
                    hide-details
                    @click:append-inner="addComment(index)"
                    @keyup.enter="addComment(index)"
                  ></v-text-field>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>

          <!-- Right Sidebar -->
          <v-col cols="12" md="3" class="d-none d-md-block">
            <v-card class="mb-4">
              <v-card-title>Suggested Friends</v-card-title>
              <v-list>
                <v-list-item v-for="(friend, i) in suggestedFriends" :key="i">
                  <template v-slot:prepend>
                    <v-avatar size="40">
                      <v-img :src="friend.avatar"></v-img>
                    </v-avatar>
                  </template>
                  <v-list-item-title>{{ friend.name }}</v-list-item-title>
                  <template v-slot:append>
                    <v-btn size="small" color="primary" variant="text">Add</v-btn>
                  </template>
                </v-list-item>
              </v-list>
            </v-card>

            <v-card>
              <v-card-title>Trending Topics</v-card-title>
              <v-list>
                <v-list-item v-for="(topic, i) in trendingTopics" :key="i">
                  <v-list-item-title>{{ topic.title }}</v-list-item-title>
                  <v-list-item-subtitle>{{ topic.posts }} posts</v-list-item-subtitle>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';

const name = 'News Feed';

const newPostContent = ref('');

const posts = ref([
  {
    username: 'John Doe',
    avatar: 'https://randomuser.me/api/portraits/men/32.jpg',
    time: '15 minutes ago',
    content: 'Just finished a great workout at the gym! 💪 Feeling energized and ready for the day ahead. #fitness #motivation',
    image: 'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80',
    likes: 24,
    liked: false,
    showComments: true,
    comments: [
      {
        username: 'Sarah Johnson',
        avatar: 'https://randomuser.me/api/portraits/women/44.jpg',
        content: 'Looking good! What's your workout routine?'
      },
      {
        username: 'Mike Wilson',
        avatar: 'https://randomuser.me/api/portraits/men/46.jpg',
        content: 'Keep it up! 💯'
      }
    ],
    newComment: ''
  },
  {
    username: 'Emily Clark',
    avatar: 'https://randomuser.me/api/portraits/women/26.jpg',
    time: '2 hours ago',
    content: 'Just got back from an amazing trip to Japan! The cherry blossoms were in full bloom and the food was incredible. Can\'t wait to share more photos! #travel #japan #cherryblossoms',
    image: 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80',
    likes: 47,
    liked: false,
    showComments: false,
    comments: [
      {
        username: 'Alex Turner',
        avatar: 'https://randomuser.me/api/portraits/men/22.jpg',
        content: 'Wow! I\'ve always wanted to visit Japan during cherry blossom season!'
      }
    ],
    newComment: ''
  }
]);

const suggestedFriends = ref([
  { name: 'Robert Johnson', avatar: 'https://randomuser.me/api/portraits/men/41.jpg' },
  { name: 'Lisa Anderson', avatar: 'https://randomuser.me/api/portraits/women/63.jpg' },
  { name: 'Michael Brown', avatar: 'https://randomuser.me/api/portraits/men/55.jpg' }
]);

const trendingTopics = ref([
  { title: '#TechNews', posts: '2.3k' },
  { title: '#Travel', posts: '1.8k' },
  { title: '#FoodLovers', posts: '1.5k' },
  { title: '#Photography', posts: '1.2k' }
]);

const addNewPost = () => {
  if (!newPostContent.value.trim()) return;
  
  posts.value.unshift({
    username: 'Jane Smith',
    avatar: 'https://randomuser.me/api/portraits/women/85.jpg',
    time: 'Just now',
    content: newPostContent.value,
    image: null,
    likes: 0,
    liked: false,
    showComments: false,
    comments: [],
    newComment: ''
  });
  
  newPostContent.value = '';
};

const toggleLike = (index) => {
  const post = posts.value[index];
  post.liked = !post.liked;
  post.likes += post.liked ? 1 : -1;
};

const addComment = (index) => {
  const post = posts.value[index];
  if (!post.newComment.trim()) return;
  
  post.comments.push({
    username: 'Jane Smith',
    avatar: 'https://randomuser.me/api/portraits/women/85.jpg',
    content: post.newComment
  });
  
  post.showComments = true;
  post.newComment = '';
};
</script>

<style>
.v-card {
  border-radius: 12px;
}
</style>