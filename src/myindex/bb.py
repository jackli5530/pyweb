from anaconda_navigator.utils.py3compat import request
from django.shortcuts import render_to_response

def hi(request):
    return render_to_response("index.html")