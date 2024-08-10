# from runner \
import logging
from rt_with_exceptions import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run1 = Runner("run1", -5)
            for i in range(10):
                run1.walk()
            self.assertEqual(run1.distance, 50)
            logging.info('"test_walk" выполнен успешно')

        except ValueError as err:
            logging.warning("Неверная -скорость для Runner ", exc_info=True)

    def test_run(self):
        try:
            run2 = Runner(2, 5)
            for i in range(10):
                run2.run()
            self.assertEqual(run2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_chalenge(self):
        run3 = Runner("run3")
        run4 = Runner("run4")
        for i in range(11):
            run3.run()
            run4.walk()
        self.assertNotEqual(run3.distance, run4.distance)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding="utf8", format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()
