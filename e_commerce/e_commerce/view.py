from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def product(request):
    return render(request, 'product.html')
def contact(request):
    return render(request, 'contact.html')
def feedback(request):
    return render(request, 'feedback.html') # Replace this with actual login page template.
