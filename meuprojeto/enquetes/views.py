from django.shortcuts import render
from enquetes.models import Enquete

# Create your views here.
def bemvindo(request):
	return render(request, 'bemvindo.html')

def exibir(request, enquete_id):
	enquete = Enquete()

	try:
		Enquete.objects.get(id = enquete_id)
	except Enquete.DoesNotExists:
		pass
	finally:
		enquete_db = Enquete.objects.get(id = enquete_id)
		enquete.texto = enquete_db.texto
		enquete.data_publicacao = enquete_db.data_publicacao


	return render(request, 'enquetes.html', { "enquete" : enquete})