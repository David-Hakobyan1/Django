from django.urls import path
from . import views

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('game',views.game,name='game'),
    path('calc',views.calc,name='calc'),
    path('addquest',views.Add_Quest,name='addquest'),
    path('Play_Game',views.Play_Game,name='Play_Game'),
]
