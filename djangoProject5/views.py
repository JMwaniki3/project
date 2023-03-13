from django.shortcuts import render


def index(request):
  context ={'page': 'home'}
  return render(request, 'index.html', context)
def _messages(request):
  return render(request, '_messages.html')
def _navbar(request):
  return render(request, '_navbar.html')
def base(request):
  return render(request, 'base.html')
def change_password(request):
  return render(request, 'change_password.html')
def detail(request):
  return render(request, 'detail.html')
def login(request):
  return render(request, 'login.html')
def logout(request):
  return render(request, 'logout.html')
def profile(request):
  return render(request, 'profile.html')
def register(request):
  return render(request, 'register.html')
def results(request):
  return render(request, 'results.html')