from django.shortcuts import render

# Create your views here.
def kohli(request):
    return render(request,'kohli.html')
def table(request):
    return render(request,'table.html')
def forms(request):
    return render(request,'forms.html')
def landing(request):
    return render(request,'landing.html')
def frames(request):
    return render(request,'frames.html')
def transform(request):
    return render(request,'transform.html')
def music(request):
    return render(request,'music.html')
def combinators(request):
    return render(request,'combinators.html')
def positions(request):
    return render(request,'positions.html')
def attribute(request):
    return render(request,'attribute.html')
def csslink(request):
    return render(request,'csslink.html')

