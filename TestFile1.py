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


print ("dfa1: ", dfa1.Q, dfa1.Sigma, dfa1.Delta, dfa1.q0, dfa1.F) # should be True

print ("dfa2: ", dfa2.Q, dfa2.Sigma, dfa2.Delta, dfa2.q0, dfa2.F) # should be True

print ("verify DFA dfa1: ",dfa1.verifyDFA()) # should be True

print ("verify DFA dfa4: ",dfa4.verifyDFA()) # should be False

print ("verify DFA dfa5: ",dfa5.verifyDFA()) # should be False

print ("verify DFA dfa6: ",dfa6.verifyDFA()) # should be True

print ("verify DFA dfa7: ",dfa7.verifyDFA()) # should be True

print ("Acceptance DFA dfa1: ","10011", " ", dfa1.acceptDFA('10011')) # should be True

print ("Acceptance DFA dfa1: ","1111", " ", dfa1.acceptDFA('1111')) # should be False

print ("Acceptance DFA dfa2: ","10011", " ", dfa2.acceptDFA('10011')) # should be True

print ("Acceptance DFA dfa2: ","1111", " ", dfa2.acceptDFA('1111')) # should be False

print ("Acceptance DFA dfa6: ","0101010", " ", dfa6.acceptDFA('0101010')) # should be True

print ("Acceptance DFA dfa7: ","0101010", " ", dfa7.acceptDFA('0101010')) # should be True


print ("Empty DFA dfa1", dfa1.emptyDFA()) # should be false

print ("Empty DFA dfa3", dfa3.emptyDFA()) # should be true


print ("Equivalece of DFAs dfa1 and dfa2: ", dfa1.EQDFA(dfa2)) # should be False

print ("Equivalece of DFAs dfa6 and dfa7: ", dfa6.EQDFA(dfa7)) # should be True


pda1 = PDA(
    {'q1','q2','q3','q4'}, # Q
    {'0','1'}, # Sigma; may not contain 'e', which we use to denote the empty string
    {'0','$'}, # Gamma; may not contain 'e', which we use to denote the empty string
    {'q1':{'e': [['q2','e','$']], '0': [], '1': []},
     'q2':{'e': [], '0': [['q2','e','0']], '1': [['q3','0','e']]},
     'q3':{'1': [['q3','0','e']], 'e': [['q4','$','e']], '0': []},
     'q4':{'e': [], '0': [], '1': []}
    }, # Delta
    'q1', # q0
    {'q1','q4'} # F
    )

pda1A = PDA(
    {'q1','q2','q3','q4'}, # Q
    {'0','1'}, # Sigma; may not contain 'e', which we use to denote the empty string
    {'0','$'}, # Gamma; may not contain 'e', which we use to denote the empty string
    {'q1':{'e': [['q2','e','$']], '0': [], '1': []},
     'q2':{'e': [], '0': [['q2','e','0']], '1': [['q3','0','e']]},
     'q3':{'1': [['q3','0','e']], 'e': [['q4','$','e']], '0': []},
     'q4':{'e': [], '0': [], '1': []}
    }, # Delta
    'q1', # q0
    {'q4'} # F
    )

print ("pda1: ", pda1.Q, pda1.Sigma, pda1.Gamma, pda1.Delta, pda1.q0, pda1.F)


pda2 = PDA(
    {'q1','q2','q3','q4'}, # Q
    {'0','1'}, # Sigma; may not contain 'e', which we use to denote the empty string
    {'0','$'}, # Gamma; may not contain 'e', which we use to denote the empty string
    {'q1':{'e': [['q2','e','$']], '0': [], '1': []},
     'q2':{'0': [['q2','e','0'],['q3','e','0']], '1': [['q3','0','e']], 'e': []},
     'q3':{'1': [['q3','0','e']], 'e': [['q4','$','e']], '0': []},
     'q4':{'e': [], '0': [], '1': []}
    }, # Delta
    'q1', # q0
    {'q4'} # F
    )



print ("pda2: ", pda2.Q, pda2.Sigma, pda2.Gamma, pda2.Delta, pda2.q0, pda2.F)

print ("verify PDA pda1: ",pda1.verifyPDA()) # should be True

print ("verify PDA pda2: ",pda2.verifyPDA()) # should be True

pda3 = PDA(
    {'q1','q2','q3','q4'}, # Q
    {'0','1'}, # Sigma; may not contain 'e', which we use to denote the empty string
    {'0','$'}, # Gamma; may not contain 'e', which we use to denote the empty string
    {'q1':{'e': [['q2','e','$']], '0': []}, ##Bad: no transtition for '1'
     'q2':{'0': [['q2','e','0'],['q3','e','0']], '1': [['q3','0','e']], 'e': []},
     'q3':{'1': [['q3','0','e']], 'e': [['q4','$','e']], '0': []},
     'q4':{}
    }, # Delta
    'q1', # q0
    {'q4'} # F
    ) ## Bad PDA

