from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.name = None
    '''

    def __str__(self):
        return f'{self.user.username} Profile'
    '''
    def redimensiona_imagem(imagem, max_width=300, max_height=300):
        #abrindo imagem
        img = Image.open(imagem)

        #redimensionando imagem
        img.thumbnail((max_width, max_height), Image.ANTIALIAS)

        #Criando um buffer de memória para salvar a imagem redimensionada
        buffer = BytesIO()
        img.save(buffer, format='JPEG')

        #Criando um arquivo de memoria temporaria com o buffer e dando mesmo nome do original
        arquivo_imagem = ContentFile(buffer.getvalue())
        arquivo_imagem.name = imagem.name

        return arquivo_imagem


        def save(self,*args, **kwargs):
            if self.image:
                imagem_redimensionada = self.redimensiona_imagem(imagem)
                self.image = imagem_redimensionada

            super().save(*args, kwargs)
    '''



