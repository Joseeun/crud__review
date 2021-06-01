from .forms import PostForm #forms에서 PostForm 가져옴
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post #models에서 Post 가져옴
from django.utils import timezone 
#시간을 사용하기 위해 django.utils로 부터 timezone 넣어줌


#메인페이지
def main(request):
    return render(request, 'crudApp/main.html') #홈페이지 들어가자마자 보일 페이지 main.html 요청

#글쓰기페이지
def create(request): #creat함수
    if request.method =='POST': #request의 method확인
        form = PostForm(request.POST) #form의 입력값이 'Post'인지 검사
        if form.is_valid(): #post로 요청받은 것이 form이 유효하다면
            form = form.save(commit=False) #commit=False는 데이터베이스에 당장 저장하지 않음
            form.pub_date = timezone.now() #현재 시간을 불러오기 위해 timezone.now()사용
            form.save() #저장 함수 불러옴
            return redirect('read') #맞으면 read로 보냄
    else: #request의 method확인이 되지 않는다면
        form = PostForm #폼 다시 입력
        return render(request, 'crudApp/new.html',{'form':form})  #new.html요청함으로서 글 작성

#글쓰기 함수
def create(request): #글쓰기 페이지와 주석 동일
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form. save()
            return redirect('read') 

    else:
        form = PostForm #글쓰기 페이지와 주석 동일
        return render(request, 'crudApp/new.html', {'form':form})




#읽기페이지
def read(request): #read 함수
    posts = Post.objects #post의 객체들을 posts라는 변수에 담아줌
    return render(request, 'crudApp/read.html',{'posts':posts}) #변수에 담아준것을 html에서는 'posts'라고 표현

#디테일페이지
def detail(request,id): #지정한 id값 요청받는 detail함수
    post = get_object_or_404(Post,id=id) #Post model의 id값을 가져오는 변수의 이름은 post, post 모델에서 id값을 post에서 제대로 가져오지 못하면 404에러 발생 
    return render(request, 'crudApp/detail.html',{'post':post}) # detail.html 요청

#수정페이지
def edit(request): #request함수
    return render(request, 'crudApp/edit.html') #edit.html 요청

#수정 함수
def edit(request,id): #지정한 id값 요청받는 request함수
    post = get_object_or_404(Post,id=id) #Post model의 id값을 가져오는 변수의 이름은 post, post 모델에서 id값을 post에서 제대로 가져오지 못하면 404에러 발생
    if request.method == "POST": #post 메소드 확인
        form = PostForm(request.POST, instance=post) # 수정할 글의 id를 설명해주기 위해 instance 코드 사용
        if form.is_valid(): #form이 유효하다면
            form.save(commit=False) #commit=False는 데이터베이스에 당장 저장하지 않음
            form.save() #저장 함수 불러옴
            return redirect('read') #맞으면 read로 보냄
    else: #그 외
        form = PostForm(instance=post) #다시 입력받음
        return render(request, 'crudApp/edit.html',{'form':form})  #다시 edit.html 요청


#삭제하기
def delete(request,id): #지정한 id값 입력받는 request 함수
    post = get_object_or_404(Post, id=id) #Post model의 id값을 가져오는 변수의 이름은 post, post 모델에서 id값을 post에서 제대로 가져오지 못하면 404에러 발생
    post.delete() #특정 id값 데이터 삭제해주기 위해 delete()함수 사용
    return redirect('read') #맞으면 read로 보냄