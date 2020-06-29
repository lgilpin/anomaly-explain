%% Techniques of Prolog Programming by T. Van Le) A farmer has a wolf, a
%% goat, and a cabbage on the north side of the river, and also a small
%% boat.  He wants to bring his property to the south side of the river,
%% but the boat can only carry himself and at most one of the three. The
%% problem is that if he leaves the wolf with the goat unattended then he
%% will have no more goat; also if the goat is left behind with the
%% cabbage, then the cabbage will be finished. How can the farmer bring
%% his property to the south side of the river?  In this problem there
%% are four relevant entries: the farmer, wolf, goat, and cabbage.  The
%% problem state can be represented by a list of four variables for the
%% farmer, wolf, goat, cabbage.  [F,W,G,C]

%% Each of these entities can have only two states: "n" or "s" for
%% north or south side of the river.  The initial state is when all
%% the entities are on the north side, and the final state is when
%% they are on the south side.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Initial data

initial_state([n,n,n,n]).  % each entity is on the north side.
final_state([s,s,s,s]).  % each is on the south side.

next_state(S,S1) :- move(S,S1), safe(S1).  % move from S to S1 if S1 is safe

move([F,W,G,C], [F1,W,G,C]) :- cross(F,F1).  % farmer crosses alone
move([F,F,G,C], [F1,F1,G,C]) :- cross(F,F1). % farmer and wolf cross
move([F,W,F,C], [F1,W,F1,C]) :- cross(F,F1). % farmer and goat cross
move([F,W,G,F], [F1,W,G,F1]) :- cross(F,F1). % farmer and cabbage cross
/*
Note: for the Jealous Husband or Missionaries problems you may need to 
keep track of where the boat is also.
 For example: move([F,F,G,C,F], [F1,F1,G,C,F1]).
   This uses another "field" for the location of the boat.

*/

safe([F,W,G,C]) :- F = G, !.
safe([F,W,G,C]) :- F = W, F = C.  
   		% Safe if either Farmer and Goat are together or
		% Farmer is with Wolf and Cabbage

cross(n,s).
cross(s,n).

depth_first_search(AnsPath) :-
    initial_state(Init),
    depth_first([Init], AnsPath).

depth_first([S|Path], [S]) :-
    final_state(S), !.
depth_first([S|Path], [S|AnsPath]) :-
%write('Extending '),write([S|Path]),nl,     Sample Tracing 
    extend([S|Path], S1),
    %write('Next path: '), write(S1), nl,        Sample Tracing
depth_first([S1,S|Path], AnsPath).

extend([S|Path], S1) :-
    next_state(S,S1),
    not(member_state(S1, [S|Path])).

member_state(S, [S|_]).
member_state(X, [_|T]) :- member_state(X,T).

% If you want to collect all the answer paths:
go(AllPaths) :-
    bagof(AnsPath, depth_first_search(AnsPath), AllPaths).

%% Sample output:
%% | ?- depth_first_search(Ans).
%% Ans = [[n,n,n,n],[s,n,s,n],[n,n,s,n],[s,s,s,n],[n,s,n,n],[s,s,n,s],[n,s,n,s],[s,s,s,s]] ? ;
%% Ans = [[n,n,n,n],[s,n,s,n],[n,n,s,n],[s,n,s,s],[n,n,n,s],[s,s,n,s],[n,s,n,s],[s,s,s,s]] 
