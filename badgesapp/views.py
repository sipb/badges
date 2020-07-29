from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def badges(request):
    context = {
        'category_list': [{
            'name': 'Tier 1 Badges',
            'badges_list': [{
                'img_src': '../static/GrumpyFuzzball-meteor-back.png',
                'name': 'Grumpy Fuzzball',
                'description': 'Obtained by being a grumpy fuzzball.'
            }] * 5
        }]
    }
    return render(request, 'badges.html', context)