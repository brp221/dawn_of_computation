### IMPORTANT: Your program must run on Python 3.7.3 or later
### No libraries may be used 
###
### Author: Hector Munoz-Avila (2018)
### Last update: 4/16/2021, Arielle K. Carr



from PetkovicBratislav318ProjectSkeleton import DFA, PDA, TM, NTM, CoderName, FunctionsCompleted

print(CoderName)

print(FunctionsCompleted)

dfa1 = DFA(
    {'q0','q1'}, # Q
    {'0','1'}, # Sigma
    {'q0':{'0':'q0', '1': 'q1'},
     'q1':{'0':'q1', '1': 'q0'}}, # Delta
    'q0', # q0
    {'q1'} # F
    )

dfa2 = DFA(
    {'q0','q1','q2'}, # Q
    {'0','1'}, # Sigma
    {'q0':{'0':'q2', '1': 'q1'},
     'q2':{'0':'q1', '1': 'q1'},
     'q1':{'0':'q1', '1': 'q0'}}, # Delta
    'q0', # q0
    {'q1'} # F
    )

dfa3 = DFA(
    {'q0','q1','q2', 'q3'}, # Q
    {'0','1'}, # Sigma
    {'q0':{'0':'q2', '1': 'q1'},
     'q2':{'0':'q1', '1': 'q1'},
     'q1':{'0':'q1', '1': 'q0'},
     'q3':{'0':'q1', '1': 'q0'}}, # Delta
    'q0', # q0
    {'q3'} # F
    )

dfa4 = DFA(
    {'q0','q1','q2', 'q3'}, # Q
    {'0','1'}, # Sigma
    {'q0':{'0':'q2', '1': 'q1'},
     'q2':{'0':'q1', '1': 'q1'},
     'q1':{'0':'q1'}, ## Missing entry for q1
     'q3':{'0':'q1', '1': 'q0'}}, # Delta
    'q0', # q0
    {'q3'} # F
    ) ## Bad DFA

dfa5 = DFA(
    {'q0','q1','q2', 'q3'}, # Q
    {'0','1'}, # Sigma
    {'q0':{'0':'q2', '1': 'q1'},
     'q2':{'0':'q5', '1': 'q1'}, ## Not an state
     'q1':{'0':'q1', '1': 'q1'},
     'q3':{'0':'q1', '1': 'q0'}}, # Delta
    'q0', # q0
    {'q3'} # F
    ) ## Bad DFA

dfa6 = DFA(
    {'s','q','r', 'x'}, # Q
    {'0','1'}, # Sigma
    {'s':{'0':'q', '1': 'x'},
     'q':{'0':'q', '1': 'r'},
     'r':{'0':'q', '1': 'x'},
     'x':{'0':'x', '1': 'x'}}, # Delta
    's', # q0
    {'s','q','r'} # F
    )

dfa7 = DFA(
    {'q0','q1','q2'}, # Q
    {'0','1'}, # Sigma
    {'q0':{'0':'q1', '1': 'q2'},
     'q1':{'0':'q1', '1': 'q0'},
     'q2':{'0':'q2', '1': 'q2'}}, # Delta
    'q0', # q0
    {'q0','q1'} # F
    )


#print ("dfa1: ", dfa1.Q, dfa1.Sigma, dfa1.Delta, dfa1.q0, dfa1.F) # should be True

#print ("dfa2: ", dfa2.Q, dfa2.Sigma, dfa2.Delta, dfa2.q0, dfa2.F) # should be True

print ("dfa6: ", dfa6.Q, dfa6.Sigma, dfa6.Delta, dfa6.q0, dfa6.F) # should be True

print ("dfa7: ", dfa7.Q, dfa7.Sigma, dfa7.Delta, dfa7.q0, dfa7.F) # should be True

print ("Equivalece of DFAs dfa1 and dfa2: ", dfa1.EQDFA(dfa2)) # should be False

print ("Equivalece of DFAs dfa6 and dfa7: ", dfa6.EQDFA(dfa7)) # should be True



