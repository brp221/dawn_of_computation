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
import numpy as np
CoderName = 'Bratislav Petkovic' ## Put your first and last name here
FunctionsCompleted = {'verifyDFA', 'verifyTM','acceptDFA', 'emptyDFA','EQDFA','verifyPDA','acceptPDA' } ## List all functions you are submitting here
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
        
    
    #can be improved
    def emptyDFA(self):
        # Decides if self  accepts no  strings
        # In toher words, can you reach the final state
        # Complete this code!

        #APPROACH1: REVERSE ENGINEER; see if it is possible to reach the initial state given final state(s) >:)
        #APPROACH2: Make a tree (actually a 2-D matrix where each possibility is a new matrix inside that matrix )
        backtrack = [[]]
        counter=0
        for final_state in self.F:
            backtrack[counter].append(final_state)
            counter= counter+1
        
        print(backtrack)
            
        #assume the dfa is empty
        empty = True
        #iterate over transition fucntion Delta
        for k,v in self.Delta.items():
            #print("On state: ", k," transitions are: ", v )
            for k1,v1 in v.items():
                for branch in backtrack:
                    print("curr final state is: ", branch[counter1], '\n')
                    if(branch[0] == v1):
                        backtrack[0].append(k)
                        print(branch[0], " == ", v1)
                        print("Found the final state: ", k, "--->", v)
                        print("backtrack: ",backtrack)
                        empty = False
                        return empty
                    counter1 = counter1 + 1
                    
        
        
        return empty

    def EQDFA(self,D):
        # Decides if L(self) = L(D), where D is a DFA
        # APPROACH: MINIMIZE BOTH DFAS AND COMPARE THEM AT EACH STATE
        # if the 2 DFAs do not contain the same number of symbols and same 
        # type of symbols they can't generate the sama lang
        if(self.Sigma != D.Sigma):
            return False
        
        #2-D (or 3-D) array of dictionaries? to store values
        result_arr = []
        dfas = [self,D]
        #array to hold state_pairs to be iterated over
        state_pairs = [[self.q0, D.q0]]
        #all state_pairs which have been iterated over
        state_pairs_visited_already = [[[self.q0, D.q0]]]
        
        #start at the initial states for both. For each symbol, see what their transitions are 
        while(not(len(state_pairs)==0)):

            #print("State_pairs on queue: ",state_pairs )
            #add to the already visited_pairs
            state_pairs_visited_already.append(state_pairs[0])
            #reset counter by placing it here 
            counter = 0
            #create a line to connect/represent both DFAs
            for dfa in dfas:
                line = [state_pairs[0][counter]]
                #print("Curr Pair: ",state_pairs[0])
                ##print("Curr state: ", state_pairs[0][counter])
                #print("Curr line: ", line) # the line to be created
                #for each symbol in array of sorted symbols 
                for symbol in sorted(dfa.Sigma):
                    for k,v in dfa.Delta.items():
                        #if the curr_state and the state in transition func are the same
                        if(state_pairs[0][counter] == k):
                            for k1,v1 in v.items():
                                #if k1 matches the current loop's symbol
                                if(k1==symbol):
                                    #add symbol and corresponding state
                                    line.append({symbol:v1})
                print("Line: ", line)
                result_arr.append(line)    
                
                #once the counter is 2, the looping has finished, reason being is because we are comparing 2 DFAs
                counter = counter + 1

            #creation of the pair from the 'line'
            for i in range(len(result_arr[0])):
                #create the pair(or the triple or the n-size(depends on numb of symbols))
                if(i>0):
                    state_group = []
                    for j in range(len(result_arr)):
                        #extracting state pair
                        #create the pair(or the triple or the n-size(depends on numb of symbols))
                        key,value = next(iter(result_arr[j][i].items()))
                        #print("at index i,j:", j,",",i, " result_arr is:", str(key), ", ", str(value))
                        state_group.append(value)
                        #print("State_group: ", state_group)
                    print("State_group JOINED: ", state_group)

                    #check to see if the state group is all final states or all non-final 
                    #handles case for the 2DFAs not being equal
                    if(((not state_group[0] in self.F) and (state_group[1] in D.F)) or((not state_group[1] in self.F) and (state_group[0] in D.F))):
                        print("state_group[0]:",state_group[0], "is not in self.F:", self.F)
                        print("state_group[1]:",state_group[1], "is not in D.F:", D.F)
                        return False
                    #only add the state group if it has not been visited yet
                    if(not state_group in state_pairs_visited_already):
                        #print("                                     state_group: ",state_group, " is not in state_pairs_visited_already:", state_pairs_visited_already)
                        state_pairs.append(state_group)
                    
                    #delete the first state pair and move on :):
                    #print("State_pairs between 2 DFAs: ", state_pairs)

            #pop the 1st state_pair from the queue once algorithm is done with it  
            state_pairs.pop(0)
            #reset the result_arr for a new line to be created from a new state_pair
            result_arr = []
            
        #if the algorithm reaches here, the 2 DFAs are equivalent :)
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
         #PDA is not verified if:
            #on its transition function delta, any of teh transitions are missing any of the symbols
            #sigma or gamma contain 'e'

        if(('e' in self.Sigma) or ('e' in self.Gamma)):
            print('Sigma and Delta may not contain \'e\', which we use to denote the empty string')    
        #create an array of symbols for each transition func
        arr=[]
        for k,v in self.Delta.items():
            object_transition = []
            object_transition.append(k)
            for k1,v1 in v.items():
                #add all the the symbols to the corresponding transition
                object_transition.append(k1)
            arr.append(object_transition)
                 
        print("arr:", arr)
            
        for symbol in self.Sigma:
            for each in arr:
                if(not(symbol in each)):
                    print("symbol:", symbol, " is not in ", each)
                    return False
        
        return True

    def acceptPDA(self,s):
        # Decides if self accepts s with at most 2|s| transitions from the start state
        # Must try all possible transitions
        # Complete this code!
        stack = []
        state_transitions = [self.q0]
        string_created = ''
        #special case of empty string s                        
        if(string_created==''):
            last_index = len(state_transitions)-1
            if((state_transitions[last_index] in self.F) and s==string_created):
                print("String accepted because given string s:",s," === generated string g:",string_created)
                print("State transition: ",state_transitions[last_index], "is in final states: ", self.F)
                return True
            if((not(state_transitions[last_index] in self.F)) and s==string_created):
                print("String rejected because because even though given string s:",s," === generated string g:",string_created)
                print("State transition: ",state_transitions[last_index], "is not a final state: ", self.F)
                return False

        s_arr = list(s)
        s_created = []
        print(s_arr)
        counter=0

        while(counter<len(s_arr)):
            current_char=s_arr[counter]
            print("char is: ",current_char)
            for k,v in self.Delta.items():
                #print(k,"--->",v)
                curr_state = state_transitions[len(state_transitions) -1]
                #print("curr_state: ", curr_state)
                if(k==curr_state):
                    #print("for k=",k, "transitions are: ", v)
                    for k1,v1 in v.items():
                        #case for input being empty/not being considered
                        if((k1=='e')and (len(v1)>0)):
                            print("v1:", v1)
                            print("v1[0]:", v1[0])
                            #print("e case")
                            print("len of v1[0]:", len(v1[0])) #assume always 3 for now
                            v1_len = len(v1)
                            #print('UMM: ', [v1[0][1]])
                            print('stack: ', stack)
                            #print(stack == [v1[0][1]])
                            i=0
                            temp_arr = s_created
                            while(i<v1_len):
                                #i think this does backtracking
                                s_created = temp_arr
                                #case for pushing $ on stack; the START
                                if(v1[i][1] == 'e' and (len(stack)==0)):
                                    #print("E CASE DID SOMETHING")
                                    state_transitions.append(v1[i][0])
                                    stack.append(v1[i][2])  # the $ symbol to denote bottom of stack
                                    print('stack: ', stack)
                                    print("string_created: ", s_created)
                                    print('state_transitions: ', state_transitions)
                                    print('\n')
                                #case for popping $ off stack; the END
                                if((v1[i][1] == '$') and (stack == [v1[i][1]])):
                                    #print('UMM: ', [v1[0][1]])
                                    #print('YEAH: ', stack)
                                    state_transitions.append(v1[i][0])
                                    print('stack: ', stack)
                                    stack.pop()  # the $ symbol to denote bottom of stack
                                    print('stack: ', stack)
                                    print("string_created: ", s_created)
                                    print('state_transitions: ', state_transitions)
                                    last_index = len(state_transitions)-1
                                    #if statements for accepting or rejecting input go here at the end of the line 
                                    #3 conditions to cover are 
                                        #is the last transition one of the final stransition 
                                        #is s_arr==s_created
                                        #is |state_transitions| < 2|s|
                                        #is it the last possible option: i = v1_len-1
                                    if((state_transitions[last_index] in self.F) and (s_arr==s_created) and (len(state_transitions)<=len(s)*2)):
                                        print("String accepted because given string s:",s_arr," === generated string g:",s_created)
                                        print("(# of transitions)<=2|s|):  ", len(state_transitions), "<=",len(s)*2)
                                        print('\n')
                                        return True
                                    if((state_transitions[last_index] in self.F) and ((s_arr!=s_created)or(len(state_transitions)>len(s)*2))):
                                        if(i==v1_len-1):
                                            print("String rejected because given string s:",s_arr," !!== generated string g:",s_created)
                                            print("OR because the number of state transitions is greater than 2|w|")
                                            print('\n')
                                            return False
                                        
                                        print("hit a dead end tbh")
                                        i = i+1
                                        continue
                                        
                                #case for getting to end of string but the stack is not equivalent to ['$'] as it should be 
                                if((v1[i][1] == '$') and (stack != [v1[i][1]])):
                                    print("The stack is not empty: ", stack)
                                    if(i==v1_len-1):
                                            print("String rejected because given string s:",s_arr," !!== generated string g:",s_created)
                                            print("OR because the number of state transitions is greater than 2|w|")
                                            print("OR because the stack isn't empty")
                                            print('\n')
                                            return False
                                    i = i + 1
                                    continue
                                    return False
                                i = i+1
                        #input symbol is not 'e', 
                        else:
                            if((k1==current_char) and (len(v1)>0)):       
                                print('stack: ', stack)
                                
                                v1_len = len(v1)
                                #print('UMM: ', [v1[0][1]])
                                print('stack: ', stack)
                                #print(stack == [v1[0][1]])
                                #case for pushing $ on stack; the START
                                for i in range(v1_len):
                                    stack_top = stack[len(stack)-1]
                                    print('stack_top: ', stack_top)
                                    #only if the stack contains something more than the $ symbol
                                    if(v1[i][1]=='e'):
                                        #append v1[0][2] to the stack
                                        stack.append(v1[i][2])
                                        state_transitions.append(v1[i][0])
                                        s_created.append(k1)
                                        print('stack1: ', stack)
                                        print("string_created1: ", s_created)
                                        print('state_transitions1: ', state_transitions)
                                        print('\n')
                                    #if there is stuff on the stac other than just $, the top of the stack needs to be checked 
                                    if((len(stack)>1) and (v1[i][1]==stack_top)):
                                        s_created.append(k1)
                                        state_transitions.append(v1[i][0])
                                        print('stack before pop: ', stack)
                                        stack.pop()
                                        print('stack after pop: ', stack)
                                        print("string_created: ", s_created)
                                        print('state_transitions: ', state_transitions)
                                        print('\n')
            counter = counter + 1
    
    def notEQPDA(self,P,k):

        #APPROACH: CREATE A STRING. IF A CERTAIN STATE HAS MORE THAN 1 POSSIBLE TRANSITIONS, CHOOSE ONE AT RANDOM. 
        #THEN RUN THE ALGORITHM TO CREATE SUCH A STRING 1000 TIMES OR UNTIL DESIRED STRING IS REACHED

        # Pseudo-recognizes if L(self) != L(P), where P is a  PDA
        # Must try all strings of length  0, 1, 2, .., k.
        # When it reaches strings of length  k+1, it returns false.
        # Complete this code!
        genrtd_strgs = []

        #generate a string of length k
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
        states_found =[]
        for state in self.Q:
            states_found =[]
            for k,v in self.Delta.items():
                states_found.append(k)
                if (state==k):
                    #print("state=", state, " k=", k)
                    #print("state matches k, v is : ", v, "\n")
                    for symbol in self.Gamma:
                        #print("symbol : ",symbol )
                        if not symbol in v:
                            print("symbol: ",symbol , " is not in: ", k, "--> ", v)
                            return False
            if((state!='accept') and (state!='reject') and (not (state in states_found))):
                print("state: ", state, "not in: ", states_found)
                return False

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
        strng_len = len(s)
        state_transitions = [self.q0]
        gen_string =[]
        curr_state = state_transitions[len(state_transitions)-1]
        counter1=0
        while(counter1<strng_len):
            print(s[counter1])
            for k,v in self.Delta.items():
                if(k==curr_state):
                    print("k: ",k, " ---> v: ", v)
                    for k1,v1 in v.items():
                        #current tape symbol mathches transition symbol 
                        if(s[head]==k1):       
                            print("             v.items: ", k1, " ---->", v1)
                            state_transitions.append(v1[0])
                            gen_string.append(v1[1])
            
            #UPDATES PEOPLE
            print("gen_string: ", gen_string)
            print("state_transitions: ", state_transitions)
            curr_state = state_transitions[len(state_transitions)-1]
            counter1+=1

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
        

