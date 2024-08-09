# from runner \
from runner import Runner
import unittest


class RunnerTest( unittest.TestCase ):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run1 = Runner( "run1" )
        for i in range( 10 ):
            run1.walk()
        self.assertEqual( run1.distance, 50 )

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        run2 = Runner( "run2" )
        for i in range( 10 ):
            run2.run()
        self.assertEqual( run2.distance, 100 )

    @unittest.skipIf( is_frozen, 'Тесты в этом кейсе заморожены' )
    def test_chalenge(self):
        run3 = Runner( "run3" )
        run4 = Runner( "run4" )
        for i in range( 11 ):
            run3.run()
            run4.walk()
        self.assertNotEqual( run3.distance, run4.distance )


if __name__ == "__main__":
    unittest.main()
