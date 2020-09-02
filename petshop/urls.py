"""petshop URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView



class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


API_TITLE = 'Pet shop'  # new
API_DESCRIPTION = 'Моя документация'

schema_view1 = get_schema_view(title=API_TITLE)

schema_view = get_swagger_view(title=API_TITLE)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('accounts/', include('allauth.urls')),
    # path('accounts/google/login/', include('allauth.urls')),


    path('api/v1/', include('backend.userprofile.urls')),


    path('schema/', schema_view1),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),

    path('swagger-docs/', schema_view),

    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login')

]
