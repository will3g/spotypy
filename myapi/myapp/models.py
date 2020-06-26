from django.db import models

class Music(models.Model):

    class Meta:
        db_table = 'music'
    
    title = models.CharField(max_length=200)
    seconds = models.IntegerField()
    album = models.ForeignKey(
        'Album',
        related_name='musics',
        on_delete=models.CASCADE,
        default='unknown'
    )

    def __str__(self):
        return self.title


class Album(models.Model):

    class Meta:
        db_table = 'album'

    title = models.CharField(max_length=200)
    band = models.ForeignKey(
        'Band',
        related_name='albuns',
        on_delete=models.CASCADE
    )
    date = models.DateField()


class Band(models.Model):

    class Meta:
        db_table = 'band'

    name = models.CharField(max_length=200)


class Member(models.Model):

    class Meta:
        db_table = 'member'

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    band = models.ForeignKey(
        'Band',
        related_name='members',
        on_delete=models.CASCADE
    )


##### LEMBRETES ######################################################################
# CASCADE: Quando o objeto referenciado for excluído, exclua também os objetos que têm referências 
# a ele (quando você remove uma postagem de blog, por exemplo, também pode excluir comentários). SQL equivalentes: CASCADE.

# PROTECT: Proíbe a exclusão do objeto referenciado. Para excluí-lo, você terá que excluir 
# todos os objetos que o referenciam manualmente. SQL equivalentes: RESTRICT.

# SET_NULL: Defina a referência como NULL (requer que o campo seja anulável). Por exemplo, quando você 
# exclui um Usuário, pode manter os comentários que ele publicou nas postagens do blog, mas diz que 
# foram publicados por um usuário anônimo (ou excluído). SQL equivalentes: SET NULL.

# SET_DEFAULT: Defina o valor padrão. SQL equivalentes: SET DEFAULT.

# SET(...): Defina um determinado valor. Este não faz parte do padrão SQL e é inteiramente tratado pelo Django.

# DO_NOTHING: Provavelmente, é uma péssima idéia, pois isso criaria problemas de integridade no banco de 
# dados (referenciando um objeto que realmente não existe). SQL equivalentes: NO ACTION.
##### LEMBRETES ######################################################################