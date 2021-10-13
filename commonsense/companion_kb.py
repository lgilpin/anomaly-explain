class CompanionKB(KB):

	def __init__(self):
		NEXT_KB = NextKBAgent.parse_command_line_args()
		default_mt = "PaxMt"

	def search_for_concept(self, predicate, concept, source):
		refs = NEXT_KB.retrieve_references(concept, default_mt, False)
		## then filter on predicate
		return filter(lambda x: x.head() == predicate, refs)


	def find_closest_anchor(self, concept_phrase, anchors, include_score: bool):
		for anchor in anchors:
        	if anchor in concept_phrase:
        		triple = [concept_phrase, 'IsA', anchor]
	            return make_fact(triple, "direct search")

        # (isa Pill ?x)
        # (nonTransitiveInference (isa concept ?x))
        # 	(nonTransitiveInference (genls ?x ?y))
        # 		until y = anchor
