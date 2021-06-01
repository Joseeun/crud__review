from django.db import models #models이라는 클래스를 상속
from django.conf import settings
#프로젝트에서 사용하려하는 이용자를 넣기 위해 settings를 가져옴


class Post(models.Model):
    title = models.CharField(max_length=200) #models안 char필드(한줄 문자입력창)를 가져오고, 최대 길이 200으로 저장
    pub_date = models.DateField('date published') #models안 DateField를 가져옴으로서, 날짜 사용할 수 있게 만듦
    writer = models.CharField(max_length=15, default="닉네임을 입력해주세요")
    #writer는 models안 CharField을 가져오고 최대길이 15, null값을 방지하기 위해 default값인 제시문을 입력해줌으로서, 해당 제시문이 나오도록 출력
    body = models.TextField()
    #body는 models안 text필드 가져옴


    def __str__(self): #인스턴스 객체를 생성해주기 위한 메소드 
        return self.title