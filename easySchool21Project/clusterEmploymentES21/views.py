from django.shortcuts import render

from PIL import Image, ImageDraw

from clusterEmploymentES21.models import hydrogenPlaces
from clusterEmploymentES21.models import carbonPlaces
from clusterEmploymentES21.models import sulfurPlaces

jsondata = [
  {
    "place": "hy-a1",
    "login": "EmmaDillard"
  },
  {
    "place": "hy-f9",
    "login": "VirgieFernandez"
  },
  {
    "place": "ca-g5",
    "login": "LesterConway"
  },
  {
    "place": "ca-e8",
    "login": "TamikaBooker"
  },
  {
    "place": "ca-c4",
    "login": "HuntTalley"
  },
  {
    "place": "hy-f5",
    "login": "BridgetteCoffey"
  },
  {
    "place": "su-e1",
    "login": "VictoriaCain"
  },
  {
    "place": "hy-d9",
    "login": "HuberSmith"
  },
  {
    "place": "su-a6",
    "login": "EmersonMerritt"
  },
  {
    "place": "su-g4",
    "login": "TanyaHays"
  },
  {
    "place": "su-c7",
    "login": "OllieHayden"
  },
  {
    "place": "su-e5",
    "login": "KatherynAdams"
  },
  {
    "place": "ca-f6",
    "login": "BeckerDuke"
  },
  {
    "place": "ca-b6",
    "login": "RobbieGregory"
  },
  {
    "place": "su-c5",
    "login": "AshleeJohnston"
  },
  {
    "place": "su-e5",
    "login": "TashaJacobson"
  },
  {
    "place": "su-d1",
    "login": "AileenDejesus"
  },
  {
    "place": "ca-d7",
    "login": "MyrtleGuy"
  },
  {
    "place": "hy-b6",
    "login": "OrrKey"
  },
  {
    "place": "hy-h4",
    "login": "ShortBridges"
  },
  {
    "place": "hy-e4",
    "login": "BergerRuiz"
  },
  {
    "place": "hy-e6",
    "login": "TateStein"
  },
  {
    "place": "su-a2",
    "login": "LottieBrewer"
  },
  {
    "place": "hy-c4",
    "login": "GeorginaCummings"
  },
  {
    "place": "hy-e6",
    "login": "BrittanyOneal"
  },
  {
    "place": "hy-b9",
    "login": "KennedyMccarty"
  },
  {
    "place": "hy-g9",
    "login": "LambertDuncan"
  },
  {
    "place": "su-b1",
    "login": "SloanSalas"
  },
  {
    "place": "su-g9",
    "login": "HannahArmstrong"
  },
  {
    "place": "hy-a2",
    "login": "NoreenMcmillan"
  },
  {
    "place": "su-d2",
    "login": "MeltonMarsh"
  },
  {
    "place": "su-e5",
    "login": "LilianRamsey"
  },
  {
    "place": "ca-e2",
    "login": "ClementsBrady"
  },
  {
    "place": "su-d7",
    "login": "DuranFletcher"
  },
  {
    "place": "su-f6",
    "login": "LindsayHuff"
  },
  {
    "place": "ca-d4",
    "login": "YolandaGoodwin"
  },
  {
    "place": "hy-a1",
    "login": "SashaFischer"
  },
  {
    "place": "hy-g3",
    "login": "PageRodriquez"
  },
  {
    "place": "ca-g1",
    "login": "ElviaBurris"
  },
  {
    "place": "ca-e9",
    "login": "McgowanGolden"
  },
  {
    "place": "ca-c7",
    "login": "EmilyHenry"
  },
  {
    "place": "hy-g2",
    "login": "LucasHead"
  },
  {
    "place": "su-d8",
    "login": "WatsonCollins"
  },
  {
    "place": "hy-a1",
    "login": "CamposBentley"
  },
  {
    "place": "ca-a8",
    "login": "MableHoover"
  },
  {
    "place": "ca-g6",
    "login": "GreeneRichard"
  }
]

busyPositions = {}


def index_page(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})

    freePositions = hydrogenPlaces.objects.all()
    counter = freePositions.count()
    freePositions = carbonPlaces.objects.all()
    counter += freePositions.count()
    freePositions = sulfurPlaces.objects.all()
    counter += freePositions.count()

    return render(request, 'index.html', context={
        'count': counter,
        'freePositions': counter - len(busyPositions),
        'busyPositions': len(busyPositions),
    })

def hydrogenPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})
    freePositions = hydrogenPlaces.objects.all()

    counter=0

    for i in busyPositions:
        if "hy" in i:
            counter += 1

    return render(request, 'hydrogenPage.html', context={
        'count':freePositions.count(),
        'freePositions':freePositions.count()-counter,
        'busyPositions': counter,
    })

def carbonPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})
    freePositions = carbonPlaces.objects.all()

    counter = 0

    for i in busyPositions:
        if "ca" in i:
            counter += 1

    return render(request, 'carbonPage.html', context={
        'count': freePositions.count(),
        'freePositions': freePositions.count() - counter,
        'busyPositions': counter,
    })

def sulfurPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})
    freePositions = sulfurPlaces.objects.all()

    counter = 0

    for i in busyPositions:
        if "su" in i:
            counter += 1

    return render(request, 'sulfurPage.html', context={
        'count': freePositions.count(),
        'freePositions': freePositions.count() - counter,
        'busyPositions': counter,
    })


def hydrogenTextPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})
    freePositions = hydrogenPlaces.objects.all()
    for name in freePositions:
        print(name.positionName)
    return render(request, 'hydrogenTextPage.html', context={'freePositions':freePositions, 'busyPositions':busyPositions})

def carbonTextPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})
    freePositions = carbonPlaces.objects.all()
    for name in freePositions:
        print(name.positionName)
    return render(request, 'carbonTextPage.html', context={'freePositions': freePositions, 'busyPositions': busyPositions})


def sulfurTextPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})
    freePositions = sulfurPlaces.objects.all()
    for name in freePositions:
        print(name.positionName)
    return render(request, 'sulfurTextPage.html', context={'freePositions': freePositions, 'busyPositions': busyPositions})


def hydrogenGraphicPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})

    map = Image.open("media/hydAcarMap.png")
    img = Image.new("RGBA",map.size)

    draw = ImageDraw.Draw(img, "RGBA")

    radius = 12

    freePositions = hydrogenPlaces.objects.all()

    for position in freePositions:
        # print(f'{position}, {freePositions[position][0]}, {freePositions[position][1]}')
        if position.positionName in busyPositions:
            draw.ellipse((position.x - radius,
                          position.y - radius,
                          position.x + radius,
                          position.y + radius), fill=(255, 0, 0, 100))
        else:
            draw.ellipse((position.x - radius,
                          position.y - radius,
                          position.x + radius,
                          position.y + radius), fill=(0, 255, 0, 100))
    map.paste(img, (0,0), img)
    map = map.rotate(90, expand=True)
    map.save("media/hydrogenMapEdit.png", "PNG")

    return render(request, 'hydrogenGraphicPage.html')

def carbonGraphicPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})

    map = Image.open("media/hydAcarMap.png")
    img = Image.new("RGBA", map.size)

    draw = ImageDraw.Draw(img, "RGBA")

    radius = 12

    freePositions = carbonPlaces.objects.all()

    for position in freePositions:
        # print(f'{position}, {freePositions[position][0]}, {freePositions[position][1]}')
        if position.positionName in busyPositions:
            draw.ellipse((position.x - radius,
                          position.y - radius,
                          position.x + radius,
                          position.y + radius), fill=(255, 0, 0, 100))
        else:
            draw.ellipse((position.x - radius,
                          position.y - radius,
                          position.x + radius,
                          position.y + radius), fill=(0, 255, 0, 100))
    map.paste(img, (0, 0), img)
    map = map.rotate(90, expand=True)
    map.save("media/carbonMapEdit.png", "PNG")

    return render(request, 'carbonGraphicPage.html')


def sulfurGraphicPage(request):
    for i in jsondata:
        busyPositions.update({i['place']: i['login']})

    map = Image.open("media/sulfurMap.png")
    img = Image.new("RGBA", map.size)

    draw = ImageDraw.Draw(img, "RGBA")

    radius = 12

    freePositions = sulfurPlaces.objects.all()

    for position in freePositions:
        # print(f'{position}, {freePositions[position][0]}, {freePositions[position][1]}')
        if position.positionName in busyPositions:
            draw.ellipse((position.x - radius,
                          position.y - radius,
                          position.x + radius,
                          position.y + radius), fill=(255, 0, 0, 100))
        else:
            draw.ellipse((position.x - radius,
                          position.y - radius,
                          position.x + radius,
                          position.y + radius), fill=(0, 255, 0, 100))
    map.paste(img, (0, 0), img)
    map = map.rotate(90, expand=True)
    map.save("media/sulfurMapEdit.png", "PNG")

    return render(request, 'sulfurGraphicPage.html')