# VDRF Template Documentation

## Overview

**VDRF** (Vue Django Rest Framework) is a full-stack web application template built with modern tools and best practices. It combines a Vue.js 3 frontend with a Django Rest Framework backend, providing a complete foundation for developing web applications with authentication, user management, and demo pages.

This template is designed to help developers quickly scaffold new projects without repeating boilerplate setup for authentication, API integration, and component architecture.

---

## Project Architecture

### Frontend (Vue.js 3 + Vite)

The frontend is a single-page application (SPA) built with Vue.js 3, using Vite as the build tool for fast development and optimized production builds.

**Key Frontend Technologies:**
- **Vue 3** - Modern reactive UI framework
- **Vite** - Next-generation frontend build tool
- **Vuetify** - Material Design component library
- **Vue Router** - Client-side routing
- **Vuex** - State management
- **Axios** - HTTP client for API communication
- **Sass** - CSS preprocessing

**Frontend Structure:**
```
src/
├── pages/           # Page components (views)
├── components/      # Reusable Vue components
├── layouts/         # Layout wrapper components
├── router/          # Route configuration
├── stores/          # State management (Vuex)
├── services/        # API service modules
├── composables/     # Reusable Vue 3 composables
├── plugins/         # Vue plugins (Vuetify, Router, etc.)
├── assets/          # Images and static assets
├── styles/          # Global stylesheets
├── utilities/       # Helper functions
├── App.vue          # Root app component
└── main.js          # Entry point
```

### Backend (Django + Django Rest Framework)

The backend is a Django application providing REST API endpoints for authentication, user management, and data operations.

**Key Backend Technologies:**
- **Django** - Web framework
- **Django Rest Framework** - REST API toolkit
- **Django CORS** - Cross-origin resource sharing
- **Python** - Server-side logic

**Backend Structure:**
```
backend/
├── users/           # User authentication and profiles
├── profile/         # User profile management
├── image_blob/      # Image storage handling
├── settings/        # Django settings configuration
├── docs/            # Backend documentation
├── tests/           # Unit tests
├── urls.py          # URL routing
├── views.py         # Global view logic
├── wsgi.py          # WSGI entry point
├── asgi.py          # ASGI entry point
└── cors.py          # CORS configuration
```

---

## Getting Started

### Prerequisites

- **Node.js** (v16+) - For frontend development
- **Python** (v3.8+) - For backend development
- **pip** - Python package manager
- **npm** - Node package manager
- **Git** - Version control

### Installation

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd VDRF_Template
```

#### 2. Frontend Setup
```bash
npm install
```

#### 3. Backend Setup
```bash
pip install -r requirements-dev.txt
```

#### 4. Create Environment Variables
Copy `.env_other` to `.env` and configure:
```bash
SITE_URL=http://localhost:5173  # Frontend URL
```

---

## Running the Application

### Development Mode

Run both frontend and backend servers concurrently:

```bash
make dev_live
```

This command:
- Starts the **Vite dev server** on `http://localhost:5173`
- Starts the **Django dev server** on `http://localhost:8000`

**Alternatively, run servers separately:**

**Frontend (Vue.js):**
```bash
npm run dev
# Access at http://localhost:5173
```

**Backend (Django):**
```bash
python manage.py runserver
# Access at http://localhost:8000/api
```

### Production Build

Build the frontend for production:
```bash
npm run build
```

Output is in the `dist/` directory.

---

## Key Features

### Built-In Features

✅ **User Authentication**
- Login/Sign up
- JWT token-based authentication
- Secure password hashing with bcrypt
- Session management with cookies

✅ **Account Management**
- Forgot Password & Password Reset
- Email Verification
- User Profile Management
- User Panel with settings

✅ **UI Components**
- Slide-out user panel
- Responsive navigation
- Material Design components via Vuetify

### Demo Pages

The template includes demo pages showcasing framework capabilities:
- **Image Manager** (`/demo/Photos`) - Image upload and management
- **CSV Importer** (`/demo/Data`) - Import CSV data
- **File Tree** (`/demo/Files`) - Hierarchical file browsing
- **Meme Maker** (`/demo/Art`) - HTML5 Canvas drawing
- **News Feed** (`/demo/News`) - Social network style feed

---

## API Communication

### Service Layer

API requests are handled through service modules in `src/services/`. These services:
- Encapsulate API endpoints
- Handle request/response formatting
- Manage authentication headers
- Provide error handling

### Making API Calls

Example service module:
```javascript
// src/services/userService.js
import axios from 'axios'

const API_BASE_URL = `${process.env.SITE_URL}/api`

export default {
  getUser(userId) {
    return axios.get(`${API_BASE_URL}/users/${userId}/`)
  },
  updateUser(userId, data) {
    return axios.put(`${API_BASE_URL}/users/${userId}/`, data)
  }
}
```

Use in components:
```javascript
import userService from '@/services/userService'

export default {
  methods: {
    async loadUser() {
      const response = await userService.getUser(1)
      this.user = response.data
    }
  }
}
```