print ("pda3: ", pda3.Q, pda3.Sigma, pda3.Gamma, pda3.Delta, pda3.q0, pda3.F)

print ("verify PDA pda3: ",pda3.verifyPDA()) # should be False

print ("Acceptance PDA pda1: ","0011", " ", pda1.acceptPDA('0011')) # should be True

print ("Acceptance PDA pda1: ","001", " ", pda1.acceptPDA('001')) # should be False

print ("Acceptance PDA pda1: ","", " ", pda1.acceptPDA('')) # should be True


print ("Acceptance PDA pda2: ","0011", " ", pda2.acceptPDA('0011')) # should be True

print ("Acceptance PDA pda2: ","001", " ", pda2.acceptPDA('001')) # should False

print ("Acceptance PDA pda2: ","", " ", pda2.acceptPDA('')) # should be false

print ("Acceptance PDA pda1A: ","0011", " ", pda1A.acceptPDA('0011')) # should be True

print ("Acceptance PDA pda1A: ","001", " ", pda1A.acceptPDA('001')) # should False

print ("Acceptance PDA pda1A: ","", " ", pda1A.acceptPDA('')) # should be false


print ("Not equivalent PDAs pda1 and pda2: ", pda1.notEQPDA(pda2,10)) # should be True

print ("Not equivalent PDAs pda2 and pda2: ", pda2.notEQPDA(pda2,10)) # should be False

print ("Not equivalent PDAs pda1 and pda1A: ", pda1.notEQPDA(pda1A,10)) # should be True

print ("Not equivalent PDAs pda1A and pda2: ", pda1A.notEQPDA(pda2,10)) # should be False

tm1 = TM(
    {'q0','q1','accept','reject'}, # Q
    {'0','1'}, # Sigma
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank
    {'q0':{'0': ['q0','0','R'], '1': ['q1','1','R'], '_': ['reject','_','L']},
     'q1':{'0': ['q1','0','R'], '1': ['q0','1','R'], '_': ['accept','_','L']},
    }, # Delta
    'q0', # q0
    'accept', #qAccept
    'reject' #qReject
    )

print ("tm1: ", tm1.Q, tm1.Sigma, tm1.Gamma, tm1.Delta, tm1.q0, tm1.qAccept, tm1.qReject)

print ("verify TM tm1: ",tm1.verifyTM()) # should be True

tmPAL = TM(
    {'q0','q1','qRight0','accept','reject', 'qRight1', 'qSearch0L', 'qSearch1L', 'qSearch0R', 'qSearch1R', 'qLeft0', 'qLeft1'}, # Q
    {'0','1'}, # Sigma
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank
    {'q0':{'0': ['qRight0','_','R'], '1': ['qRight1','_','R'], '_': ['accept','_','R']},
     'q1':{'0': ['qLeft0','_','L'], '1': ['qLeft1','_','L'], '_': ['accept','_','R']},
     'qRight0':{'0': ['qRight0','0','R'], '1': ['qRight0','1','R'], '_': ['qSearch0L','_','L']},
     'qRight1':{'0': ['qRight1','0','R'], '1': ['qRight1','1','R'], '_': ['qSearch1L','_','L']},
     'qSearch0L':{'0': ['q1','_','L'], '1': ['reject','1','R'], '_': ['accept','_','R']},
     'qSearch1L':{'0': ['reject','0','R'], '1': ['q1','_','L'], '_': ['accept','_','R']},
     'qSearch0R':{'0': ['q0','_','R'], '1': ['reject','1','R'], '_': ['accept','_','R']},
     'qSearch1R':{'0': ['reject','0','R'], '1': ['q0','_','R'], '_': ['accept','_','R']},
     'qLeft0':{'0': ['qLeft0','0','L'], '1': ['qLeft0','1','L'], '_': ['qSearch0R','_','R']},
     'qLeft1':{'0': ['qLeft1','0','L'], '1': ['qLeft1','1','L'], '_': ['qSearch1R','_','R']}
    }, # Delta
    'q0', # q0
    'accept', #qAccept
    'reject' #qReject
    )

print ("tmPAL: ", tmPAL.Q, tmPAL.Sigma, tmPAL.Gamma, tmPAL.Delta, tmPAL.q0, tmPAL.qAccept, tmPAL.qReject)

print ("verify TM tmPAL: ",tmPAL.verifyTM()) # should be True

