from django.db import models

# Create your models here.
opcoes = [
    ('Gasto', 'Gasto'),
    ('Receita', 'Receita'),
]
class Cadastro(models.Model):
    data = models.DateField()
    responsavel = models.CharField(max_length=50)
    descricao = models.TextField()
    tipo = models.CharField(max_length=7,choices=opcoes)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    comprovante = models.ImageField(upload_to="comprovante", null=True, blank=True)

    def __str__(self):
        return self.descricao

opcoes_contato = [
    ('consulta', 'consulta'),
    ('reclamacao', 'reclamação'),
    ('sugestao', 'sugestão'),
    ('felicitacoes', 'felicitações'),
    ('outro', 'outro')
]
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_consulta = models.CharField(max_length=12,choices=opcoes_contato)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome
    