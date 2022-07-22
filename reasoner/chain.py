from typing import List

from commonsense.logical_classes import Fact

import pprint

pp = pprint.PrettyPrinter(indent=1)
pprint = pp.pprint

def forward_chain(facts, rules=None):
    """
    Creates a new set of
    :param facts:
    :type facts:
    :param rules:
    :type rules:
    :return:
    :rtype:
    """
    new_facts = facts
    is_changed = True
    while is_changed:
        is_changed = False
        for fact1 in new_facts:
            for fact2 in new_facts[1::]:
                if fact1.object == fact2.subject and fact1.predicate == fact2.predicate:
                    new_fact = Fact(fact1.subject, fact1.predicate, fact2.object)
                    if new_fact not in new_facts:
                        new_facts.append(Fact(fact1.subject, fact1.predicate, fact2.object, reason="Rule triggered"))
                        is_changed = True
                        break
    return new_facts


def chain_explanation(facts: List[Fact], query: Fact, chain = [], verbose=False):
    """
    Almost a backwards chain.

    :param facts:
    :type facts:
    :param query:
    :type query:
    :return:
    :rtype:
    """
    if chain is None:
        return []
    if chain == []:   # starting so we need a fact
        if verbose:
            print("chain is nothing adding more")
        for f in facts:
            if f.subject == query.subject:
                return chain_explanation(facts, query, [f], verbose)
    else:
        # First find all those ending in the query
        # get the last in the chain
        if verbose:
            print("has a chain, currently is %s"%chain)
        new_query = chain[-1]
        for fact in facts:
            if fact.subject == new_query.object:
                # check if we're done!
                if fact.object == query.object: # and len(chain) > 1:  # we're done! (also need to check it's not the null explanation).
                    chain.append(fact)
                    return chain
                return chain_explanation(facts, query, chain + [fact], verbose)

def summarize(facts: List[Fact], all_facts: List[Fact] = None, important_fact:str = None):
    summary = ""
    important_fact = facts[-1]
    for fact in facts:
        # if fact.subject == important_fact:
        if summary != "":
            summary += ", (%s)"%fact.to_string()
        else:
            summary = "(%s)"%fact.to_string()
    if all_facts:
        for fact in all_facts:
            if fact.subject == important_fact.subject and fact not in facts:  # Additional summarization
                summary += ", (%s)" % fact.to_string()
    return summary


