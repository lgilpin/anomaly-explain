from unittest import TestCase
from monitor import reasonableness_monitor as monitor
from commonsense.conceptnet import Fact

class TestSnapshotMonitor(TestCase):
    def test_explain_fact(self):
        test_monitor = monitor.SnapshotMonitor()
        starter_fact = Fact("penguin", "IsA", "animal")

        test_monitor.explain_fact(starter_fact) # List of facts with fact object.
        # self.fail()

