from time import sleep
class UrTube:
    users=[]
    videos=[]
    current_user=''

    def __init__(self):
        pass

    def log_in(self, login, password):
        for item_user in self.users:
            if item_user.nickname == login and item_user.password == password:
                self.current_user=item_user;
                print( 'Пользователь ', self.current_user, ' успешно вошел в систему' )

        if not self.current_user:
            print('Пользователя', login, 'не существует')

    def log_out(self):
        print("Пользователь ", self.current_user, "вышел из системы")
        self.current_user = None

    def register(self, nickname, password, age):
        res = ''
        if self.current_user:
            self.log_out()
        reg_user = User( nickname, password, age )
        for item_user in self.users:
            if item_user.nickname == nickname:
                res = 'Пользователь ' + nickname + ' уже существует!'
                return "res"
        self.users.append( reg_user )
        print('Пользователь ', reg_user , "успешно зарегистрирован")
        self.log_in(nickname,password)

    def add(self,*new_video): #Добавление спсика видео
        for item_video in new_video:
            self.videos.append (item_video)

    def get_videos(self,word_search): # поиск названий видео по ключевым словам
        list_video = []
        for item_video in self.videos:
            if item_video.title.lower().find( word_search.lower() ) != -1:
                list_video.append(item_video.title)
        return list_video

    def watch_video(self, word_search): # абсолютный поиск видео и воспроизведение
        dostup = False
        for item_video in self.videos:
            if item_video.title == word_search:
                if item_video.adult_mode:
                    for item_user in self.users:
                        if  self.current_user == item_user :
                            if int(item_user.age) >= 18:
                                print('можно смотреть', self.current_user)
                                dostup = True
                            else:
                                print('Вам нет 18 лет, пожалуйста покиньте страницу', self.current_user)
                else:
                    dostup = True
                if dostup:
                    print( "Воспроизводим видео ", item_video.title )
                    for run_time in range(item_video.duration):
                        print (run_time)
                        sleep(1)
                    print("Конец видео")





class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __str__(self):
        return self.nickname

print("Добро пожаловать на мой YouTube!")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
if not ur.current_user :
    ur.watch_video('Для чего девушкам парень программист?')
else:
    print('Войдите в аккаунт чтобы смотреть видео')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)

# print('Текущий пользователь ' ,ur.current_user)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
#watch_video('Лучший язык программирования 2024 года!')
