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