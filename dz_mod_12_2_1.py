from runner_and_tournament import Runner
from runner_and_tournament import Tournament
from pprint import pprint
import unittest


class TournamentTest( unittest.TestCase ):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.uein = Runner( "Усэйн", 10 )
        self.andrey = Runner( "Андрей", 9 )
        self.nick = Runner( "Ник", 3 )

    @classmethod
    def tearDownClass(cls):
        pprint( 'Результаты забегов ' )
        for item in list( cls.all_results.values() ):
            print( item )

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test1(self):
        Zabeg1 = Tournament( 90, self.uein, self.nick )
        result = Zabeg1.start()
        self.all_results.update( {"Результат 1 забега": result} )
        self.assertTrue( list( result.values() )[-1] == "Ник" )

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test2(self):
        Zabeg1 = Tournament( 90, self.andrey, self.nick )
        result = Zabeg1.start()
        self.all_results.update( {"Результат 2 забега": result} )
        self.assertTrue( list( result.values() )[-1] == "Ник" )

    @unittest.skipIf( is_frozen, 'Тесты в этом кейсе заморожены' )
    def test3(self):
        Zabeg1 = Tournament( 90, self.uein, self.andrey, self.nick )
        result = Zabeg1.start()
        self.all_results.update( {"Результат 3 забега": result} )
        self.assertTrue( list( result.values() )[-1] == "Ник" )

    @unittest.skipIf( is_frozen, 'Тесты в этом кейсе заморожены' )
    def test4(self):
        Zabeg1 = Tournament( 61, self.andrey, self.uein )
        result = Zabeg1.start()
        self.all_results.update( {"Результат 4 забега": result} )


if __name__ == "__main__":
    unittest.main()