tm2 = TM(
    {'q0','q1','accept','reject'}, # Q
    {'0','1'}, # Sigma
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank
    {'q0':{'0': ['q0','0','R'], '1': ['q1','1','R']}, ##Bad: Missing transition for '_'
     'q1':{'0': ['q1','0','R'], '1': ['q0','1','R'], '_': ['accept','_','L']},
    }, # Delta
    'q0', # q0
    'accept', #qAccept
    'reject' #qReject
    ) ## BAD TM

print ("tm2: ", tm2.Q, tm2.Sigma, tm2.Gamma, tm2.Delta, tm2.q0, tm2.qAccept, tm2.qReject)

print ("verify TM tm2: ",tm2.verifyTM()) # should be False

tm3 = TM(
    {'q0','q1','accept','reject'}, # Q
    {'0','1'}, # Sigma
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank
    {'q0':{'0': ['q0','0','R'], '1': ['q1','1','R'], '_': ['reject','_','L']}
    }, # Delta'; BAD: no transitions for 'q1'
    'q0', # q0
    'accept', #qAccept
    'reject' #qReject
    )

print ("tm3: ", tm3.Q, tm3.Sigma, tm3.Gamma, tm3.Delta, tm3.q0, tm3.qAccept, tm3.qReject)

print ("verify TM tm3: ",tm3.verifyTM()) # should be False

print ("Acceptance TM tm1 10011: ",tm1.acceptTM(['1','0','0','1','1'],100)) # should be True

print ("Acceptance TM tm1 1111:",tm1.acceptTM(['1','1','1','1'],100)) # should be False


print ("Acceptance TM tmPAL 0: ",tmPAL.acceptTM(['0'],1000)) # should be True

print ("Acceptance TM tmPAL 00: ",tmPAL.acceptTM(['0','0'],1000)) # should be True

print ("Acceptance TM tmPAL 11011: ",tmPAL.acceptTM(['1','1','0','1','1'],1000)) # should be True

print ("Acceptance TM tmPAL 1101: ",tmPAL.acceptTM(['1','1','0','1'],1000)) # should be False


ntm1 = NTM(
    {'q0','q1','accept'}, # Q
    {'0','1'}, # Sigma; may  not contain '_', which we use for the blank symbol
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank;
    {'q0':{'0': [['q0','0','R']], '1': [['q1','1','R']], '_': []},
     'q1':{'0': [['q1','0','R']], '1': [['q0','1','R']], '_': [['accept','_','L']]},
    }, # Delta
    'q0', # q0
    'accept', #qAccept
    )


print ("ntm1: ", ntm1.Q, ntm1.Sigma, ntm1.Gamma, ntm1.Delta, ntm1.q0, ntm1.qAccept )

print ("verify NTM ntm1: ",ntm1.verifyNTM()) # should be True

print ("Acceptance NTM ntm1 10011: ",ntm1.acceptNTM(['1','0','0','1','1'],100)) # should be True

ntm2 = NTM(
    {'q0','q1','accept'}, # Q
    {'0','1'}, # Sigma; may   not contain '_', which we use for the blank symbol
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank
    {'q0':{'0': [['q0','0','R'],['q1','0','R']], '1': [['q0','1','L'],['q1','1','L']], '_': []},
     'q1':{'_': [['accept','_','L']], '0': [], '1': []},
    }, # Delta
    'q0', # q0
    'accept', #qAccept
    )

print ("verify NTM ntm2: ",ntm2.verifyNTM()) # should be True

ntm3 = NTM(
    {'q0','q1','accept'}, # Q
    {'0','1'}, # Sigma; may   not contain '_', which we use for the blank symbol
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank
    {'q0':{'0': [['q0','0','R'],['q1','0','R']], '1': [['q0','1','L'],['q1','1','L']], '_': []},
     'q1':{'_': [['accept','_','L']], '1': []}, ### BAD: Missing transition for '0'
    }, # Delta
    'q0', # q0
    'accept', #qAccept
    ) ## BAD NTM

print ("verify NTM ntm3: ",ntm3.verifyNTM()) # should be False

print ("Acceptance NTM ntm2 00000: ",ntm2.acceptNTM(['0','0','0','0','0'],100)) # should be True


