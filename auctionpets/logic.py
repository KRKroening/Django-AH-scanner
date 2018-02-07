from .models import Pets, AhPets
import requests
import pdb



def GetCharacterPetsFromBlizzard():
    urlCollected = "https://us.api.battle.net/wow/character/doomhammer/Ziast?fields=pets&locale=en_US&apikey=zpbbcws848zkzqb3gqv5rjy2npwf2qb9"
    responseCollected = requests.get(urlCollected).json()
    responseCollected = responseCollected["pets"]["collected"]

    urlAll = "https://us.api.battle.net/wow/pet/?locale=en_US&apikey=zpbbcws848zkzqb3gqv5rjy2npwf2qb9"
    responseAll = requests.get(urlAll).json()
    responseAll = responseAll["pets"]

    notCollected = []

    for i in responseAll: #refactor
        found = False
        for t  in responseCollected:
            if i["creatureId"] == t["creatureId"]:
                found = True
                break
        if not found:
            notCollected.append(i)

    for pet in notCollected:
        #pdb.set_trace()
        p,r = Pets.objects.get_or_create(creatureId=pet["creatureId"],speciesId=pet["stats"]["speciesId"],creatureName=pet["name"])
        p.save()

def GetPetsFromAH():
    # Delete the existing table so old records aren't used
    AhPets.objects.all().delete()

    initURL = "https://us.api.battle.net/wow/auction/data/Doomhammer?locale=en_US&apikey=zpbbcws848zkzqb3gqv5rjy2npwf2qb9"
    initResponse = requests.get(initURL).json()
    #pdb.set_trace()
    initResponse = initResponse["files"][0]["url"]
    dataResponse = requests.get(initResponse).json()
    for data in dataResponse["auctions"]:
        try:
            data["petSpeciesId"]
            foundPet = Pets.objects.get(speciesId=data["petSpeciesId"])
            if not foundPet.collected:
                #pdb.set_trace()
                AhPets.objects.create(
                    speciesId=foundPet.speciesId,
                    creatureId=foundPet.creatureId,
                    creatureName=foundPet.creatureName,
                    cost=data["buyout"],
                    time_left=data["timeLeft"]
                )
                AhPets.save()
        except:
            continue

def formatPrice(price):
    price = int(price)
    # copper = price[-2:]
    # silver = price[-4:-2]
    # gold = price[:6]

    # copper = price / 100 / 100
    # silver = price / 100
    # gold = copper % 100

    #("I have %dg %ds %dc"): format(, (copper / 100) % 100, copper % 100))

    #return gold , "g " , silver , "s " , copper , " c"

    # return "%sc %ss %sg" % (price % 100, price / 100 % 100, price // 10000)
    return "%sg %ss  %sc" % ( round(price // 10000), round(price / 100 % 100), round(price % 100))
