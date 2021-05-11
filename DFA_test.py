### IMPORTANT: Your program must run on Python 3.7.3 or later
### No libraries may be used 
###
### Author: Hector Munoz-Avila (2018)
### Last update: 4/16/2021, Arielle K. Carr



from PetkovicBratislav318ProjectSkeleton import DFA, PDA, TM, NTM, CoderName, FunctionsCompleted

print(CoderName)

print(FunctionsCompleted)


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

print ("Acceptance PDA pda2: ","0011", " ", pda2.acceptPDA('0011')) # should be True
print('--------------------------------------------------------------------------')
#print ("Acceptance PDA pda2: ","001", " ", pda2.acceptPDA('001')) # should False
print('--------------------------------------------------------------------------')

