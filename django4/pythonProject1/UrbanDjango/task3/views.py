from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request,'third_task/main.html')

def magazine(request):
    game_1 = 'Atomic Heart'
    game_2 = 'Cyberpunk 2077'
    game_3 = 'PayDay 2'
    context = {
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3
    }
    return render(request,'third_task/magazine.html', context)

def corzine(request):
    return render(request,'third_task/corzine.html')
