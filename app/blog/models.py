from django.db import models
from django.contrib.auth.models import User

#armazena opções para o campo status no modelo Post. É uma forma de criar escolhas fixas para um campo, onde: 0 representa "Draft" (Rascunho, 1 representa "Publish" (Publicado)
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    #Um campo que armazena uma versão curta e amigável do título para URLs.
    slug = models.SlugField(max_length=200, unique=True)
    #ForeignKey: Define uma relação muitos-para-um com o modelo User. on_delete=models.CASCADE: Se um usuário for deletado, todos os posts relacionados a ele também serão deletados. related_name='blog_posts': Permite acessar todos os posts de um usuário usando user.blog_posts.all().
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    #Atualiza automaticamente o campo com a data e hora atuais sempre que o post é atualizado.
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    #auto_now_add=True: Define automaticamente a data e hora no momento em que o post é criado e não muda após isso.
    created_on = models.DateTimeField(auto_now_add=True)
    #choices=STATUS: Limita as opções possíveis aos valores definidos em STATUS. default=0: Define "Draft" como o status padrão para novos posts.
    status = models.IntegerField(choices=STATUS, default=0)


    #A classe Meta define opções adicionais para o modelo: ordering = ['-created_on']: Ordena os posts por data de criação, do mais recente para o mais antigo.    
    class Meta:
        ordering = ['-created_on']
        

    def __str__(self):
        return self.title