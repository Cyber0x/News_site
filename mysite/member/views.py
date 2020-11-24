from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AuthUserForm, RegisterUserForm



    #def post(self, request, *args, **kwargs):
     #   res = super().post(request, *args, **kwargs)
       # form_kwargs = self.get_form_kwargs()
        #username = form_kwargs['data']('username')
        #user = User.objects.get(username=username)
        #login(user=user, request=request)
        #return res


class BlogLoginView(LoginView):
    template_name = 'member/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('blog:home')


class RegisterUserView(CreateView):
    model = User
    template_name = 'member/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('blog:home')


class LogoutUserView(LogoutView):
    template_name = 'member/logout.html'

