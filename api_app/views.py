from django.shortcuts import render
from django.views import View
from api_app.models import *

# Create your views here.


class Index(View):
    def get(self, request):
        res = dict()
        res['content'] = list(Notices.objects.all().values('content'))[::-1][:2]
        return render(request, 'login.html', res)



