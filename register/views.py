# views.py
from django.shortcuts import render, redirect ,HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group


# Create your views here.
def register(response):
	print('****************')
	print("register:",response.method)
	print('****************')

	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid:
			try:
				new_user = form.save()
				new_user.is_staff = True
				my_group = Group.objects.get(name='admin_simple') 
				my_group.user_set.add(new_user)
				my_group = form.save()
				login(response, new_user)
				return HttpResponseRedirect("/")
			except:
				print("form is not valid",form.error_messages)	

			# new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
			
			# return redirect("/")
	else:

		form = RegisterForm()
		# return redirect('/')
	return render(response, "register/register.html", {"form":form})
