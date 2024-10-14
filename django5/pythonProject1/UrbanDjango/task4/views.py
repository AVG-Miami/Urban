from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request,'fourth_task/main.html')

def magazine(request):
    games = ['Atomic Heart','Cyberpunk 2077','PayDay 2']
    # game_2 = 'Cyberpunk 2077'
    # game_3 = 'PayDay 2'
    context = {
        'games': games
        # 'game_2': game_2,
        # 'game_3': game_3
    }
    return render(request,'fourth_task/magazine.html', context)

def corzine(request):
    return render(request,'fourth_task/corzine.html')

