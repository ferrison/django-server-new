from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from land.models import Users
import datetime


@csrf_exempt
def info(request):
    print(request.POST)
    print(request.body)
    values = request.POST
    if 'name' in values and 'pass' in values:
        try:
            user = Users.objects.get(username=values['name'])
        except Users.DoesNotExist:
            return HttpResponse('Bad username')
        if user.password == values['pass']:
            return JsonResponse(user.get())
        else:
            return HttpResponse('Bad password')
    return HttpResponse('Bad request')


@csrf_exempt
def login(request):
    print(request.POST)
    print(request.body)
    values = request.POST
    if 'name' in values and 'pass' in values and 'imei' in values:
        try:
            user = Users.objects.get(username=values['name'])
        except Users.DoesNotExist:
            return HttpResponse('Bad username')
        if user.password == values['pass']:
            if user.imei == "" or user.imei == values['imei']:
                if user.user_info.nom.time.start.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=3)))\
                 < datetime.datetime.now(datetime.timezone.utc)\
               and user.user_info.nom.time.end.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=3)))\
                 > datetime.datetime.now(datetime.timezone.utc):
                    user.imei = values['imei']
                    user.save()
                    return HttpResponse(user.id)
                else:
                    return HttpResponse('Bad time')
            #if user.imei == values['imei']:
                #return HttpResponse(user.id)
            return HttpResponse('Access denied')
        return HttpResponse('Bad password')
    return HttpResponse('Bad request')


@csrf_exempt
def logout(request):
    print(request.POST)
    print(request.body)
    values = request.POST
    if 'id' in values and 'imei' in values:
        try:
            user = Users.objects.get(id=values['id'])
        except Users.DoesNotExist:
            return HttpResponse('Bad id')
        if user.imei == values['imei']:
            user.imei = ''
            user.save()
            return HttpResponse('Ok')
        return HttpResponse('Access denied')
    return HttpResponse('Bad request')


@csrf_exempt
def current(request):
    print(request.POST)
    print(request.body)
    values = request.POST
    if 'id' in values:
        try:
            user = Users.objects.get(id=values['id'])
        except Users.DoesNotExist:
            return HttpResponse('Bad id')
        if user.user_info.nom.time.start.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=3)))\
                 < datetime.datetime.now(datetime.timezone.utc)\
               and user.user_info.nom.time.end.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=3)))\
                 > datetime.datetime.now(datetime.timezone.utc):
            return HttpResponse(str(user.user_info.nom))
        return HttpResponse('Bad time')
    return HttpResponse('Bad id')
