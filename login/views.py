from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("""
    	<h1>Login Page</h1>
    	<hr>
    	Hello, world. You're at the Login index.
    	""")
    	