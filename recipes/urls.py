from django.urls import path
from .views import recipe_list_create, recipe_detail


urlpatterns = [
    path('recipes/', recipe_list_create, name='recipe-list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),
    path('recipes/update/<int:pk>', recipe_detail, name='recipe_detail'),

    
]

