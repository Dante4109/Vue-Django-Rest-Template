"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from rest_framework import routers

from django.contrib import admin, auth
from django.urls import path, include
from backend.users import routers
from django.conf import settings, urls
from django.views.static import serve
from django.views.generic import TemplateView
from django.conf.urls.static import static
from backend.profile import routers
from backend.profile.views import (
    ProfileSetup,
    ProfilePublicListView,
    ProfilePublicView,
)

from .views import index_view

from backend.users.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .users.handlers import CustomTokenObtainPairView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin/", admin.site.urls),
    # API Backend Views
    path(
        "api/auth/obtain_token/",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("api/auth/refresh_token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include("backend.users.routers")),
    path(
        "api/email_verification/",
        UserEmailVerificationView.as_view({"post": "post"}),
        name="email_verification",
    ),
    path("api/", include("backend.profile.routers")),
    path(
        r"api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path("api/profilesetup/", ProfileSetup.as_view(), name="profile_setup"),
    path(
        "api/public/profile/<int:pk>/",
        ProfilePublicView.as_view(),
        name="profile_public",
    ),
    path(
        "api/public/profile/",
        ProfilePublicListView.as_view(),
        name="profilelist_public",
    ),
    path("api/", include("backend.image_blob.routers")),
    # Web App Views
    path("", index_view, name="index"),
    path("email_verification/<str:token>", index_view, name="user_email_verificaiton"),
    path("password_reset/<str:token>", index_view, name="user_password_reset"),
    # Demo pages
    # TO-DO make this dynamic instead of manual
    path("demo/imagemanager", index_view, name="demo_image_manager page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
