### IMPORTANT: Your program must run on Python 3.7.3 or later
### No libraries may be used 
###
### Author: Hector Munoz-Avila (2018)
### Last update: 4/16/2021, Arielle K. Carr



from PetkovicBratislav318ProjectSkeleton import DFA, PDA, TM, NTM, CoderName, FunctionsCompleted

print(CoderName)

print(FunctionsCompleted)


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

#print ("ntm1: ", ntm1.Q, ntm1.Sigma, ntm1.Gamma, ntm1.Delta, ntm1.q0, ntm1.qAccept )
print("------------------------------------------------------------------------")
print("Acceptance NTM ntm2 00000: ",ntm2.acceptNTM(['0','0','0','0','0'],100)) # should be True
print("------------------------------------------------------------------------")
#print ("ntmPAL: ", ntmPAL.Q, ntmPAL.Sigma, ntmPAL.Gamma, ntmPAL.Delta, ntmPAL.q0, ntmPAL.qAccept)
print ("Acceptance NTM ntm1 10011: ",ntm1.acceptNTM(['1','0','0','1','1'],100)) # should be True
print("------------------------------------------------------------------------")
#print ("Acceptance NTM ntmPAL 0: ",ntmPAL.acceptNTM(['0'],1000)) # should be True
#print ("Acceptance NTM ntmPAL 00: ",ntmPAL.acceptNTM(['0','0'],1000)) # should be True
#print ("Acceptance NTM ntmPAL 11011: ",ntmPAL.acceptNTM(['1','1','0','1','1'],1000)) # should be True
#print ("Acceptance NTM ntmPAL 1101: ",ntmPAL.acceptNTM(['1','1','0','1'],100)) # should be False
#print ("ntmPAL2: ", ntmPAL2.Q, ntmPAL2.Sigma, ntmPAL2.Gamma, ntmPAL2.Delta, ntmPAL2.q0, ntmPAL2.qAccept)
#print ("Acceptance NTM ntmPAL2 0: ",ntmPAL2.acceptNTM(['0'],1000)) # should be True
#print ("Acceptance NTM ntmPAL2 00: ",ntmPAL2.acceptNTM(['0','0'],1000)) # should be True
#print ("Acceptance NTM ntmPAL2 11011: ",ntmPAL2.acceptNTM(['1','1','0','1','1'],1000)) # should be True
print("------------------------------------------------------------------------")
print ("Acceptance NTM ntmPAL2 1101: ",ntmPAL2.acceptNTM(['1','1','0','1'],100)) # should be False
