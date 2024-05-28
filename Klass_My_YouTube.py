from colorama import Fore
from time import sleep


class UrTube:
    users = []
    videos = []
    current_user = ''

    def __init__(self):
        pass

    def find_User_by_nickname(self, nickname):
        for item_user in UrTube.users:
            if item_user.nickname == nickname:
                return item_user

    def log_in(self, login, password):
#        item_user = self.find_User_by_nickname( login )
        for item_user in UrTube.users:
            if item_user.nickname == login and item_user.password == hash(password):
                self.current_user = item_user;
                print( Fore.GREEN + 'Пользователь ', self.current_user, ' успешно вошел в систему' )
            if not self.current_user:
                print( Fore.RED + 'Пользователя', login, 'не существует' )

    def log_out(self):
        print( Fore.GREEN + "Пользователь ", self.current_user, "вышел из системы" )
        self.current_user = None

    def register(self, nickname, password, age):
        reg_user = User( nickname, hash(password), age )
        for item_user in UrTube.users:
            if item_user.nickname == nickname:
                print( Fore.RED + 'Пользователь ' + nickname + ' уже существует!' )
                return
        self.users.append( reg_user )
        print( Fore.GREEN + 'Пользователь ', reg_user, "успешно зарегистрирован" )
        self.log_in( nickname, password )

    def add(self, *new_video):  # Добавление спсика видео
        for item_video in new_video:
            self.videos.append( item_video )

    def get_videos(self, word_search):  # поиск названий видео по ключевым словам
        list_video = []
        for item_video in self.videos:
            if item_video.title.lower().find( word_search.lower() ) != -1:
                list_video.append( item_video.title )
        return list_video

    def watch_video(self, word_search):  # абсолютный поиск видео и воспроизведение
        if not self.current_user:
            print( Fore.RED + 'Войдите в аккаунт чтобы смотреть видео' )
            return
        dostup = False
        video_found = True
        for item_video in self.videos:
            if item_video.title == word_search:  # Поиск по названию видео
                if item_video.adult_mode:  # проверка на возрастное ограничение
                    for item_user in self.users:
                        if item_user == self.current_user:
                            if int( item_user.age ) >= 18:  # проверка возраста текущего пользователя
                                print( Fore.GREEN + 'можно смотреть', self.current_user )
                                dostup = True
                            else:
                                print( Fore.RED + 'Вам нет 18 лет, пожалуйста покиньте страницу', self.current_user )
                                dostup = False
                                return
                else:
                    dostup = True
                if dostup:
                    print( Fore.GREEN + "Воспроизводим видео ", item_video.title )
                    for run_time in range( item_video.time_now + 1, item_video.duration + 1 ):
                        print( ' ', run_time, end="" )
                        sleep( 1 )
                    print( " Конец видео" )
                    return
            else:
                video_found = False
        if not video_found:
            print( Fore.RED + 'Видео не найдено' )


class Video:
    """
    Каждый объект класса Video должен обладать следующими атрибутами и методами:
    Атриубуты:
    title(заголовок, строка),
    duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту,
    bool (False по умолчанию))
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    """
    Каждый объект класса User должен обладать следующими атрибутами и методами:
    Атриубуты:
    nickname(имя пользователя, строка),
    password(в хэшированном виде, число),
    age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


print( "Добро пожаловать на мой YouTube!" )

ur = UrTube()
v1 = Video( 'Лучший язык программирования 2024 года', 200 )
v2 = Video( 'Для чего девушкам парень программист?', 10, adult_mode=True )

# Добавление видео
ur.add( v1, v2 )

# Проверка поиска
print( Fore.WHITE + "команда: " + Fore.BLUE + "print(ur.get_videos('лучший'))" )
print( Fore.GREEN, end='' )
print( ur.get_videos( 'лучший' ) )
print( Fore.WHITE + "команда: " + Fore.BLUE + "print(ur.get_videos('ПРОГ'))" )
print( Fore.GREEN, end='' )
print( ur.get_videos( 'ПРОГ' ) )

# Проверка на вход пользователя и возрастное ограничение
print( Fore.BLUE + "команда: ur.watch_video('Для чего девушкам парень программист?')" )
ur.watch_video( 'Для чего девушкам парень программист?' )
print( Fore.WHITE + "команда: " + Fore.BLUE + "ur.register('vasya_pupkin', 'lolkekcheburek', 13)')" )
ur.register( 'vasya_pupkin', 'lolkekcheburek', 13 )

# print('Текущий пользователь ' ,ur.current_user)
print( Fore.WHITE + "команда: " + Fore.BLUE + "ur.watch_video('Для чего девушкам парень программист?')" )
ur.watch_video( 'Для чего девушкам парень программист?' )
print( Fore.WHITE + "команда: " + Fore.BLUE + "ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)" )
ur.register( 'urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25 )
print( Fore.WHITE + "команда: " + Fore.BLUE + "ur.watch_video('Для чего девушкам парень программист?')" )
ur.watch_video( 'Для чего девушкам парень программист?' )

# Проверка входа в другой аккаунт
print( Fore.WHITE + "команда: " + Fore.BLUE + "ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)" )
ur.register( 'vasya_pupkin', 'F8098FM8fjm9jmi', 55 )
print( Fore.WHITE + "команда: " + Fore.BLUE + "print(ur.current_user)" )
print( Fore.GREEN, end='' )
print( ur.current_user )

# Попытка воспроизведения несуществующего видео
ur.watch_video( 'Лучший язык программирования 2024 года!' )