ntmPAL = NTM(
    {'q0','q1','qRight0','accept','qRight1', 'qSearch0L', 'qSearch1L', 'qSearch0R', 'qSearch1R', 'qLeft0', 'qLeft1'}, # Q
    {'0','1'}, # Sigma
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank
    {'q0':{'0': [['qRight0','_','R']], '1': [['qRight1','_','R']], '_': [['accept','_','R']]},
     'q1':{'0': [['qLeft0','_','L']], '1': [['qLeft1','_','L']], '_': [['accept','_','R']]},
     'qRight0':{'0': [['qRight0','0','R']], '1': [['qRight0','1','R']], '_': [['qSearch0L','_','L']]},
     'qRight1':{'0': [['qRight1','0','R']], '1': [['qRight1','1','R']], '_': [['qSearch1L','_','L']]},
     'qSearch0L':{'0': [['q1','_','L']], '1': [], '_': [['accept','_','R']]},
     'qSearch1L':{'0': [], '1': [['q1','_','L']], '_': [['accept','_','R']]},
     'qSearch0R':{'0': [['q0','_','R']], '1': [], '_': [['accept','_','R']]},
     'qSearch1R':{'0': [], '1': [['q0','_','R']], '_': [['accept','_','R']]},
     'qLeft0':{'0': [['qLeft0','0','L']], '1': [['qLeft0','1','L']], '_': [['qSearch0R','_','R']]},
     'qLeft1':{'0': [['qLeft1','0','L']], '1': [['qLeft1','1','L']], '_': [['qSearch1R','_','R']]}
    }, # Delta
    'q0', # q0
    'accept', #qAccept
    )

print ("ntmPAL: ", ntmPAL.Q, ntmPAL.Sigma, ntmPAL.Gamma, ntmPAL.Delta, ntmPAL.q0, ntmPAL.qAccept)

print ("verify TM tmPAL: ",ntmPAL.verifyNTM()) # should be True

print ("Acceptance NTM ntmPAL 0: ",ntmPAL.acceptNTM(['0'],1000)) # should be True

print ("Acceptance NTM ntmPAL 00: ",ntmPAL.acceptNTM(['0','0'],1000)) # should be True

print ("Acceptance NTM ntmPAL 11011: ",ntmPAL.acceptNTM(['1','1','0','1','1'],1000)) # should be True

print ("Acceptance NTM ntmPAL 1101: ",ntmPAL.acceptNTM(['1','1','0','1'],100)) # should be False


ntmPAL2 = NTM(
    {'q0','q1','qRight0','accept','qRight1', 'qSearch0L', 'qSearch1L', 'qSearch0R', 'qSearch1R', 'qLeft0', 'qLeft1'}, # Q
    {'0','1'}, # Sigma
    {'0','1','_'}, # Gamma; '_" is the symbol that must be used for blank
    {'q0':{'0': [['qRight0','_','R'],['q0','0','R']], '1': [['qRight1','_','R']], '_': [['accept','_','R']]},
     'q1':{'0': [['qLeft0','_','L']], '1': [['qLeft1','_','L']], '_': [['accept','_','R']]},
     'qRight0':{'0': [['qRight0','0','R']], '1': [['qRight0','1','R']], '_': [['qSearch0L','_','L']]},
     'qRight1':{'0': [['qRight1','0','R']], '1': [['qRight1','1','R']], '_': [['qSearch1L','_','L']]},
     'qSearch0L':{'0': [['q1','_','L']], '1': [], '_': [['accept','_','R']]},
     'qSearch1L':{'0': [], '1': [['q1','_','L']], '_': [['accept','_','R']]},
     'qSearch0R':{'0': [['q0','_','R']], '1': [], '_': [['accept','_','R']]},
     'qSearch1R':{'0': [], '1': [['q0','_','R']], '_': [['accept','_','R']]},
     'qLeft0':{'0': [['qLeft0','0','L']], '1': [['qLeft0','1','L']], '_': [['qSearch0R','_','R']]},
     'qLeft1':{'0': [['qLeft1','0','L']], '1': [['qLeft1','1','L']], '_': [['qSearch1R','_','R']]}
    }, # Delta
    'q0', # q0
    'accept', #qAccept
    )

print ("ntmPAL2: ", ntmPAL2.Q, ntmPAL2.Sigma, ntmPAL2.Gamma, ntmPAL2.Delta, ntmPAL2.q0, ntmPAL2.qAccept)

print ("verify TM tmPAL2: ",ntmPAL2.verifyNTM()) # should be True

print ("Acceptance NTM ntmPAL2 0: ",ntmPAL2.acceptNTM(['0'],1000)) # should be True

print ("Acceptance NTM ntmPAL2 00: ",ntmPAL2.acceptNTM(['0','0'],1000)) # should be True

print ("Acceptance NTM ntmPAL2 11011: ",ntmPAL2.acceptNTM(['1','1','0','1','1'],1000)) # should be True

print ("Acceptance NTM ntmPAL2 1101: ",ntmPAL2.acceptNTM(['1','1','0','1'],100)) # should be False
