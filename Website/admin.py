from django.contrib import admin

from .models import CustomUser, CapacitacaoExterna, CapacitacaoInterna, ContatoCapacitacao, ContatoIniciativa, EmpresaParceira, Evento, EventoInstitucional, Financiamento, Iniciativa, Setor, Telefone, TipoParceria
admin.site.register(CustomUser)

admin.site.register(CapacitacaoExterna)
admin.site.register(CapacitacaoInterna)
admin.site.register(ContatoCapacitacao)
admin.site.register(ContatoIniciativa)
admin.site.register(EmpresaParceira)
admin.site.register(Evento)
admin.site.register(EventoInstitucional)
admin.site.register(Financiamento)
admin.site.register(Iniciativa)
admin.site.register(Setor)
admin.site.register(Telefone)
admin.site.register(TipoParceria)