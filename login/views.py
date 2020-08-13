from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from .worker import user_validate_db,user_create
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

#def login(request):
#    if request.method=='GET':
#        # messages.info(request, 'Your password has been changed successfully!')
#        return render(request, 'login.html', {})

 
@csrf_exempt
def user_validate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        req_data=json.loads(request.body.decode("utf-8"))
        user_name=req_data.get('username')
        password=req_data.get('password')
        if (user_name and password):
            decison=user_validate_db(user_name,password)
            if decison[0]:
                messages.info(request, decison[1])
                return JsonResponse({"status_code":"200","status":"SUCESS","reason":"Valid User"}) 
            return JsonResponse({"status_code":"201","status":"FAILD","reason":"INVALID_USER_AUTHENTICATION"})
        else:
            return JsonResponse({"status_code":"202","status":"FAILD","reason":"parameter missing"})
    return JsonResponse({"status_code":"405","status":"FAILD","reason":"Method Not Allowed"})
@csrf_exempt
def create_user_(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        req_data=json.loads(request.body.decode("utf-8"))
        user_name=req_data.get('username')
        password=req_data.get('password')
        if (user_name and password):
            decison=user_create(user_name,password)
            if decison[0]:
                messages.info(request, decison[1])
                return JsonResponse({"status_code":"200","status":"SUCESS","reason":"Created Sucessfully"})
            return JsonResponse({"status_code":"201","status":"FAILD","reason":"User Exists"})
        else:
            return JsonResponse({"status_code":"202","status":"FAILD","reason":"parameter missing"}) 
    else:
        return JsonResponse({"status_code":"405","status":"FAILD","reason":"Method Not Allowed"})
        
    


