from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.views.generic import View, CreateView

from accounts.models import CustomUser
from .forms import SignInForm, CustomUserCreationForm
# Create your views here.

class Signin(View):
    def get(self, request, *args, **kwargs):
        next_url = request.GET.get('next')
        if next_url is None:
            next_url = '/'
        form = SignInForm()
        return render(request, 'accounts/login.html', {'form': form, 'next':next_url})

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password= password)

            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', '')
                if next_url != '' and next_url != None:
                    return HttpResponseRedirect(next_url)
                return redirect('frontpage')

        messages.info(request, "Email or Password is incorrect")
        return render(request, 'accounts/login.html', {'form': form})


class Signup(CreateView):
    template_name = 'accounts/signup.html'
    model = CustomUser
    form_class = CustomUserCreationForm


def logoutUser(request):
    logout(request)
    return redirect('login')