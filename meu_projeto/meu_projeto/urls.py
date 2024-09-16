from django.contrib import admin  # Importa o módulo admin do Django para usar a interface administrativa
from django.urls import path, include  # Importa 'path' para mapear URLs e 'include' para incluir outras URLs
from usuarios import views  # Importa o arquivo 'views.py' do app 'usuarios'

urlpatterns = [
    path('admin/', admin.site.urls),  # Define a URL para a interface administrativa do Django
    path('auth/', include('usuarios.urls')),  # Inclui as URLs definidas no app 'usuarios' dentro de 'usuarios/urls.py'
    path('', views.home, name='home'),  # Define a URL para a página inicial, que será atendida pela view 'home'
]
