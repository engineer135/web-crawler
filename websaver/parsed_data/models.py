from django.db import models

# Create your models here.
class BlogData(models.Model) :
    title = models.CharField(max_length=200)
    link = models.URLField()

    #아래 함수를 추갛면서 models.py 파일을 수정했지만 DB에 반영되는 사항이 아니기 때문에  
    #makemigrations 나  migrate 를 해줄 필요가 없습니다. 오호.. 그렇군...!
    def __str__(self):
        return self.title