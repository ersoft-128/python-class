from django.shortcuts import render

# Create your views here.
def homepage(request):
    if request.method=="POST":
        seacrh=request.POST.get("search")
        print(seacrh)
    return render(request,"index.html")
def searchbar(request):
    return render(request,"search.html")
def about(request):
    return render(request,'about.html')