from django.http import HttpResponse
from django.shortcuts import render
 
def test(request):
    context = {}
    context['word'] = 'test'
    return render(request, 'test.html', context)