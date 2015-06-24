from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homeView, name='home'),
    url(r'^AtualizarPerfil$', views.atualizarPerfilView, name='atualizarPerfil'),
    url(r'^CadastrarMembro$', views.cadastrarMembroView, name='CadastrarMembro'),
    url(r'^ConsultarMembro$', views.ConsultarMembroView, name='ConsultarMembro'),
    url(r'^Perfil$', views.perfilView, name='perfil'),
    url(r'^CapacitacaoInterna$', views.CapacitacaoInternaView, name='CapacitacaoInterna'),
    url(r'^CapacitacaoExterna$', views.CapacitacaoExternaView, name='CapacitacaoExterna'),
    url(r'^ContatoCapacitacao$', views.ContatoCapacitacaoView, name='ContatoCapacitacao'),
    url(r'^ContatoIniciativa$', views.ContatoIniciativaView, name='ContatoIniciativa'),
    url(r'^EmpresaParceira$', views.EmpresaParceiraView, name='EmpresaParceira'),
    url(r'^CadastrarEmpresa$', views.CadastrarEmpresaView, name='CadastrarEmpresa'),
    url(r'^ConsultarEmpresa$', views.ConsultarEmpresaView, name='ConsultarEmpresa'),
    url(r'^Evento$', views.EventoView, name='Evento'),
    url(r'^CadastrarEvento$', views.CadastrarEventoView, name='CadastrarEvento'),
    url(r'^ConsultarEvento$', views.ConsultarEventoView, name='ConsultarEvento'),
    url(r'^EventoInstitucional$', views.EventoInstitucionalView, name='EventoInstitucional'),
    url(r'^CadastrarFinanciamento$', views.CadastrarFinanciamentoView, name='CadastrarFinanciamento'),
    url(r'^ConsultarFinanciamento$', views.ConsultarFinanciamentoView, name='ConsultarFinanciamento'),
    url(r'^RemoverFinanciamento$', views.RemoverFinanciamentoView, name='RemoverFinanciamento'),
    url(r'^Financiamento$', views.FinanciamentoView, name='Financiamento'),
    url(r'^EditarFinanciamento$', views.EditarFinanciamentoView, name='EditarFinanciamento'),
    url(r'^Iniciativa$', views.IniciativaView, name='Iniciativa'),
    url(r'^CadastrarIniciativa$', views.CadastrarIniciativaView, name='CadastrarIniciativa'),
    url(r'^ConsultarIniciativa$', views.ConsultarIniciativaView, name='ConsultarIniciativa'),
    url(r'^EditarIniciativa$', views.EditarIniciativaView, name='EditarIniciativa'),
    url(r'^Setor$', views.SetorView, name='Setor'),
    url(r'^CadastrarSetor$', views.CadastrarSetorView, name='CadastrarSetor'),
    url(r'^RemoverSetor$', views.RemoverSetorView, name='RemoverSetor'),
    url(r'^Telefone$', views.TelefoneView, name='Telefone'),
    url(r'^TipoParceria$', views.TipoParceriaView, name='TipoParceria'),
    url(r'^Login$', views.LoginView, name='Login'),
    url(r'^Logout$', views.LogoutView, name='Logout')
]