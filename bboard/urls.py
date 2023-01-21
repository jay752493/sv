from django.urls import path, include
from .views import index, by_rubric, create, detail, edit


urlpatterns = [
    path('<int:rubric_pk>/<int:pk>/edit/', edit, name='edit'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', create, name='add'),
    path('', index, name='index'),
]
