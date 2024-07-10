def is_prime(func):
    def wrapper(*args):
        original_result = func( *args )
        if original_result <= 3:
            print( "Простое" )
            return original_result
        if original_result % 2 == 0:
            print( "Составное" )
            return original_result
        f = int( original_result ** 0.5 ) + 1
        for i in range( 3, original_result - 1 ):
            if original_result % i == 0:
                print( "Составное" )
                return original_result
            print( "Простое" )
            return original_result

    return wrapper


@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res


result = sum_three( 2, 3, 6 )
print( result )
