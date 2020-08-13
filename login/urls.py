from django.urls import path
from django.views.generic import TemplateView

from . import views
#from rest_framework_swagger.views import get_swagger_view
#schema_view = get_swagger_view(title='Picture API')


urlpatterns = [
    #path(r'swagger-docs/', schema_view),
    path('user_validate/', views.user_validate, name='user_validate'),
    path('user_create/', views.create_user_, name='user_create'), 
]
