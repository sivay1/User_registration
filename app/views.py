from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import Userdata
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registerPage(request):
	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			print(f"User {user.username} created successfully.")
			return redirect('login')  # Change 'home' to the URL you want to redirect to after registration
		else:
			print("Form is not valid. Errors:", form.errors)
	else:
		print("Not a POST request.")

	context = {'form': form}
	return render(request, "register.html", context)
def loginPage(request):
	if request.method == "POST":

		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username Or Password is incorrect')

	context = {}
	return render(request,"login.html",context)
@login_required
def home(request):
	data = Userdata.objects.filter(username=request.user).first()
	context = {"data":data}
	return render(request,"home.html",context)

def logoutUser(request):
    logout(request)
    return redirect('login')