---

## State Management (Vuex)

Global application state is managed with Vuex, located in `src/stores/vuex.js`.

### Store State Structure
```javascript
store.state = {
  authenticatedUser: {},    // Current logged-in user
  isAuthenticated: false,   // Login status
  // ... other global state
}
```

### Accessing State in Components
```javascript
import store from '@/stores/vuex'

// In component
computed: {
  user() {
    return JSON.parse(store.state.authenticatedUser)
  }
}
```

### Actions
Common store actions:
- `login(credentials)` - Authenticate user
- `logout()` - Clear session
- `updateUser(data)` - Update user profile

---

## Routing

Routes are defined in `src/router/index.js`. The router uses Vue Router v4 with path-based routing.

### Route Examples

| Path | Component | Protected | Purpose |
|------|-----------|-----------|---------|
| `/` | Home.vue | No | Landing page |
| `/dashboard` | Dashboard.vue | **Yes** | User dashboard |
| `/email_verification/:token` | Email_Verification.vue | No | Verify email |
| `/password_reset/:token` | Password_Reset.vue | No | Reset password |
| `/demo/Photos` | image_manager.vue | No | Demo: Image gallery |
| `/demo/Data` | csv_import.vue | No | Demo: CSV import |

### Protected Routes

Routes can require authentication:
```javascript
{
  path: '/dashboard',
  name: 'dashboard',
  component: Dashboard,
  beforeEnter: (to, from, next) => {
    const user = JSON.parse(store.state.authenticatedUser)
    if (user) {
      next()
    } else {
      next('/')  // Redirect to home
    }
  }
}
```

---

## Development Commands

### NPM Scripts

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start dev server (Vite) |
| `npm run prod` | Start production server |
| `npm run dev_host` | Start dev server on all interfaces (port 3000) |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint and fix issues |
| `npm run test` | Run tests |

### Make Commands

| Command | Purpose |
|---------|---------|
| `make help` | Show available commands |
| `make test` | Run backend unit tests |
| `make flake8` | Run Python linting |
| `make coverage` | Generate code coverage report |
| `make test-all` | Run linting + tests + coverage |
| `make commit msg="message"` | Stage and commit changes |
| `make push` | Run tests and push to remote |
| `make docs` | Generate Sphinx documentation |
| `make dev_live` | Start both servers concurrently |

---

## Project Configuration

### Frontend Configuration

**vite.config.mjs** - Vite build configuration
- Plugin configuration (Vue, Vuetify, auto-imports)
- Development server settings
- Build optimization

**jsconfig.json** - JavaScript path aliases
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

**eslintrc.js** - Code linting rules for Vue and JavaScript

### Backend Configuration

**backend/settings/dev.py** - Development-specific settings
- Database configuration
- Debug settings
- CORS configuration
- Static file serving

**.env** - Environment variables
- `SITE_URL` - Frontend URL for CORS
- Database credentials
- Secret keys

---

## Adding New Features

### Adding a New API Endpoint

1. **Create backend view** in `backend/views.py` or create an app-specific view file
2. **Register URL route** in `backend/urls.py`
3. **Create frontend service** in `src/services/`
4. **Use in component** via the service

### Creating a New Page

1. **Create page component** in `src/pages/YourPage.vue`
2. **Add route** in `src/router/index.js`
3. **Add to navigation** if needed in layout/navbar

### Creating a Reusable Component

1. **Create component** in `src/components/`
2. **Document props and events**
3. **Use in pages** via imports or auto-import

---

## Building & Deployment

### Production Build

```bash
npm run build
```

The output is in the `dist/` directory with optimized, minified code.

### Serve Production Build

```bash
npm run preview
```

### Backend Deployment

The Django app is deployed as a standard Django application:
```bash
python manage.py collectstatic   # Collect static files
gunicorn backend.wsgi:application  # Run with Gunicorn
```

---

## Troubleshooting

### Port Already in Use

If port 8000 (Django) or 5173 (Vite) is in use:

**Change Vite port:**
```bash
npm run dev -- --port 3001
```

**Change Django port:**
```bash
python manage.py runserver 8001
```

### CORS Errors

Check `.env` `SITE_URL` matches your frontend URL.

Update `backend/cors.py` if needed:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
]
```

### Module Not Found Errors

Reinstall dependencies:
```bash
npm install
pip install -r requirements-dev.txt
```

---

## Testing

### Frontend Tests
```bash
npm run test
```

### Backend Tests
```bash
python test.py
# or
make test
```

### Code Coverage
```bash
make coverage
```

---

## Additional Resources

- [Vue 3 Documentation](https://vuejs.org/)
- [Vite Documentation](https://vitejs.dev/)
- [Vuetify Components](https://vuetifyjs.com/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Vue Router](https://router.vuejs.org/)
- [Vuex Store](https://vuex.vuejs.org/)

---

## License

See LICENSE file for details.

---

## Support

For issues, questions, or contributions, please refer to the project's GitHub repository.
