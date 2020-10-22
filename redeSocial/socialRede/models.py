from django.db import models

# Create your models here.
class Usuario(models.Model):
	email = models.EmailField(max_length = 255)
	senha = models.CharField(max_length = 255)
	#perfil = models.ForeignKey("Perfil", on_delete = models.CASCADE, related_name ='perfis')
	data_nascimento = models.DateField()


class Perfil(models.Model):
	nome = models.CharField(max_length = 255, null = False)
	email = models.CharField(max_length = 255, null = False)
	telefone = models.CharField(max_length = 15, null = False)
	nome_empresa = models.CharField(max_length = 255, null = False)
	usuario = models.OneToOneField(Usuario, related_name = 'perfil_usuario', on_delete = models.CASCADE)
	contatos = models.ManyToManyField('self')
	#timeline = models.ForeignKey("Postagem", on_delete = models.CASCADE, related_name = 'postagens')
	
	def convidar(self, perfil_convidado): 
		convite = Convite(solicitante = self,convidado = perfil_convidado) 
		convite.save()

class Postagem(models.Model):
	texto = models.CharField(max_length = 255)
	data = models.DateField()
	perfil = models.OneToOneField(Perfil, related_name = 'perfil_postagem', on_delete = models.CASCADE)
	#comentarios = models.ForeignKey("Comentario", on_delete = models.CASCADE, related_name = 'comentarios')
	#reacoes = models.ForeignKey("Reacao", on_delete = models.CASCADE, related_name = 'reações')


class Comentario(models.Model):
	texto = models.CharField(max_length = 255)
	data = models.DateField()
	perfil = models.OneToOneField(Perfil, related_name = 'comentario_perfil', on_delete = models.CASCADE)
	postagem = models.OneToOneField(Postagem, related_name = 'postagem_comentario', on_delete = models.CASCADE)


class Reacao(models.Model):
	TYPES_REACTIONS = (
		("C", "CURTIR"),
		("A", "AMEI"),
		("R", "RISOS"),
		("G", "GRRR"),
		("B", "RUIM")
	)
	tipo = models.CharField(max_length = 1, choices = TYPES_REACTIONS)
	data = models.DateField()
	postagem = models.OneToOneField(Postagem, related_name = 'postagem_reacao', on_delete = models.CASCADE)
	perfil = models.OneToOneField(Perfil, related_name = 'perfil_comentario', on_delete = models.CASCADE)
	peso = models.IntegerField()
	if tipo == 'CURTIR':
		peso = 5
	elif tipo == 'AMEI':
		peso = 4
	elif tipo == 'RISOS':
		peso = 3
	elif tipo == 'GRRR':
		peso = 2
	elif tipo == 'RUIM':
		peso = 1

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, related_name = 'convites_feitos', on_delete = models.CASCADE)
	convidado = models.ForeignKey(Perfil, related_name = 'convites_recebidos', on_delete = models.CASCADE)

	def aceitar(self):
		self.convidado.contatos.add(self.solicitante)
		self.solicitante.contatos.add(self.convidado)
		self.delete()