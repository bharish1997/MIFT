from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from jobsapp.views import *

from .views import *

app_name = "accounts"

urlpatterns = [
    path('user/register', RegisterUserView.as_view(), name='user-register'),
    path('ngo/register', RegisterNgoView.as_view(), name='ngo-register'),
    path('user/profile/update', EditProfileView.as_view(), name='user-profile-update'),
    path('ngo/profile/update', NgoEditProfileView.as_view(), name='ngo-profile-update'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
