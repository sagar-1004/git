from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from dateutil.relativedelta import relativedelta
import datetime
from backend.models import *
import requests
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import json
from django.http import JsonResponse
from django.core import serializers
import json
from uuid import UUID
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import re
# from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this

# Create your views here.
def home(request):
    return render(request, 'home.html')

