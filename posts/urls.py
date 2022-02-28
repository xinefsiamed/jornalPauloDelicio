from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>',
         views.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
    path('post/escrever', login_required(views.Escrever.as_view()), name='post_escrever')

]
