%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Helpers

%isin(X,L) is true if X appears in L
isin(X,[X|_]).
isin(X,[_|T]) :- isin(X,T).

% zip(L1,L2,L3) is true if L3 is the result of interleaving L1 and L2
% e.g. zip([1,2],[3,4],[1,3,2,4])   is true
zip([],[],[]).
zip([H1|T1],[H2|T2],[H1,H2|T]) :- zip(T1,T2,T).

% assoc(L,K,V) is true if L is a list of 2-element lists and one of
% them is [K,V] e.g. assoc([[key1,value1],['a',1],[3,4]], 3, 4) is
% true
assoc([[X,Y]|_],X,Y).
assoc([_|T],X,Y) :- assoc(T,X,Y).

% remove_duplicates(L1,L2) is true if L2 is the result of removing all
% duplicate elements from L1.  The remaining elements should be in the
% original order.  e.g. remove_duplicates([1,1,2,2,3,3,4,4],[1,2,3,4])
% is true
clean([],Soln,Y) :- reverse(Y,Soln).
clean([H|T],Soln,Y) :- isin(H,Y),!,clean(T,Soln,Y).
clean([H|T],Soln,Y) :- clean(T,Soln,[H|Y]).
remove_duplicates(L1,L2) :- clean(L1,L2,[]). 

% union(L1,L2,L3) is true if L3 is the set union of L1 and L2. 
% There should be no duplicates in L3.
% e.g. union([1,2,3],[2,3,4],[1,2,3,4]) is true
union(L1,L2,L3) :- append(L1,L2,L),remove_duplicates(L,L3). 

% intersection(L1,L2,L3) is true if L3 is the set intersection of L1
% and L2.  There should be no duplicates in L3.
% e.g. intersection([1,2,3],[2,3,4],[2,3]) is true
its([],_,X,Y) :- reverse(X,Y).
its([H|T],L,X,Y) :- isin(H,L),!,its(T,L,[H|X],Y).
its([_|T],L,X,Y) :- its(T,L,X,Y).
intersection(L1,L2,L3) :- its(L1,L2,[],L3).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Example: House Negociation.
%
% Basic idea: Willing to negociate with nice clients
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
bottom_line(buyer, 244).
bottom_line(seller, 260).
asking_price(seller, 300).
% Need a starting bid

% individual reasonableness monitor?
interests(buyer, [price, condition]).
interests(seller, [price, sell]). 

% Ontology
% In the future, will want MUTLIPLE parties. 
%sides(house_negociation, [buyer, seller]).
sides(house_negociation, buyer, seller).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Example: Job Negociation.
%
% Basic idea: If by the end of the month, Company X does not make a 
%             satisfactory offer:
%             (1) Take job with company Y
%             (2) Look in another city
%             (3) start own business
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
job_offers(anon, [companyX, companyY]).

starting_salary(companyX, 120).
starting_salary(companyY, 140).

bottom_line(anon, 160).
asking_price(anon, 200). 

benefits(companyX, [stock, vacation, bonus, remote]).
benefits(companyY, [vacation, bonus]).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Rules of negociation
% 1.  wise agreement
% 2.  efficient (does this mean BFS vs DFS)?
% 3.  improve or not damage relationships between parties
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% For now, let's concentrate on just two parties

good_negociate(X,Y) :- wise_agreement(X,Y), efficent_negociation(X,Y),
                       good_relationship(X,Y).


start_negociate(N) :- sides(N, X, Y), asking_price(X, Z),
                       bottom_line(Y, Z), Y>Z.

satisfies_interests(X,Y) :- interests(Y,Z),isin(X,Z).
meets_interests(N) :- bagof(X, negociation(N,X), P), satisfies_interests(_,_).

% N is the negociation 
wise_agreement(N) :- meets_interests(N), resolves_conflicts(N), durable(N),
                     community_intersts(N). 
