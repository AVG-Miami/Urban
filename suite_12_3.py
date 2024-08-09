import unittest
import dz_mod_12_2
import dz_mod_12_1

testST=unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(dz_mod_12_1.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(dz_mod_12_2.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)