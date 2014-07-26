import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from models import *
from forms import *
# Create your views here.

def home(request):
    # if request.method == "POST":
    #     form = GetTeamForm(request.POST)
    #     if form.is_valid():
    #         this_team = form.cleaned_data['team']
    #         team = Pokemon.objects.filter(team=this_team)
    #         return render_to_response('pokemon_team_info.html', team)
    # else:
    #     form = GetTeamForm()
    # data = {'form': form}

    data = {
        'teams': Team.objects.all(),
    }
    return render(request, "home.html", data)


# initial basic version
@csrf_exempt
def serial_pokemon(request):
    pokemon = Pokemon.objects.all()
    data = serializers.serialize('json', pokemon)
    return HttpResponse(data, mimetype='application/json')


@csrf_exempt
def all_pokemon(request):
    pokemon_objects = Pokemon.objects.all()
    collection = []
    for pokemon in pokemon_objects:
        collection.append({
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'id': pokemon.pk,
            'team': {
                'id': pokemon.team.id,
                'name': pokemon.team.name
            }
        })
    return HttpResponse(
                json.dumps(collection),
                content_type='application.json'
           )

# SERIAL VERSION
# @csrf_exempt
# def new_pokemon(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         pokemon = Pokemon.objects.create(
#             name=data['name'],
#             image=data['image'],
#             pokedex_id=data['pokedex_id'],
#             team=Team.objects.get(id=data['team'])
#         )
## SERIALIZE BELOW EXPECTS AN ARRAY
#     response = serializers.serialize('json', [pokemon])
#     return HttpResponse(response,
#                         content_type='application/json')

@csrf_exempt
def new_pokemon(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print data
        team, created = Team.objects.get_or_create(name='Team K')
        print 'hello'
        pokemon = Pokemon.objects.create(
            name=data['name'],
            image=data['image'],
            pokedex_id=data['pokedex_id'],
            team=team
        )
        pokemon_info = {
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'team': {
                'id': pokemon.team.id,
                'name': pokemon.team.name
            }
        }
        return HttpResponse(json.dumps(pokemon_info),
                   content_type='application/json')


def pokemon_info(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    this_pokemon = {
        'name': pokemon.name,
        'image': pokemon.image,
        'pokedex_id': pokemon.pokedex_id,
        'team': {
            'id': pokemon.team.id,
            'name': pokemon.team.name
        }
    }
    return render_to_response('pokemon_info.html', this_pokemon)

def pokemon_team_info(request, team_id):
    pokemon_in_team = Pokemon.objects.filter(team_id=team_id)
    # this_pokemon = {
    #     'name': pokemon.name,
    #     'image': pokemon.image,
    #     'pokedex_id': pokemon.pokedex_id,
    #     'team': {
    #         'id': pokemon.team.id,
    #         'name': pokemon.team.name
    #     }
    # }
    data = {
        'pokemon_in_team': pokemon_in_team,
    }
    return render_to_response('pokemon_team_info.html', data)