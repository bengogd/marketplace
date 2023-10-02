from django.shortcuts import render

# Create your views here.

#Home view - index.html
def home(request):
    
    return render(request, "main/index.html")

def blog(request):
    return render(request, "main/blog-single.html")