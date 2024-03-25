"""
URL configuration for restaurantProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphene_django_cruddals.views.cruddals_views import CRUDDALSView
# from restaurantProject.schema import schema
from menu.schema import schema

urlpatterns = (
    [
        path('admin/', admin.site.urls),
        path('_nested_admin/', include('nested_admin.urls')),
        path("graphql/", csrf_exempt(CRUDDALSView.as_view(graphiql=True, schema=schema, generate_cruddals_files_client=True))),
    ] 
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)