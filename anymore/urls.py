from django.urls import path, include
from .views import CustomRegisterView

urlpatterns = [
    # dj-rest-auth 기본 제공 API
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', CustomRegisterView.as_view(), name='custom_registration'),
    path('accounts/', include('allauth.urls')),  # django-allauth 경로 (소셜 로그인 지원)
]
