from django.shortcuts import render
import requests
from django.conf import settings
# Create your views here.

webservice_url = settings.AMIE_WEBSERVICE_URL


def homepage(request):
    data_provinces = []
    req = requests.get(url='{base_url}/get_provinces'.format(base_url=webservice_url))
    if req.status_code != 200:
        data_provinces = []

    data_provinces = req.json()
    return render(request, 'index.html', {'data_provinces': data_provinces})


def get_province_information(request):
    if request.method == "POST":
        province_id = request.POST.get('province')
        data = dict(province_id=province_id)
        req_population = requests.get(url='{base_url}/get_provinces'.format(base_url=webservice_url), params=data)
        req_district = requests.get(url='{base_url}/get_districts'.format(base_url=webservice_url), params=data)

        return render(request, 'index.html', {'req_population': req_population, 'req_district': req_district})
