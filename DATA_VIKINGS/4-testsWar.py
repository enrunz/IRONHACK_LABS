import unittest
from viking_clases import War
from viking_clases import Viking
from viking_clases import Saxon
from inspect import signature


class TestWar(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.war = War()

    def testWarShouldReciveNoParams(self):
        self.assertEqual(len(signature(War).parameters), 0)

    def testviking_army(self):
        self.assertEqual(self.war.viking_army, [])

    def testsaxon_army(self):
        self.assertEqual(self.war.saxon_army, [])


class TestWar2(unittest.TestCase):
    @classmethod
    def setUp(cls):
        def generateViking():
            cls.name = 'Harald'
            cls.strength = 150
            cls.health = 300
            return Viking(cls.name, cls.health, cls.strength)

        def generateSaxon():
            cls.health = 60
            cls.strength = 25
            return Saxon(cls.health, cls.strength)

        cls.viking = generateViking()
        cls.saxon = generateSaxon()
        cls.war = War()
        cls.war.add_saxon(cls.saxon)
        cls.war.add_viking(cls.viking)

    def testAddViking(self):
        self.assertEqual(callable(self.war.add_viking), True)

    def testAddVikingShouldReceiveOneParam(self):
        self.assertEqual(len(signature(self.war.add_viking).parameters), 1)

    def testAddVikingInList(self):
        self.assertEqual(self.war.viking_army, [self.viking])

    def testAddVikingReturnNull(self):
        self.assertEqual(self.war.add_viking(self.viking), None)

    def testAddSaxonShouldBeFunction(self):
        self.assertEqual(callable(self.war.add_saxon), True)

    def testAddSaxonReceiveOneParam(self):
        self.assertEqual(len(signature(self.war.add_saxon).parameters), 1)

    def testsaxon_armyReturnEmptyList(self):
        self.assertEqual(self.war.saxon_army, [self.saxon])

    def testAddSaxonReturnNone(self):
        self.assertEqual(self.war.add_saxon(self.saxon), None)

    def testVikingAttackIsFunction(self):
        self.assertEqual(callable(self.war.viking_attack), True)

    def testVikingAttackReceiveNoParam(self):
        self.assertEqual(len(signature(self.war.viking_attack).parameters), 0)

    def testSaxonHealth(self):
        oldHealt = self.saxon.health
        self.war.viking_attack()
        self.assertEqual(self.saxon.health, oldHealt - self.viking.strength)

    def testVikingAttack(self):
        self.war.viking_attack()
        self.assertEqual(len(self.war.saxon_army), 0)

    def testAddSaxon(self):
        print(self.war.__dict__)
        self.assertEqual(self.war.viking_attack(),
                         'A Saxon has died in combat')

    def testsaxon_attackIsFunction(self):
        self.assertEqual(callable(self.war.saxon_attack), True)

    def testsaxon_attackReceiveNoParam(self):
        self.assertEqual(len(signature(self.war.saxon_attack).parameters), 0)

    def testVikingHealth(self):
        oldHealt = self.viking.health
        self.war.saxon_attack()
        self.assertEqual(self.viking.health, oldHealt - self.saxon.strength)

    def testviking_armyList(self):
        for i in range(12):
            if(len(self.war.viking_army) == 0):
                break
            self.war.saxon_attack()
        self.assertEqual(len(self.war.viking_army), 0)

    def testReturnOfsaxon_attack(self):
        self.assertEqual(self.war.saxon_attack(), self.viking.name +
                         ' has received ' + str(self.saxon.strength) + ' points of damage')

    def testshow_statusShouldIsFunction(self):
        self.assertEqual(callable(self.war.show_status), True)

    def testshow_statusReceiveNoParams(self):
        self.assertEqual(len(signature(self.war.show_status).parameters), 0)

    def testShouldReturnStringVikingsWon(self):
        self.war.viking_attack()
        self.assertEqual(self.war.show_status(),
                         'Vikings have won the war of the century!')

    def testShouldReturnStringSaxonsWon(self):
        for i in range(12):
            self.war.saxon_attack()
        self.assertEqual(self.war.show_status(
        ), 'Saxons have fought for their lives and survive another day...')

    def testShouldReturnStringStillFighting(self):
        self.assertEqual(
            self.war.show_status(), 'Vikings and Saxons are still in the thick of battle.')


if __name__ == '__main__':
    unittest.main()
