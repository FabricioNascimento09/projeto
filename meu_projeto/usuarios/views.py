from django.shortcuts import render  # Importa o método 'render' para exibir templates HTML
from django.http import HttpResponse  # Importa 'HttpResponse' para enviar respostas HTTP simples
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django
from django.contrib.auth import authenticate, login as auth_login  # Importa funções para autenticar e logar usuários

# Função para o cadastro de usuários
def cadastro(request):
    if request.method == 'GET':  # Se for uma requisição GET, exibe a página de cadastro
        return render(request, 'cadastro.html')
    else:  # Se for uma requisição POST, processa o cadastro
        username = request.POST.get('username')  # Obtém o valor do campo 'username' do formulário
        email = request.POST.get('email')  # Obtém o valor do campo 'email' do formulário
        senha = request.POST.get('senha')  # Obtém o valor do campo 'senha' do formulário

        # Verifica se já existe um usuário com o mesmo username
        if User.objects.filter(username=username).exists():
            return HttpResponse('Já existe um usuário com esse username')

        # Cria um novo usuário com os dados recebidos
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()  # Salva o usuário no banco de dados

        return HttpResponse('Usuário cadastrado com sucesso!')

# Função para login de usuários
def login_view(request):
    if request.method == 'GET':  # Se for uma requisição GET, exibe a página de login
        return render(request, 'login.html')
    else:  # Se for uma requisição POST, processa o login
        username = request.POST.get('username')  # Obtém o valor do campo 'username' do formulário
        senha = request.POST.get('senha')  # Obtém o valor do campo 'senha' do formulário

        # Autentica o usuário com base no username e senha
        user = authenticate(username=username, password=senha)

        if user:  # Se a autenticação for bem-sucedida
            auth_login(request, user)  # Faz o login do usuário
            return HttpResponse('Autenticado com sucesso')
        else:  # Se a autenticação falhar
            return HttpResponse('Email ou senha inválidos')

# Função que exibe a plataforma, disponível apenas para usuários autenticados
def plataforma(request):
    if request.user.is_authenticated:  # Verifica se o usuário está autenticado
        return HttpResponse('Bem-vindo à nossa plataforma!')
    return HttpResponse('Você precisa estar logado')  # Resposta para usuários não autenticados

# Função que exibe a página inicial
def home(request):
    return render(request, 'home.html')  # Renderiza a página 'home.html'
