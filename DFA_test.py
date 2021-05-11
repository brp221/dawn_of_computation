### IMPORTANT: Your program must run on Python 3.7.3 or later
### No libraries may be used 
###
### Author: Hector Munoz-Avila (2018)
### Last update: 4/16/2021, Arielle K. Carr



from PetkovicBratislav318ProjectSkeleton import DFA, PDA, TM, NTM, CoderName, FunctionsCompleted

print(CoderName)

print(FunctionsCompleted)

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

#print ("tm1: ", tm1.Q, tm1.Sigma, tm1.Gamma, tm1.Delta, tm1.q0, tm1.qAccept, tm1.qReject)

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

#print ("tmPAL: ", tmPAL.Q, tmPAL.Sigma, tmPAL.Gamma, tmPAL.Delta, tmPAL.q0, tmPAL.qAccept, tmPAL.qReject)

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

#print ("tm2: ", tm2.Q, tm2.Sigma, tm2.Gamma, tm2.Delta, tm2.q0, tm2.qAccept, tm2.qReject)

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

#print ("tm3: ", tm3.Q, tm3.Sigma, tm3.Gamma, tm3.Delta, tm3.q0, tm3.qAccept, tm3.qReject)

print ("verify TM tm3: ",tm3.verifyTM()) # should be False

print ("Acceptance TM tm1 10011: ",tm1.acceptTM(['1','0','0','1','1'],100)) # should be True
print("--------------------------------------------------------------------------")
print ("Acceptance TM tm1 1111:",tm1.acceptTM(['1','1','1','1'],100)) # should be False
print("--------------------------------------------------------------------------")
print ("Acceptance TM tmPAL 0: ",tmPAL.acceptTM(['0'],1000)) # should be True
print("--------------------------------------------------------------------------")
print ("Acceptance TM tmPAL 00: ",tmPAL.acceptTM(['0','0'],1000)) # should be True
print("--------------------------------------------------------------------------")
print ("Acceptance TM tmPAL 11011: ",tmPAL.acceptTM(['1','1','0','1','1'],1000)) # should be True
print("--------------------------------------------------------------------------")
print ("Acceptance TM tmPAL 1101: ",tmPAL.acceptTM(['1','1','0','1'],1000)) # should be False