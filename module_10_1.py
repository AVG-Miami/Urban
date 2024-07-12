from threading import Thread
from datetime import datetime
from time import sleep


def wite_words(word_count, file_name):
    with open( file_name, encoding="utf-8", mode='w' ) as file:
        for i in range( 1, word_count + 1 ):
            s = 'Какое-то слово №' + str( i ) + '\n'
            file.writelines( s )
            sleep( 0.1 )
    print( "Завершилась запись в файл ", file_name )


# Без использование потоков
time_start = datetime.now()
wite_words( 10, "example1.txt" )
wite_words( 30, "example2.txt" )
wite_words( 200, "example3.txt" )
wite_words( 100, "example4.txt" )
time_end = datetime.now()
time_res = time_end - time_start
print( "Работа в 1 поток", time_res )
print( "" )

# Использование потоков
time_start = datetime.now()

thr_1 = Thread( target=wite_words, args=(10, "example5.txt") )
thr_2 = Thread( target=wite_words, args=(30, "example6.txt") )
thr_3 = Thread( target=wite_words, args=(200, "example7.txt") )
thr_4 = Thread( target=wite_words, args=(100, "example8.txt") )

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end = datetime.now()
time_res = time_end - time_start

print( "Работа потоков", time_res )
