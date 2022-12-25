from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import json
from .models import ParkinsonModel
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


"""
Values that will be entered by user:
* PPE
* Shimmer:APQ5
* MDVP:Fo(Hz)
* MDVP:Shimmer
* MDVP:Fo(Hz)
* MDVP:Fhi(Hz)
* MDVP:Flo(Hz)
* MDVP:Fhi(Hz)
* RPDE
"""
PPE = 0
ShimmerAPQ5 = 0
MDVPFo = 0
MDVPShimmer = 0
MDVPFhi = 0
MDVPFlo = 0
RPDE = 0

def isParkinson(PPE, ShimmerAPQ5,MDVPFo, MDVPShimmer, MDVPFhi, MDVPFlo, RPDE):
    if(PPE > 0.134): # Left side of tree
        if(ShimmerAPQ5 > 0.013):
            return True
        else:
            if(MDVPFo > 117.987):
                if(MDVPShimmer > 0.021):
                    return False
                else:
                    return True
            else:
                if(MDVPFo > 112.349):
                    return False
                else:
                    return True

    else: # Right side of tree
        if(MDVPFhi > 202.310):
            if(MDVPFlo > 93.141):
                return False
            else:
                if(MDVPFhi > 233.694):
                    return False
                else:
                    return True
        else:
            if(RPDE > 0.459):
                return False
            else:
                return True


# True ise parkinsonsun, False ise degilsin.



def render_template(request):
    if request.method == 'GET':
        return render(request, 'parkinson.html', {})
    else:
        return HttpResponse

@csrf_exempt
def control_parkinson(request):
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        ppe = float(json_data['ppe'])
        shimmerapq5 = float(json_data['shimmerapq5'])
        mdvpfo = float(json_data['mdvpfo'])
        mdvpshimmer = float(json_data['mdvpshimmer'])
        mdvpflo = float(json_data['mdvpflo'])
        mdvpfhi = float(json_data['mdvpfhi'])
        rpde = float(json_data['rpde'])


        check_parkinson = isParkinson(ppe, shimmerapq5, mdvpfo, mdvpshimmer, mdvpfhi, mdvpflo, rpde)
        print(check_parkinson)
        if check_parkinson == True:
            created = ParkinsonModel.objects.create(ppe=ppe, shimmerapq5=shimmerapq5, mdvpfo=mdvpfo, mdvpshimmer=mdvpshimmer, mdvpfhi=mdvpfhi, mdvpflo=mdvpflo, rpde=rpde, is_parkinson=True)
            return JsonResponse({'data':created.to_dict()}, status=200)
        else:
            created = ParkinsonModel.objects.create(ppe=ppe, shimmerapq5=shimmerapq5, mdvpfo=mdvpfo, mdvpshimmer=mdvpshimmer, mdvpfhi=mdvpfhi, mdvpflo=mdvpflo, rpde=rpde, is_parkinson=False)
            return JsonResponse({'data':created.to_dict()}, status=200)


    else:
        return HttpResponse(status=405)



@csrf_exempt
def return_datas(request):
    if request.method == 'GET':
        datas = ParkinsonModel.objects.all().order_by('created_date')

        datas_serialized = []

        for data in datas:
            datas_serialized.append(data.to_dict())

        return JsonResponse({'data':datas_serialized}, status=200)
    else:
        return HttpResponse(status=405)