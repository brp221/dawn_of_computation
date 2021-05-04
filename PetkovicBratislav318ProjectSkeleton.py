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
            #print("Current Transition: ", k, "--> ", v)
            for symbol in self.Sigma:
                #print("symbol : ",symbol )
                if not symbol in v:
                    print("symbol: ",symbol , " is not in: ", k, "--> ", v)
                    return False
                
        # If so return True; else return False

        return True    
       

    def acceptDFA(self,s):
        ##how about try to create the string s and if it fails return false i like this better
        #the array to store the transition functions

        s_arr = list(s) #turn string into array 
        print('\n')
        state_transitions = []
        generated_w = []
        #curr_state keeps track of the current state
        curr_state = self.q0   
        counter = 0
        state_transitions.append(curr_state)

        #iterate over the character array
        while(len(generated_w) < len(s_arr)):
            #print("curr char: ", char)
            #iterating over delta the transition function in order
            for k,v in sorted(self.Delta.items()):
                #print(generated_w)            
                if(k == curr_state):
                    for k1,v1 in v.items():
                        #handles array out of bounds
                        if(counter >= len(s_arr)):
                            break
                        if (k1==s_arr[counter]):
                            #print("k1 == current_char: ", k1, " == ", s_arr[counter])
                            #print("Before append: ",state_transitions)
                            #change the current state
                            curr_state = v1
                            state_transitions.append(curr_state)
                            #print("After append: ",state_transitions)
                            #generated_w
                            generated_w.append(s_arr[counter])
                            #pop the element from list
                            counter = counter + 1
                            #important to break once the loop has found the needed transition and updated info
                            break
        
        if(not (state_transitions[len(state_transitions)-1] in self.F)):
            print(s_arr)
            print("Final State generated: ",state_transitions[len(state_transitions)-1] )
            print("Final State given: ", self.F)
            print("state_transitions: " ,state_transitions)
            print("generated_w: " ,generated_w)
            return False
        print("String Given:     ",s_arr)
        print("String Generated: " ,generated_w)
        print("Final State generated: ",state_transitions[len(state_transitions)-1] )
        print("Final State(s) given    : ", self.F)
        print("state_transitions: " ,state_transitions)
        return True
        

    def emptyDFA(self):
        # Decides if self  accepts no  strings
        # In toher words, can you reach the final state
        # Complete this code!
       return True

    def EQDFA(self,D):
        # if the 2 DFAs do not contain the same number of symbols and same 
        # type of symbols they can't generate the sama lang
        if(self.Sigma != D.Sigma):
            return False
        
        #2-D (or 3-D) array of dictionaries? to store values
        result_arr = []
        dfas = [self,D]
        curr_states = [self.q0, D.q0]
        state_pairs = [{self.q0, D.q0}]
        finished = False
        #start at the initial states for both. For each symbol, see what their transitions are 
        while(not finished):
            temp_arr = []
            counter = 0
            for dfa in dfas:
                line = [curr_states[counter]]
                print("Curr state: ", curr_states[counter])
                print("Curr line: ", line)
                #add: [statename, symbol1 symbol2]
                #symnbols are 0 and 1 only
                for symbol in dfa.Sigma:
                    print("curr symbol: ", symbol)
                    for k,v in dfa.Delta.items():
                        print(k,"--->", v)
                        if(curr_states[counter] == k):
                            for k1,v1 in v.items():
                                if(k1==symbol):
                                    print("adding: ", {symbol:v1} )
                                    line.append({symbol:v1})
                print("Line: ", line)
                result_arr.append(line)     

                counter = counter + 1
                print("Counter is : ", counter)
               
            #check to see if the produced table's states are both final or both non final 

            #add the new pair to state_pairs if they already do not exist if they exist add them at next index 
            #if they already exist at the next index as well you've finished :)
            # use something such as while state_pairs have not been exhasueted 
            list1 = list(result_arr[0][1].values())
            list2 = list(result_arr[1][1].values())
            print(list1)
            state_pairs.append({list1[0],list2[0]})
            print("State_pairs between 2 DFAss: ", state_pairs)
            finished = True
                        
        print("resulting arr: ",result_arr)       
                


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
        

