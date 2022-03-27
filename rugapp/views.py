import requests
from django.db.models import Q
from django.shortcuts import render, redirect
import json
from .forms import SearchForm, VoteForm
from .models import NFTProject, Comments


# Create your views here.


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

        one_day_volume = parsed_json["collection"]["stats"]["one_day_volume"]
        seven_day_volume = parsed_json["collection"]["stats"]["seven_day_volume"]
        thirty_day_volume = parsed_json["collection"]["stats"]["thirty_day_volume"]
        num_owners = parsed_json["collection"]["stats"]["num_owners"]
        description = parsed_json["collection"]["description"]
        external_link = parsed_json["collection"]["external_url"]
        slug = parsed_json["collection"]["slug"]
        floor_price = parsed_json["collection"]["stats"]["floor_price"]
        verified = parsed_json["collection"]["safelist_request_status"]

        print(image, name, total_supply, total_sales, banner_image_url, total_volume, num_owners, description, slug,
              floor_price, verified, external_link)


        nft = NFTProject(name = name, banner_image = banner_image_url, description = description, total_volume = total_volume, total_supply = total_supply, num_owners = num_owners, floor_price = floor_price, slug = slug, image = image, external_link = external_link, one_day_volume = one_day_volume, seven_day_volume = seven_day_volume, thirty_day_volume = thirty_day_volume, safelist_request_status = verified)
        nft.save()
'''


    '''
    offset = 0
    while offset <= 40000:

        url = "https://api.opensea.io/api/v1/collections?offset=" + str(offset) + "&limit=300"
        headers = {"Accept": "application/json"}

        response = requests.request("GET", url, headers=headers)

        parsed_json = json.loads(response.text)
        try:
            for i in range(len(parsed_json["collections"])):
                image = parsed_json["collections"][i]["image_url"]
                name = parsed_json["collections"][i]["name"]
                total_supply = parsed_json["collections"][i]["stats"]["total_supply"]
                total_sales = parsed_json["collections"][i]["stats"]["total_sales"]
                banner_image_url = parsed_json["collections"][i]["banner_image_url"]
                total_volume = parsed_json["collections"][i]["stats"]["total_volume"]
                one_day_volume = parsed_json["collections"][i]["stats"]["one_day_volume"]
                seven_day_volume = parsed_json["collections"][i]["stats"]["seven_day_volume"]
                thirty_day_volume = parsed_json["collections"][i]["stats"]["thirty_day_volume"]
                num_owners = parsed_json["collections"][i]["stats"]["num_owners"]
                description = parsed_json["collections"][i]["description"]
                external_link = parsed_json["collections"][i]["external_url"]
                slug = parsed_json["collections"][i]["slug"]
                floor_price = parsed_json["collections"][i]["stats"]["floor_price"]
                verified = parsed_json["collections"][i]["safelist_request_status"]

                print(image, name, total_supply, total_sales, banner_image_url, total_volume, num_owners, description, slug,
                      floor_price, verified, external_link)

                nft = NFTProject(name=name, banner_image=banner_image_url, description=description, total_volume=total_volume,
                                 total_supply=total_supply, num_owners=num_owners, floor_price=floor_price, slug=slug,
                                 image=image, external_link=external_link, one_day_volume=one_day_volume,
                                 seven_day_volume=seven_day_volume, thirty_day_volume=thirty_day_volume,
                                 safelist_request_status=verified)
                nft.save()
            offset += 20000
        except:
            offset += 20000
    '''


    nfts = NFTProject.objects.order_by('-total_volume')[0:10]
    voted = False
    nft_voted_for = ""
    if request.session['voted'] == True:

        voted = True
        nft_voted_for = request.session['nft_voted']
        request.session['nft_voted'] = ""
        request.session['voted'] = False


    if request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            request.session['query'] = query
            return redirect('searched/')
    else:
        form = SearchForm



    return render(request, 'rugapp/home.html', {"nfts": nfts, 'form': form, "voted":voted, "nft_voted_for": nft_voted_for})

def searched(request):

    if request.session.get('query') != "":
        query_string = request.session.get('query')
    else:
        query_string = "StopTheRug"
    found_entries = None

    entry_query = get_query(query_string, ['name',])

    found_entries = NFTProject.objects.filter(entry_query).order_by('-total_volume')

    return render(request, 'rugapp/searched.html',
                              {'query': query_string, 'nfts': found_entries}
                              )

def about(request):



    return render(request, 'rugapp/about.html')

def vote(request, nft_id):
    nft = NFTProject.objects.get(pk=nft_id)

    if request.POST:
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.cleaned_data.get('vote')
            comment = form.cleaned_data.get('comment')
            new_commment = Comments(text = comment, nft = nft)
            new_commment.save()
            nft.votes += 1
            nft.total_cred += vote
            nft.credibility_rating = nft.total_cred/nft.votes
            nft.save()
            request.session['voted'] = True
            request.session['nft_voted'] = nft.name
            return redirect('/')
    else:
        form = VoteForm

    return render(request, 'rugapp/vote.html', {"nft": nft, "form":form})

def report(request, nft_id):

    nft = NFTProject.objects.get(pk = nft_id)
    comments = Comments.objects.filter(nft = nft)

    votes = []

    return render(request, 'rugapp/report.html', {"nft": nft, "comments": comments, "comment_amount":len(comments)})



import re



def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

