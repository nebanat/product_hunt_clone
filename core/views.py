from django.shortcuts import render
from django.views import View
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import SignUpForm


# # Create your views here.
class UserSignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'core/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('product:index'))
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # clean the data
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('product:index'))
        else:
            return render(request, self.template_name, {'form': form})






