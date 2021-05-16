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
import random
CoderName = 'Bratislav Petkovic' ## Put your first and last name here
FunctionsCompleted = {'verifyDFA', 'verifyTM','acceptDFA', 'emptyDFA','EQDFA','verifyPDA','acceptPDA', 'acceptTM','verifyNTM','acceptNTM', 'acceptNTM'} ## List all functions you are submitting here
FunctionsToComplete = {'emptyDFA'}
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
            #print("Final State generated: ",state_transitions[len(state_transitions)-1] )
            #print("Final State given: ", self.F)
            print("state_transitions: " ,state_transitions)
            print("generated_w: " ,generated_w)
            return False
        #print("String Given:     ",s_arr)
        #print("String Generated: " ,generated_w)
        #print("Final State generated: ",state_transitions[len(state_transitions)-1] )
        #print("Final State(s) given    : ", self.F)
        print("state_transitions: " ,state_transitions)
        return True
        
    
    def emptyDFA(self):
        # Decides if self  accepts no  strings
        # In toher words, can you reach the final state
        # Complete this code!

        #APPROACH1: REVERSE ENGINEER; see if it is possible to reach the initial state given final state(s) >:)
        backtrack = []
        for final_state in self.F:
            backtrack.append([final_state])

        #assume the dfa is empty
        empty = True
        counter_1=0
        #len(backtrack)
        while(counter_1<4 and len(backtrack) != 0):
            curr_poss = backtrack[0]
            #check if its a valid transition
            recent_state= curr_poss[len(curr_poss)-1]
            if(recent_state in self.q0):
                print("Valid state transition: ", curr_poss)
                return False
            #print("curr poss: ", curr_poss)
            #print("recent_state: ", recent_state)
            counter_2=0
            while(counter_2<3):
                #print("counter_2:",counter_2)
                #iterate over transition fucntion Delta
                for k,v in self.Delta.items():
                    for k1,v1 in v.items():
                        #print("here")
                        temp_transition=[]
                        temp_transition.extend(curr_poss)
                        if(recent_state == v1):
                            temp_transition.append(k)
                            #print("temp_transition: ", temp_transition)
                            if(not(temp_transition in backtrack)):
                                backtrack.append(temp_transition)
                counter_2+=1
            
            #print("backtrack",backtrack)

            #delete the already branched state_trans
            backtrack.remove(curr_poss)
            #print("backtrack",backtrack)

            counter_1+= 1
        
        print(backtrack)
        
        
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
                #print("Line: ", line)
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
                    #print("State_group JOINED: ", state_group)

                    #check to see if the state group is all final states or all non-final 
                    #handles case for the 2DFAs not being equal
                    if(((not state_group[0] in self.F) and (state_group[1] in D.F)) or((not state_group[1] in self.F) and (state_group[0] in D.F))):
                        print("\nstate_group[0]:",state_group[0], "is not in self.F:", self.F)
                        print("\nstate_group[1]:",state_group[1], "is not in D.F:", D.F)
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
                 
        #print("arr:", arr)
            
        for symbol in self.Sigma:
            for each in arr:
                if(not(symbol in each)):
                    print("symbol:", symbol, " is not in ", each)
                    return False
        
        return True

    
    def acceptPDA(self,s):
        def generate_string_pda(self,s):
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
                    return True
                if((not(state_transitions[last_index] in self.F)) and s==string_created):
                    return False

            s_arr = list(s)
            s_created = []
            counter=0

            while(counter<len(s_arr)):
                current_char=s_arr[counter]
                #print("char is: ",current_char)
                for k,v in self.Delta.items():
                    #print(k,"--->",v)
                    curr_state = state_transitions[len(state_transitions) -1]
                    #print("curr_state: ", curr_state)
                    if(k==curr_state):
                        #print("for k=",k, "transitions are: ", v)
                        for k1,v1 in v.items():

                            #case for input being 'e'
                            if((k1=='e')and (len(v1)>0)):                                
                                v1_len = len(v1)
                                i = random.randint(0, v1_len-1)                               
                                #case for pushing $ on stack; the START
                                if(v1[i][1] == 'e' and (len(stack)==0)):
                                    state_transitions.append(v1[i][0])
                                    stack.append(v1[i][2])  # the $ symbol to denote bottom of stack

                                #case for popping $ off stack; the ENDING has been reached 
                                if(v1[i][1] == '$'):
                                    if(stack == [v1[i][1]]):
                                        # check that everything mathches up
                                        state_transitions.append(v1[i][0])
                                        stack.pop()  # the $ symbol to denote bottom of stack
                                        last_index = len(state_transitions)-1
                                        if((state_transitions[last_index] in self.F) and (s_arr==s_created) and (len(state_transitions)<=len(s)*2)):
                                            return True
                                        else:
                                            return False

                                    #prob a reject case
                                    if(not(stack == [v1[i][1]])):
                                        return False
                            #input symbol is not 'e', 
                            else:
                                if((k1==current_char) and (len(v1)>0)):                        
                                    v1_len = len(v1)
                                    #case for pushing $ on stack; the START
                                    j = random.randint(0, v1_len-1)
                                    stack_top = stack[len(stack)-1]
                                    #only if the stack contains something more than the $ symbol
                                    if(v1[j][1]=='e'):
                                        #append v1[0][2] to the stack
                                        stack.append(v1[j][2])
                                        state_transitions.append(v1[j][0])
                                        s_created.append(k1)
                                        
                                    #if there is stuff on the stac other than just $, the top of the stack needs to be checked 
                                    if((len(stack)>1) and (v1[j][1]==stack_top)):
                                        s_created.append(k1)
                                        state_transitions.append(v1[j][0])
                                        stack.pop()

                counter = counter + 1

        for i in range(0,200):
            if(generate_string_pda(self,s)==True):
                return True

        return False
    
    
    def notEQPDA(self,P,k):

        # APPROACH: Keep following the states and creating string based on current tape status, curr state and the delta transition function
        # curr state and the delta transition function
        # Each possibility is of the following format:
        # [generated_string,stack, state_transitions]
        # Iterate over all possibilities, if the last state of the indexed possibility is accept, skip it and save it else build on top of it 

        # Pseudo-recognizes if L(self) != L(P), where P is a  PDA
        # Must try all strings of length  0, 1, 2, .., k.
        # When it reaches strings of length  k+1, it returns false.
        # Complete this code!
        
        stack=[]
        state_transitions=[self.q0]
        genrtd_strgs = [['',state_transitions,stack]]
        longest_str_len=0
        str_len = 0
        #Algoithm to generate every possibility of self
        while(longest_str_len <= k):
            #generate a string of length str_len
            #print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            #print("str_len: ",str_len)
            counter_1=0
            curr_gnrt_strings = len(genrtd_strgs)
            elements_to_delete = []
            while(counter_1<curr_gnrt_strings):
                #print("-------------------------------")
                #print("counter_1: ", counter_1)
                #print("current possibility: ", genrtd_strgs[counter_1])
                curr_state = genrtd_strgs[counter_1][1][len(genrtd_strgs[counter_1][1]) -1]
                for key,value in self.Delta.items():
                    #transition and current state match
                    if(key==curr_state):
                        #print("curr_state: ", curr_state)
                        #print(key, "------->", value)
                        for k1,v1 in value.items():
                            #case for input being 'e'
                            if((k1=='e')and (len(v1)!=0)):
                                #print("E CASE")
                                #the beginning: pushing $ on stack;
                                if(v1[0][1] == 'e' and (len(genrtd_strgs[counter_1][2])==0)):
                                    #update the state_transitions
                                    temp_state_trans = []
                                    temp_state_trans.extend(genrtd_strgs[counter_1][1])
                                    temp_state_trans.extend([v1[0][0]])
                                    #update the string
                                    temp_string = ''
                                    if(v1[0][1] == 'e'):
                                        temp_string+=''
                                    #update the stack
                                    temp_stack =[]
                                    if(v1[0][2]=='$'):
                                        temp_stack.append('$')
                                    genrtd_strgs.append([temp_string,temp_state_trans,temp_stack])
                                    #print("object added: ",[temp_string,temp_state_trans,temp_stack], "\n")
                                
                                #the end; popping off the stack                
                                if(v1[0][1] == '$' and genrtd_strgs[counter_1][2] == ['$']):
                                    #update the state_transitions
                                    temp_state_trans = []
                                    temp_state_trans.extend(genrtd_strgs[counter_1][1])
                                    temp_state_trans.extend([v1[0][0]])
                                    #update the string
                                    temp_string = '' + genrtd_strgs[counter_1][0]
                                    if(v1[0][1] == 'e'):
                                        temp_string+=''
                                    #update the stack
                                    temp_stack =[]
                                    temp_stack.extend(genrtd_strgs[counter_1][2])
                                    #print("stack BEFORE pop: ", temp_stack)
                                    temp_stack.pop()
                                    #print("stack AFTER pop: ", temp_stack)
                                    #print("             after temp_state_trans:",temp_state_trans)
                                    #stack.append(v1[0][2])  # the $ symbol to denote bottom of stack
                                    genrtd_strgs.append([temp_string,temp_state_trans,temp_stack])
                                    #print("object added: ",[temp_string,temp_state_trans,temp_stack], "\n")
                                
                            #case for input not being 'e'
                            elif( (k1!='e')and (len(v1)!=0)):         
                                #print('curr_stack: ', genrtd_strgs[counter_1][2])                      
                                num_branches = len(v1)
                                counter_2=0
                                # while handles multiple possibilities and then diverge 
                                # the current possibility into num_brancehes new possibilities
                                while(counter_2 < num_branches):
                                    #there are 2 major cases: popping and not popping from the top of the stack
                                    #1: case where v1[counter_2][1] = 'e'
                                    if(v1[counter_2][1] == 'e'):
                                        #print("Stack top irrelevant")
                                        #update the state_transitions
                                        temp_state_trans = []
                                        temp_state_trans.extend(genrtd_strgs[counter_1][1])
                                        temp_state_trans.extend([v1[counter_2][0]])
                                        #update the string
                                        temp_string = '' + genrtd_strgs[counter_1][0] + k1
                                        #update the stack
                                        temp_stack =[]
                                        temp_stack.extend(genrtd_strgs[counter_1][2])
                                        if(v1[counter_2][2]!='e'):
                                            temp_stack.extend(v1[counter_2][2])
                                        #stack.append(v1[0][2])  # the $ symbol to denote bottom of stack
                                        genrtd_strgs.append([temp_string,temp_state_trans,temp_stack])
                                        #print("object added: ",[temp_string,temp_state_trans,temp_stack], "\n")
                                
                                    #1: case where v1[counter_2][1] != 'e'
                                    if(v1[counter_2][1] != 'e'):
                                        #first check top of stack
                                        #print("Stack top RELEVANT")
                                        stack_top = genrtd_strgs[counter_1][2][len(genrtd_strgs[counter_1][2])-1]
                                        if(v1[counter_2][1] == stack_top):
                                            #update the state_transitions
                                            temp_state_trans = []
                                            temp_state_trans.extend(genrtd_strgs[counter_1][1])
                                            temp_state_trans.extend([v1[counter_2][0]])
                                            #update the string
                                            temp_string = '' + genrtd_strgs[counter_1][0] + k1
                                            #update the stack
                                            temp_stack =[]
                                            temp_stack.extend(genrtd_strgs[counter_1][2])
                                            #print("stack BEFORE pop: ", temp_stack)
                                            temp_stack.pop()
                                            #print("stack AFTER pop: ", temp_stack)
                                            #stack.append(v1[0][2])  # the $ symbol to denote bottom of stack
                                            genrtd_strgs.append([temp_string,temp_state_trans,temp_stack])
                                            #print("object added: ",[temp_string,temp_state_trans,temp_stack], "\n")   
                                    counter_2+=1
                        break
                        #print("Am i Here?")
                #print("or Am i Here?")
                
                #at this point in the code, it is necessary to delete the previous gen_str element used
                #especially if it has not reached a final state
                final_state = genrtd_strgs[counter_1][1][len(genrtd_strgs[counter_1][1])-1]
                # delete case: current last state 
                if(not(final_state in self.F) or not(len(genrtd_strgs[counter_1][2]))==0):
                    #del genrtd_strgs[counter_1]
                    elements_to_delete.append(genrtd_strgs[counter_1])
                #print("elements_to_delete: ", elements_to_delete)
                counter_1+=1
            
            # deleting genrtd_strgs elements which have already been used 
            for m in elements_to_delete:
                #print("Deleting: ",m)
                genrtd_strgs.remove(m)
            #print("\ngenrtd_strgs:",genrtd_strgs,"\n")
            str_len+=1
        
            #  Algo for extracting longest generated string from the whole array so that while loop knows when to stop
            for string in genrtd_strgs:
                if(len(string[0])>longest_str_len):
                    longest_str_len=len(string[0])
        



        stack_P=[]
        state_transitions_P=[P.q0]
        genrtd_strgs_P = [['',state_transitions_P,stack_P]]
        longest_str_len_P=0
        str_len_P = 0
        #Algoithm to generate every possibility of P
        while(longest_str_len_P <= k):
            counter_1_P=0
            curr_gnrt_strings_P = len(genrtd_strgs_P)
            elements_to_delete_P = []
            while(counter_1_P<curr_gnrt_strings_P):
                curr_state_P = genrtd_strgs_P[counter_1_P][1][len(genrtd_strgs_P[counter_1_P][1]) -1]
                for key_P,value_P in P.Delta.items():
                    #transition and current state match
                    if(key_P==curr_state_P):
                        for k1_P,v1_P in value_P.items():
                            #case for input being 'e'
                            if((k1_P=='e')and (len(v1_P)!=0)):
                                #the beginning: pushing $ on stack;
                                if(v1_P[0][1] == 'e' and (len(genrtd_strgs_P[counter_1_P][2])==0)):
                                    #update the state_transitions
                                    temp_state_trans_P = []
                                    temp_state_trans_P.extend(genrtd_strgs_P[counter_1_P][1])
                                    temp_state_trans_P.extend([v1_P[0][0]])
                                    #update the string
                                    temp_string_P = ''
                                    if(v1_P[0][1] == 'e'):
                                        temp_string_P+=''
                                    #update the stack
                                    temp_stack_P =[]
                                    if(v1_P[0][2]=='$'):
                                        temp_stack_P.append('$')
                                    genrtd_strgs_P.append([temp_string_P,temp_state_trans_P,temp_stack_P])
                                
                                #the end; popping off the stack                
                                if(v1_P[0][1] == '$' and genrtd_strgs_P[counter_1_P][2] == ['$']):
                                    #update the state_transitions
                                    temp_state_trans_P = []
                                    temp_state_trans_P.extend(genrtd_strgs_P[counter_1_P][1])
                                    temp_state_trans_P.extend([v1_P[0][0]])
                                    #update the string
                                    temp_string_P = '' + genrtd_strgs_P[counter_1_P][0]
                                    if(v1_P[0][1] == 'e'):
                                        temp_string_P+=''
                                    #update the stack
                                    temp_stack_P =[]
                                    temp_stack_P.extend(genrtd_strgs_P[counter_1_P][2])
                                    temp_stack_P.pop()
                                    genrtd_strgs_P.append([temp_string_P,temp_state_trans_P,temp_stack_P])
                                
                            #case for input not being 'e'
                            elif( (k1_P!='e')and (len(v1_P)!=0)):         
                                num_branches_P = len(v1_P)
                                counter_2_P=0
                                # while will handle multiple possibilities and then diverge 
                                # the current possibility into num_brancehes new possibilities
                                while(counter_2_P < num_branches_P):
                                    #there are 2 major cases: popping and not popping from the top of the stack
                                    #1: case where v1[counter_2][1] = 'e'
                                    if(v1_P[counter_2_P][1] == 'e'):
                                        #print("Stack top irrelevant")
                                        #update the state_transitions
                                        temp_state_trans_P = []
                                        temp_state_trans_P.extend(genrtd_strgs_P[counter_1_P][1])
                                        temp_state_trans_P.extend([v1_P[counter_2_P][0]])
                                        #update the string
                                        temp_string_P = '' + genrtd_strgs_P[counter_1_P][0] + k1_P
                                        #update the stack
                                        temp_stack_P =[]
                                        temp_stack_P.extend(genrtd_strgs_P[counter_1_P][2])
                                        if(v1_P[counter_2_P][2]!='e'):
                                            temp_stack_P.extend(v1_P[counter_2_P][2])
                                        genrtd_strgs_P.append([temp_string_P,temp_state_trans_P,temp_stack_P])
                                
                                    #1: case where v1[counter_2][1] != 'e'
                                    if(v1_P[counter_2_P][1] != 'e'):
                                        #first check top of stack
                                        stack_top_P = genrtd_strgs_P[counter_1_P][2][len(genrtd_strgs_P[counter_1_P][2])-1]
                                        if(v1_P[counter_2_P][1] == stack_top_P):
                                            #update the state_transitions
                                            temp_state_trans_P = []
                                            temp_state_trans_P.extend(genrtd_strgs_P[counter_1_P][1])
                                            temp_state_trans_P.extend([v1_P[counter_2_P][0]])
                                            #update the string
                                            temp_string_P = '' + genrtd_strgs_P[counter_1_P][0] + k1_P
                                            #update the stack
                                            temp_stack_P =[]
                                            temp_stack_P.extend(genrtd_strgs_P[counter_1_P][2])
                                            temp_stack_P.pop()
                                            genrtd_strgs_P.append([temp_string_P,temp_state_trans_P,temp_stack_P])
                                    counter_2_P+=1
                        break
                
                #at this point in the code, it is necessary to delete the previous gen_str element used
                #especially if it has not reached a final state
                final_state_P = genrtd_strgs_P[counter_1_P][1][len(genrtd_strgs_P[counter_1_P][1])-1]
                # delete case: current last state 
                if(not(final_state_P in P.F) or not(len(genrtd_strgs_P[counter_1_P][2]))==0):
                    elements_to_delete_P.append(genrtd_strgs_P[counter_1_P])
                counter_1_P+=1
            
            # deleting genrtd_strgs elements which have already been used 
            for n in elements_to_delete_P:
                genrtd_strgs_P.remove(n)
            str_len_P+=1
        
            #  Algo for extracting longest generated string from the whole array so that while loop knows when to stop
            for string_P in genrtd_strgs_P:
                if(len(string_P[0])>longest_str_len_P):
                    longest_str_len_P=len(string_P[0])
        
        pda1_strings=[]
        for each in genrtd_strgs:
            if(not(each[0] in pda1_strings)):
                pda1_strings.append(each[0])

        pda2_strings=[]
        for each in genrtd_strgs_P:
            if(not(each[0] in pda2_strings)):
                pda2_strings.append(each[0])

        if(len(pda1_strings)!=len(pda1_strings)):
            return True
        # Check if the strings generated are a perfect match
        # Linearly compare elements
        for i in range(0, len(pda1_strings) - 1):
            if (pda1_strings[i] != pda2_strings[i]):
                return True
        
        return False
        
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
                    for symbol in self.Gamma:
                        if not symbol in v:
                            print("\nsymbol: ",symbol , " is not in: ", k, "--> ", v)
                            return False
            if((state!='accept') and (state!='reject') and (not (state in states_found))):
                print("\nstate: ", state, "not in: ", states_found)
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
        state_transitions = [self.q0]
        curr_state = state_transitions[len(state_transitions)-1]
        s.append('_')
        strng_len = len(s)
        print(s)
        counter1=0
        while(True):
            for key,v in self.Delta.items():
                #if key matches up the curr state
                if(key==curr_state):
                    for k1,v1 in v.items():
                        #current tape symbol mathches transition symbol 
                        if(s[head]==k1):       
                            state_transitions.append(v1[0])
                            s[head] = v1[1]
                            if(v1[2] == 'R'):
                                head+=1
                                break   #break out of for loop because head was changed
                            if(v1[2] == 'L'):
                                head-=1
                                break   #break out of for loop because head was changed
            #UPDATES PEOPLE
            curr_state = state_transitions[len(state_transitions)-1]
            counter1+=1

            if((state_transitions[len(state_transitions)-1]) == 'accept'):
                #case for more transitions than allowed
                if(len(state_transitions) > k):
                    return False
                print("\nLast state: ", state_transitions[len(state_transitions)-1])
                print("Tape Status: ", s)
                print("# of transitions: ",len(state_transitions), "<=  k: ", k)
                return True
            if(state_transitions[len(state_transitions)-1] == 'reject'):
                print("\nLast state: ", state_transitions[len(state_transitions)-1])
                print("Tape Status: ", s)
                print("# of transitions: ",len(state_transitions), "<=  k: ", k)
                return False
        
            
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
        # Decides if self is a correct TM
        # DO NOT change the representation of TM
        if('_' in self.Sigma):
            print('Sigma; may  not contain \'_\', which we use for the blank symbol')
            return False
        if(not('_' in self.Gamma)):
            print('Gamma; \'_\' is the symbol that must be used for blank')
            return False
        # Do not modify or delete the following
        for k,v in self.Delta.items():
            if not k in self.Q:
               print ("error:", k, self.Q) 
               return False  # transition from a non-state
            for k1,v1 in v.items():
                #print(k1,"--->",v1)
                if not k1 in self.Gamma:
                    print ("error:", k1, self.Sigma)
                    return False # transition reading a symbol not in Gamma
                for i in range(0,len(v1)):
                    if not v1[i][0] in self.Q:
                        print ("error:", v1[i][0], self.Q)
                        return False # transition to  a non-state
                    if not v1[i][1] in self.Gamma:
                        print ("error:", v1[i][0], self.Gamma)
                        return False # transition writing a symbol not in Gamma
                    if not v1[i][2] in ['L','R']:
                        print ("error:", v1[i][0], "should be L or R")
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
        
        return True    

    def acceptNTM(self,s,k):
                
            # Quasi-recognizes if NTM self accepts s; NTM has no reject state
            # s is a list; it is used as the initial tape;
            # assumes head pointing to first symbol in s                
            # If it doesn't reach an accepting state with all transitions of lenght k, return false.
            # Complete this code!

            #   APPROACH: EVERY TIME THAT THE CODE ARRIVES AT MULTIPLE POSSIBILITIES, EACH NEW POSSIBILITY IS 
            #   CHECKED. EACH NEW STATE IS ADDED TO THE ALL INCLUSIVE ARRAY ("all_strings")   

            #   En Español:Cada vez cuando la programa llega a multiplicas oportunidades, cada nueva 
            #   oportunidad se unie con el todo_vector("all_strings")

            #holds value of transitions length =k
            state_transitions=[self.q0]
            s.append('_')
            curr_tape = s
            head=0
            #the array to hold all possibilities of state transition length k
            #receives an object of this type: [(curr_state_transitions), (curr_tape), (head_pos)]
            all_possibilities = [[state_transitions, curr_tape, head]]

            
            #counter to store the current maximum state_transitions length
            max_transitions_len=1
            while(max_transitions_len<=k):
       
                #   1.SUB-ALGO TO FILTER OUT ALL THE POSSIBILITIES HAVING STATE_TRANSITIONS LENGTH LESS THAN MAXIMUM 
                #   2.SUB-ALGO TO CHECK IF ANY OF THE CURRENT POSSIBILITIES HAVE REACHED A FINAL STATE. RETURN TRUE IF YES
                index=0
                while(index<len(all_possibilities)):
                    #filters all state_transitions inside all_possibilities which have length of less than max_transitions_len
                    if(len(all_possibilities[index][0])<max_transitions_len):
                        del all_possibilities[index]
                        index=index-1
                    #Checks to see if any of the possibilities reach a final accept state
                    else:
                        #last current state
                        last_state = all_possibilities[index][0][len(all_possibilities[index][0])-1]
                        if(last_state == 'accept'):
                            print("FOUND IT :) : ", all_possibilities[index][0])
                            return True
                    index=index+1
                        


                #   SUB-ALGO TO ITERATE OVER ALL CURRENT POSSIBILITIES 
                #   counter for iterating over the all_possibilities array 
                counter_2=0
                curr_all_possblts = len(all_possibilities)
                while(counter_2<curr_all_possblts):
                    #curr_last_state of the possibility currently adding to 
                    last_index = len(all_possibilities[counter_2][0]) - 1
                    curr_last_state = all_possibilities[counter_2][0][last_index]      #triple matrix woah
                    for key,value in self.Delta.items():
                        #when the last state of state_transitions and k1 match
                        if(key == curr_last_state):
                            for k1,v1 in value.items():
                                #case for current tape[head] matching the symbol for state in delta 
                                no_transition= True
                                curr_head = all_possibilities[counter_2][2]
                                if(k1==all_possibilities[counter_2][1][curr_head]):
                                    no_transition = False
                                    #case 1: only one possibility is  
                                    if(len(v1)==1):
                                        #add to the state_transitions
                                        temp_state_trans = []
                                        temp_state_trans.extend(all_possibilities[0][0])
                                        temp_state_trans.extend([v1[0][0]])
                                        #update the tape 
                                        all_possibilities[counter_2][1][curr_head]=v1[0][1]
                                        temp_tape = all_possibilities[counter_2][1]
                                        #create/update the head variable 
                                        if(v1[0][2]=='R'):
                                            #to store head 
                                            temp_head= all_possibilities[counter_2][2] + 1
                                        if(v1[0][2]=='L'):
                                            #to store head 
                                            temp_head= all_possibilities[counter_2][2] - 1
                                        all_possibilities.append([temp_state_trans, temp_tape, temp_head])
                                        break
                                    #case 2: multiple possibilities, branch the curr possibiility into more possibilities
                                    if(len(v1)>1):
                                        #number of different possibilities
                                        branches = len(v1)
                                        counter_3=0
                                        while(counter_3<branches):
                                            #add to the state_transitions
                                            temp_state_trans = []
                                            temp_state_trans.extend(all_possibilities[counter_2][0])
                                            temp_state_trans.extend([v1[counter_3][0]])            
                                            #update the tape 
                                            all_possibilities[counter_2][1][curr_head]=v1[counter_3][1]
                                            temp_tape = all_possibilities[counter_2][1]
                                            #create/update the head variable 
                                            if(v1[counter_3][2]=='R'):
                                                #to store head 
                                                temp_head= all_possibilities[counter_2][2] + 1
                                            if(v1[counter_3][2]=='L'):
                                                #to store head 
                                                temp_head= all_possibilities[counter_2][2] - 1
                                            all_possibilities.append([temp_state_trans, temp_tape, temp_head])
                                            #move to next branch
                                            counter_3+=1
                                        break
                                        
                            #case for no transitions, after all of k1,v1 has been checked/iterated over
                            break
                            
                    #increment while loop to move to another possibility  
                    counter_2+=1                   
                max_transitions_len+=1
            print("\n\n\n")
            
            
            return False
        