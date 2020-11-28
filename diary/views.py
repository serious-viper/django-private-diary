from django.shortcuts import render,redirect
from .models import Diary
from .forms import DairyForm
from django.http import HttpResponse


def index(request):
      posts=Diary.objects.all()
      return render(request ,  "pages/index.html" , {"posts":posts})
	
def diary(request, num):
	post_detail=Diary.objects.get(id=num)
	return render(request ,  "pages/diary.html" , {"detail": post_detail})

	
def new(request):
	if request.method == "POST":
		blah = DairyForm(request.POST)
		if blah.is_valid():
			blah.save()
			form = DairyForm()
			return redirect('index')
	else:
		form=DairyForm()
		return render(request ,  "pages/new.html" , {  'form': form})