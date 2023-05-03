"""
URL configuration for use_DRF project.

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

from use_DRF.shema_api import schema_view
from women.routers import MyCustomRouter
from women.views import *
from rest_framework import routers

router = MyCustomRouter()
# router = routers.DefaultRouter()
router.register(r'women', WomenViewSet, basename='women')
print(router.urls)

"""
     Через include добавляются все маршруты, которые были возможны во ViewSet, 
    благодаря router и вместо нескольких урлов записывается один
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

    path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update', 'get': 'retrieve'})),
]
