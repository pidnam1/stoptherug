from django.shortcuts import render
import json
from .models import NFTProject
# Create your views here.
from django.http import HttpResponse


def home(request):
    '''
    with open('rugapp/trial_data.json', 'r') as json_file:
        json_load = json.load(json_file)
    for i in range(0, len(json_load)):
        parsed_json = json.loads(json_load[i])
        image = parsed_json["collection"]["image_url"]
        name = parsed_json["collection"]["name"]
        total_supply = parsed_json["collection"]["stats"]["total_supply"]
        total_sales = parsed_json["collection"]["stats"]["total_sales"]
        banner_image_url = parsed_json["collection"]["banner_image_url"]
        total_volume = parsed_json["collection"]["stats"]["total_volume"]
        num_owners = parsed_json["collection"]["stats"]["num_owners"]
        description = parsed_json["collection"]["description"]
        external_link = parsed_json["collection"]["external_url"]
        slug = parsed_json["collection"]["slug"]
        floor_price = parsed_json["collection"]["stats"]["floor_price"]
        verified = parsed_json["collection"]["safelist_request_status"]

        print(image, name, total_supply, total_sales, banner_image_url, total_volume, num_owners, description, slug,
              floor_price, verified, external_link)

        nft = NFTProject(name = name, banner_image = banner_image_url, description = description, total_volume = total_volume, total_supply = total_supply, num_owners = num_owners, floor_price = floor_price, slug = slug, image = image, external_link = external_link, safelist_request_status = verified)
        nft.save()
        '''






    return render(request, 'rugapp/home.html')

def searched(request):


    return render(request, 'rugapp/searched.html')
def about(request):



    return render(request, 'rugapp/about.html')
def report(request):

    nft = NFTProject.objects.get(slug="boredapeyachtclub")
    return render(request, 'rugapp/report.html', {"nft":nft})