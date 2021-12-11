from typing import List
from commonsense.logical_classes import Fact

class KB:
		
	# e.g., (isa Pill foo)
	# predicate - relation (e.g., isa)
	# concept - object being searched for
	# source - (reasons) source or other debugging tool indicating types of data
	# returns a list of concepts
	# (isa Pill Consumable) (predicate concept ?var)
	# NextKB - retrieve references (filter on predicate)
	# ConceptNet - search
	def search_for_concept(self, predicate, concept, source):
		pass

	# go up the isa hierarchy to find the closest parent from a set of anchors
	# concept - concept for which to find an anchor
	# anchors - set of possible anchors, one should be the closest parent
	def find_closest_anchor(self, concept_phrase, anchors, include_score: bool):
		pass


	def clean(self, concept: str) -> str:
		"""
		Strings/ concepts are treated differently in ConceptNet/NextKB (with capitalization).

		:param concept: The concept to prepare and clean.
		:type concept: str
		:return: The cleaned string for the particular KB
		:rtype: str
		"""
		pass

	def aggregate(self, fact: Fact, relations: List, reason: str = "") -> List[Fact]:
		"""
		Aggregates commonsense reasons for a particular concept and the relations of interest.

		:param fact_term: The fact (the fact's subject) to search for.
		:type fact_term: str
		:param relations: The list of predicates to search for
		:type relations: List[str]
		:param reason: A reason for the search (probably the name of the KB)
		:type reason: str
		:return: A list of facts aggregated for each predicate in the list of relations.
		:rtype: List[Fact]
		"""
		all_facts = []
		for relation in relations:
			# new_facts = self.search(self.clean(fact.subject), relation, reason=reason)
			new_facts = self.search(fact.subject, relation, reason=reason)
			all_facts.extend(new_facts)
		return all_facts