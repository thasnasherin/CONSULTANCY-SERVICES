from django.shortcuts import render

# Create your views here.
def hrindex(request):
    return render(request,'hrindex.html')