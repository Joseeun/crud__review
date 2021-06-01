from django.contrib import admin
from django.urls import path
import crudApp.views

urlpatterns = [ #다음과 같이 urlpatterns 안에 어떠한 url이 들어가면 views 에서 함수가 실행되도록 한다
    path('admin/', admin.site.urls),
    path('', crudApp.views.main, name='main'), #views에 main적용, 이름은 main
    path('detail/<str:id>', crudApp.views.detail, name='detail'), #특정 게시물을 가져와야하기 때문에 id 지정 필요, views에 detail적용, 이름은 detail
    path('read/', crudApp.views.read, name = 'read'), #views에 read적용, 이름은 read
    path('new/create/', crudApp.views.create, name='create'), #views에 creat적용, 이름은 create
    path('edit/<str:id>', crudApp.views.edit, name='edit'),  #특정 게시물을 가져와야하기 때문에 id 지정 필요, views에 edit적용, 이름은 edit
    path('delete/<str:id>/', crudApp.views.delete, name = 'delete'), #특정 게시물을 가져와야하기 때문에 id 지정 필요, views에 delete적용, 이름은 edit
]
