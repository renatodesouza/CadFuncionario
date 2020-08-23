from django.contrib import admin

from .models import Funcionario, Obra, Cargo, Contrato

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados Pessoais',        {'fields':('nome', 'email', 'cpf', 'rg', 'telefone', 'dt_nasc', 'estado_civil')}),
        ('Dados Internos',        {'fields':('cargo', 'obra', 'salario', 'va', 'vt')})
    ]
    
    list_display = ('nome', 'email', 'cpf', 'rg', 'telefone', 'dt_nasc', 'estado_civil', 'cargo', 'obra', 'salario', 'va', 'vt')
    
    def funcionario(self, instance):
        return f'{instance.nome.get_full_name}'
    
@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações da Obra',         {'fields':('nome', 'telefone', 'dt_inicio', 'dt_fim')}),
        ('Endereço',                    {'fields':('cidade', 'bairro', 'rua', 'numero')})
    ]
    
    list_display = ('nome', 'cidade', 'bairro', 'rua', 'numero', 'telefone', 'dt_inicio', 'dt_fim')
    
    def obra(self, instance):
        return f'{instance.nome.get_full_name}'
    
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações do Cargo',        {'fields':('nome', 'descricao')})
    ]
    
    list_display = ('nome', 'descricao')
    
    
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações do Contrato',             {'fields':('cargo', 'obra', 'funcionario', 'dt_inicio')})
    ]
    
    list_display = ('cargo', 'obra', 'funcionario', 'dt_inicio')