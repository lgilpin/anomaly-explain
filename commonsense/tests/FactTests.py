from commonsense.logical_classes import Fact
import pandas as pd

def test_initialization():
    fact = Fact('penguin', 'isA', 'bird')
    assert (fact.subject == 'penguin'), "Subject incorrectly initialized in fact"
    assert (fact.predicate == 'isA'), "Predicate incorrectly initialized in fact"
    assert (fact.object == 'bird'), "Object incorrectly initialized in fact"
    assert (fact.reason is None), "Reason incorrectly initialized in fact"
    assert (fact.score == 1.0), "Score incorrectly initialized in fact"

    print("Fact initialization test passed")

    pass


def test_get_infix_fact_list():
    fact = Fact('penguin', 'isA', 'bird')
    infixList = fact.get_infix_fact_list()

    assert (len(infixList) == 3), "list of incorrect size returned by get_infix_fact_list"
    assert (infixList[0] == [fact.subject, fact.predicate, fact.object]), "Incorrect value, should be of the following form [subject, predicate, object]"
    assert (infixList[1] == fact.reason), "Incorrect value, should be fact reason"
    assert (infixList[2] == fact.score), "Incorrect value, should be fact score"

    print("get_infix_fact_list test passed")

    pass

def test_to_data_frame():
    fact = Fact('penguin', 'isA', 'bird')
    dataframe = fact.to_data_frame()

    assert(type(dataframe) is pd.DataFrame), "to_data_frame returned an incorrect type"

    print('\n', dataframe, '\n')

    print("to_data_frame test passed")

    pass

if __name__ == "__main__":
    test_initialization()
    test_get_infix_fact_list()
    test_to_data_frame()
    print("All tests passed")
