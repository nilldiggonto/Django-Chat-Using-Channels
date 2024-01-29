from django.shortcuts import render

# Create your views here.
def singupView(request):
    template_name = 'accounts/signup.html'
    return render(request, template_name)