from django.shortcuts import render

from .models import UserData
from .utils import data_to_xslx


def home(request):
    user_data = UserData.objects.all()
    context: dict = {
        'user_data': user_data
    }
    return render(request=request, template_name='index.html', context=context)


def generate_excel(request):
    user_data = UserData.objects.all().values_list()
    return data_to_xslx(user_data=user_data)
