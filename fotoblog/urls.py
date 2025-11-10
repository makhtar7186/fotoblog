"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import authentication.views as auth_views
import blog.views as blog_views
from django.contrib.auth.views import LoginView, LogoutView , PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True    
    ), name="login"),
    
    path("logout/", auth_views.logout_view, name="logout"),
    path('change_password/', PasswordChangeView.as_view(
        template_name='authentication/change_password.html',
        success_url='change-password-done',
    ), name='change-password'),
    path('change_password/change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/change_password_done.html',
    ), name='change-password-done'),
    path('home/', blog_views.home, name='home'),
    path('signup/', auth_views.signup_page, name='signup'),
    path('photo/upload/', blog_views.photo_upload, name='photo_upload'),
    path('photo/upload_profile/', auth_views.upload_profile_photo, name='upload_profile_photo'),
    path('blog/create/', blog_views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>', blog_views.view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit', blog_views.edit_blog, name='edit_blog'),
    path('photos/upload_multiple/', blog_views.create_multiple_photos, name='create_multiple_photos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)