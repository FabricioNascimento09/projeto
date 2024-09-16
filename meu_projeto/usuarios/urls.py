from django.urls import path  # Importa 'path' para mapear URLs para as views
from . import views  # Importa o arquivo 'views.py' do diretório atual (app)

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),  # Mapeia a URL 'cadastro/' para a view 'cadastro'
    path('login/', views.login_view, name='login'),  # Mapeia a URL 'login/' para a view 'login_view'
    path('plataforma/', views.plataforma, name='plataforma')  # Mapeia a URL 'plataforma/' para a view 'plataforma'
]
