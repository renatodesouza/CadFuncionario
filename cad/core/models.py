from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=255)
    telefone = models.IntegerField('Telefone')
    cpf = models.CharField('CPF', max_length=255)
    rg = models.CharField('RG', max_length=255)
    email = models.EmailField('E-mail', max_length=255)
    dt_nasc = models.DateField()
    
class Funcionario(Pessoa):
    SOLTEIRO = 'Solteiro'
    CASADO = 'Casado'
    VIUVO = 'Viuvo'
    
    escolha_estado_civil = [(SOLTEIRO, 'Solteiro'), (CASADO, 'Casado'), (VIUVO, 'Viuvo')]
    
    cargo = models.ForeignKey('Cargo', on_delete=models.PROTECT, related_name='cargo_funcionario')
    obra = models.ForeignKey('Obra', on_delete=models.PROTECT, related_name='obra_funcionario')
    estado_civil = models.CharField('Estado Civil', max_length=10, choices=escolha_estado_civil)
    salario = models.FloatField('Salario')
    va = models.FloatField('Vale alimentação')
    vt = models.FloatField('Vale transporte')
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        
    def __str__(self):
        return self.nome
    
    
        
class Cargo(models.Model):
    nome = models.CharField('Nome', max_length=255)
    descricao = models.TextField('Descricão', blank=True)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        
    def __str__(self):
        return self.nome
    
    
class Obra(models.Model):
    nome = models.CharField('Nome', max_length=255)
    cidade = models.CharField('Cidade', max_length=255)
    bairro = models.CharField('Bairro', max_length=255)
    rua = models.CharField('Rua', max_length=255)
    numero = models.IntegerField('Numero')
    telefone = models.CharField('Telefone', max_length=255)
    dt_inicio = models.DateTimeField('Data de Inicio')
    dt_fim = models.DateTimeField('Data Final', blank=True)
    
    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        
    def __str__(self):
        return self.nome
    
class Contrato(models.Model):
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE, related_name='cargo_contrato')
    obra = models.ForeignKey('Obra', blank=True, on_delete=models.CASCADE, related_name='obra_contrato')
    funcionario = models.ForeignKey('Funcionario', on_delete=models.CASCADE, related_name='funcionario_contrato')
    dt_inicio = models.DateTimeField('Data de inicio')
        
    
    
