import unittest
import HtmlTestRunner

from Sesiunea_4_Libraria_UnitTest.main import TestElefant
from Sesiunea_5_Alerte_Suite.alerte import TestAlerts


class TestSuite(unittest.TestCase):
    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts)
            # unittest.defaultTestLoader.loadTestsFromTestCase(TestElefant)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Unit Tests Results',
            report_name='unittests_report'
        )
        runner.run(teste_de_rulat)
