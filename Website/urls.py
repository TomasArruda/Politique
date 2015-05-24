from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^Membro$', views.MembroView, name='Membro'),
    url(r'^CapacitacaoInterna$', views.CapacitacaoInternaView, name='CapacitacaoInterna'),
    url(r'^CapacitacaoExterna$', views.CapacitacaoExternaView, name='CapacitacaoExterna'),
    url(r'^ContatoCapacitacao$', views.ContatoCapacitacaoView, name='ContatoCapacitacao'),
    url(r'^ContatoIniciativa$', views.ContatoIniciativaView, name='ContatoIniciativa'),
    url(r'^EmpresaParceira$', views.EmpresaParceiraView, name='EmpresaParceira'),
    url(r'^Evento$', views.EventoView, name='Evento'),
    url(r'^EventoInstitucional$', views.EventoInstitucionalView, name='EventoInstitucional'),
    url(r'^Financiamento$', views.FinanciamentoView, name='Financiamento'),
    url(r'^Iniciativa$', views.IniciativaView, name='Iniciativa'),
    url(r'^Setor$', views.SetorView, name='Setor'),
    url(r'^Telefone$', views.TelefoneView, name='Telefone'),
    url(r'^TipoParceria$', views.TipoParceriaView, name='TipoParceria'),

]