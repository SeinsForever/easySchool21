from django.shortcuts import render

from PIL import Image, ImageDraw

from clusterEmploymentES21.models import hydrogenPlaces
from clusterEmploymentES21.models import carbonPlaces

def index_page(request):

    return render(request,'index.html', )

def hydrogenPage(request):
    busyPositions = {
        "hy-b4",
        "hy-a8",
        "hy-a2",
        "hy-b4",
    }

    freePositions = hydrogenPlaces.objects.all()

    return render(request, 'hydrogenPage.html', context={
        'count':freePositions.count(),
        'freePositions':freePositions.count()-len(busyPositions),
        'busyPositions': len(busyPositions),
    })

def carbonPage(request):
    busyPositions = {
        "hy-b4",
        "hy-a8",
        "hy-a2",
        "hy-b4",
    }

    freePositions = hydrogenPlaces.objects.all()

    return render(request, 'hydrogenPage.html', context={
        'count': freePositions.count(),
        'freePositions': freePositions.count() - len(busyPositions),
        'busyPositions': len(busyPositions),
    })

    return render(request, 'carbonPage.html')

def hydrogenTextPage(request):
    freePositions = hydrogenPlaces.objects.all()
    for name in freePositions:
        print(name.positionName)
    return render(request, 'hydrogenTextPage.html', context={'freePositions':freePositions})

def carbonTextPage(request):
    return render(request, 'carbonTextPage.html')

def hydrogenGraphicPage(request):
    map = Image.open("media/hydrogenMap.png")
    img = Image.new("RGBA",map.size)

    draw = ImageDraw.Draw(img, "RGBA")

    radius = 12

    freePositions = hydrogenPlaces.objects.all()

    busyPositions = {
        "hy-b4",
        "hy-a8",
        "hy-a2",
        "hy-a1",
    }

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
    map.save("media/hydrogenMapEdit.png", "PNG")

    return render(request, 'hydrogenGraphicPage.html')

def carbonGraphicPage(request):

    map = Image.open("media/carbonMap.png")
    img = Image.new("RGBA", map.size)

    draw = ImageDraw.Draw(img, "RGBA")

    radius = 12

    freePositions = carbonPlaces.objects.all()

    busyPositions = {
        "ca-b4",
        "ca-a8",
        "hy-a2",
        "hy-a1",
    }

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
    map.save("media/carbonMapEdit.png", "PNG")

    return render(request, 'carbonGraphicPage.html')