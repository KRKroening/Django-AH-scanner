from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Pets, AhPets
from django.views import generic
from .logic import *
import pdb

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'auctionpets/index.html'
    context_object_name = "current_found_pets"

    #GetCharacterPetsFromBlizzard()


    def get_queryset(self):
        GetPetsFromAH()
        pets = AhPets.objects.order_by('creatureName')
        for pet in pets:
            pet.cost = formatPrice(pet.cost)
        return pets

def registerAsCollected(request, speciesId):
    #pdb.set_trace()
    selectedPet = Pets.objects.get(speciesId=speciesId)
    selectedPet.collected=True
    selectedPet.save()
    GetPetsFromAH()
    return HttpResponseRedirect(reverse('auctionpets:index'))