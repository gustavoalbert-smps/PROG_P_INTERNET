from django.shortcuts import render, redirect
from socialRede.models import *

# Create your views here.
def index(request):
	return render(request, 'index.html', {'perfis' : Perfil.objects.all()})

def convidar(request, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id = perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

def get_perfil_logado(request):
	return Perfil.objects.get(id = 1)

def exibir_perfil(request, perfil_id):
	
	perfil = Perfil.objects.get(id = perfil_id)

	return render(request, 'perfil.html', {"perfil" : perfil})

'''
def rede(request, email_u, nome_perfil, txt, txt_c, type_reaction):
	usuario = Usuario()
	perfil = Perfil()
	postagem = Postagem()
	comentarios = Comentario()
	reacao = Reacao()

	try:
		Usuario.objects.get(email = email_u)
		Perfil.objects.get(nome = nome_perfil)
		Postagem.objects.get(texto = txt)
		Comentario.objects.get(texto = txt_c)
		Reacao.objects.get(tipo = type_reaction)
	except Exception as e:
		raise TypeError("the search does not exist.")
	finally:
		usuario.email = Usuario.email
		usuario.senha = Usuario.senha
		usuario.data = Usuario.data
		
		perfil.nome = Perfil.nome
		perfil.email = Perfil.email
		perfil.telefone = Perfil.telefone
		perfil.nome_empresa = Perfil.nome_empresa
		
		postagem.texto = Postagem.texto
		postagem.data = Postagem.data

		comentarios.texto = Comentario.texto
		comentarios.data = Comentario.data

		reacao.tipo = Reacao.tipo
		reacao.data = Reacao.data

	return render(request, 'rede.html', {"perfil" : perfil}, {"usuario" : usuario}, {"postagem" : postagem}, {"comentarios" : comentarios}, {"reacao" : reacao})
	'''

