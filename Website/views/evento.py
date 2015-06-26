from django.http import HttpResponse
from django.shortcuts import render
from Website.models import Evento, CapacitacaoInterna, CapacitacaoExterna, EventoInstitucional
from Website.forms import CapacitacaoInternaForm
from Website.forms import CapacitacaoExternaForm
from Website.forms import EventoInstitucionalForm
from Website.forms import EventoForm
from django.core import serializers
from django.contrib.auth.decorators import login_required

def EventoView(request):
    #query = Evento.objects.order_by('nome')
    #context = RequestContext(request, {'latest_question_list': latest_question_list,})
    return render(request, '/membros.html')

@login_required(login_url='/Website')
def CadastrarEventoView(request):

	if request.method == 'POST':

		auxForm = EventoForm(request.POST)
		
		if auxForm.is_valid():

			tipo = auxForm.cleaned_data['tipoEvento']

			if tipo == "1":

				form = CapacitacaoInternaForm(request.POST or None)

			elif tipo == "2":

				form = CapacitacaoExternaForm(request.POST or None)

			elif tipo == "3":

				form = EventoInstitucionalForm(request.POST or None)

			else:

				form = Evento(request.POST or None)

			if form.is_valid():
				form.save()

		else:
			form = Evento(None)

	else:
		form = Evento(None)
		
	return render(request, 'cadastrarEvento.html', {"form":form})

@login_required(login_url='/Website')
def EditarEventoView(request, id):
	if request.method == 'POST':

		auxForm = EventoForm(request.POST)
		
		if auxForm.is_valid():

			tipo = auxForm.cleaned_data['tipoEvento']

			if tipo == "1":
				form = CapacitacaoInternaForm(request.POST or None)
				obj = CapacitacaoInterna.objects.get(pk=id)

				if form.is_valid():
					obj.nome = form.cleaned_data['nome'] 
					obj.data = form.cleaned_data['data']
					obj.feedback = form.cleaned_data['feedback']

					obj.material = form.cleaned_data['material'] 
					obj.save()

				eventos = serializers.serialize( "python", CapacitacaoInterna.objects.filter().order_by('nome') )

			elif tipo == "2":
				form = CapacitacaoExternaForm(request.POST or None)
				obj = CapacitacaoExterna.objects.get(pk=id)

				if form.is_valid():
					obj.nome = form.cleaned_data['nome'] 
					obj.data = form.cleaned_data['data']
					obj.feedback = form.cleaned_data['feedback']

					obj.custo = form.cleaned_data['custo'] 
					obj.palestrante = form.cleaned_data['palestrante'] 
					obj.save()

				eventos = serializers.serialize( "python", CapacitacaoExterna.objects.filter().order_by('nome') )

			elif tipo == "3":
				form = EventoInstitucionalForm(request.POST or None)
				obj = EventoInstitucional.objects.get(pk=id)

				if form.is_valid():
					obj.nome = form.cleaned_data['nome'] 
					obj.data = form.cleaned_data['data']
					obj.feedback = form.cleaned_data['feedback']

					obj.custo = form.cleaned_data['custo'] 
					obj.motivoPatrocinio = form.cleaned_data['motivoPatrocinio'] 
					obj.empresasParceiras = form.empresasParceiras['custo'] 
					obj.save()

				eventos = serializers.serialize( "python", EventoInstitucional.objects.filter().order_by('nome') )
			else:

				form = Evento(request.POST or None)

			if form.is_valid():
				form.save()

		else:
			form = Evento(None)

	else:
		form = Evento(None)

	return render(request, 'consultarFianaciamento.html', {'eventos': eventos, 'form': form})


@login_required(login_url='/Website')
def ConsultarEventoView(request):

	form = EventoForm(None)
	eventos1 = serializers.serialize( "python", CapacitacaoInterna.objects.filter().order_by('nome'))

	eventos2 = serializers.serialize( "python", CapacitacaoExterna.objects.filter().order_by('nome'))

	eventos3 = serializers.serialize( "python", EventoInstitucional.objects.filter().order_by('nome'))

	return render(request, 'consultarEvento.html', {'eventos1': eventos1, 'eventos2':eventos2, 'eventos3':eventos3, 'form':form})

@login_required(login_url='/Website')
def RemoverEventoView(request, id):
    obj = Evento.objects.get(pk=id)
    obj.delete()
    return render(request, 'consultarEvento.html')
