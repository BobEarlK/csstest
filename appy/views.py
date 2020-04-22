from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def front_page_view(request):
    return render(request, 'appy/front_page.html')