### IMPORTANT: Your program must run on Python 3.7.3 or later
### No libraries may be used 
###
### Author: Hector Munoz-Avila (2018)
### Last update: 4/16/2021, Arielle K. Carr


### Rename file with your first and last name (and delete "Skeleton")
### For instance, Professor Carr's file would be CarrArielle318Project.py


#####################################
### DFA
#####################################

CoderName = 'Bratislav Petkovic' ## Put your first and last name here
FunctionsCompleted = {'verifyDFA', 'verifyTM'} ## List all functions you are submitting here
### Any function you are not completing, leave as is in the skeleton file: DO NOT DELETE IT

class DFA(object):
    def __init__(self, Q=None, Sigma=None, Delta=None, q0=None, F=None):
        self.Q = Q                  #Finite set of states.
        self.Sigma = Sigma          #set of Input Symbols
        self.Delta = Delta          #Transition Function
        self.q0 = q0                #Initial state
        self.F = F                  #set of Final States

    def verifyDFA(self):
        # Decides if self is a correct DFA
        # DO NOT change the input representation of DFAs

        # Do not modify or remove the following 
        for k,v in self.Delta.items():
             if not k in self.Q:
                print ("error:", k, self.Q)
                return False # transition from a non-state
             for k1,v1 in v.items():
               if not k1 in self.Sigma:
                   print ("error:", k1, self.Sigma)
                   return False # transition with a symbol not in Sigma
               if not v1 in self.Q:
                   print ("error:", v1, self.Q)
                   return False  # transition to a non-state
                
        # Complete this code!       
        # Add code verifying that each state in Q has one and only one transtion
        # in delta for each symbol in Sigma.
        
        for k,v in self.Delta.items():
            print("Current Transition: ", k, "--> ", v)
            for symbol in self.Sigma:
                print("symbol : ",symbol )
                if not symbol in v:
                    print("symbol : ",symbol , " is not in : ", k, "--> ", v)
                    return False
                
        # If so return True; else return False

        return True    
       

    def acceptDFA(self,s):
        # Decides if self accepts the string s
        # Complete this code!
        return True
        

    def emptyDFA(self):
        # Decides if self  accepts no  strings
        # Complete this code!
       return True

    def EQDFA(self,D):
        # Decides if L(self) = L(D), where D is a DFA
        # Complete this code!
        return True



#####################################
### PDA 
#####################################

class PDA(object):
    def __init__(self, Q=None, Sigma=None, Gamma=None, Delta=None, q0=None, F=None):
        self.Q = Q
        self.Sigma = Sigma # may not contain 'e', which we use to denote the empty string
        self.Gamma = Gamma # may not contain 'e', which we use to denote the empty string
        self.Delta = Delta # may use 'e', which we use to denote the empty string
        self.q0 = q0
        self.F = F

    def verifyPDA(self):
         # Decides if self is a correct PDA
         # Complete this code!
         # DO NOT change the input representation of PDAs
        
        
         return True

    def acceptPDA(self,s):
        # Decides if self accepts s with at most 2|s| transitions from the start state
        # Must try all possible transitions
        # Complete this code!
        return True

    def notEQPDA(self,P,k):
        # Pseudo-recognizes if L(self) != L(P), where P is a  PDA
        # Must try all strings of length  0, 1, 2, .., k.
        # When it reaches strings of length  k+1, it returns false.
        # Complete this code!
        return True  
               
        
#####################################
### TM 
#####################################

class TM(object):
    def __init__(self, Q=None, Sigma=None, Gamma=None, Delta=None, q0=None, qAccept=None, qReject=None):
        self.Q = Q
        self.Sigma = Sigma
        self.Gamma = Gamma # '_' is the blank symbol
        self.Delta = Delta # Move to left: 'L'; move to right: 'R'
        self.q0 = q0
        self.qAccept = qAccept
        self.qReject = qReject

    def verifyTM(self):
        # Decides if self is a correct TM
        # DO NOT change the representation of TM

        # Do not modify or delete the following
        for k,v in self.Delta.items():
            if not k in self.Q:
               print ("error:", k, self.Q) 
               return False  # transition from a non-state
            for k1,v1 in v.items():
               if not k1 in self.Gamma:
                   print ("error:", k1, self.Sigma)
                   return False # transition reading a symbol not in Gamma
               if not v1[0] in self.Q:
                   print ("error:", v1[0], self.Q)
                   return False # transition to  a non-state
               if not v1[1] in self.Gamma:
                   print ("error:", v1[1], self.Gamma)
                   return False # transition writing a symbol not in Gamma
               if not v1[2] in ['L','R']:
                   print ("error:", v1[2], "should be L or R")
                   return False # "should be L or R"
                
        # Complete this code!
        # Add code verifying that each state in Q has one and only one transtion
        # in delta for each symbol in Gamma.
        # If so return True; otherwise return False

        return True    
       
    def acceptTM(self,s,k):
        # Pseudo-recognizes if TM self accepts s
        # if TM reaches an accepting state, it should accept
        # if TM reaches a rejecting states it should reject.
        # s is a list; it is used as the initial tape;
        # Assumes head pointing to first symbol in s
        # returns false if the number of transitions exceeds k.
        # Complete this code!
        head = 0
        
        return True
        
            
#####################################
### NTM 
#####################################

class NTM(object):
    def __init__(self, Q=None, Sigma=None, Gamma=None, Delta=None, q0=None, qAccept=None):
        self.Q = Q
        self.Sigma = Sigma
        self.Gamma = Gamma # '_' is the blank symbol
        self.Delta = Delta # Move to left: 'L'; move to right: 'R'
        self.q0 = q0
        self.qAccept = qAccept
      

    def verifyNTM(self):
        # Decides if self is a correct NTM
        # DO NOT change the representation of NTM
        # Complete this code!
        
        return True    
       
    def acceptNTM(self,s,k):
        # Quasi-recognizes if NTM self accepts s; NTM has no reject state
        # s is a list; it is used as the initial tape;
        # assumes head pointing to first symbol in s
        # If it doesn't reach an accepting state with all transitions of lenght k, return false.
        # Complete this code!
        
        head = 0
        
        return True
        

