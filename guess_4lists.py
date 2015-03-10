# guess_4lists.py  10/03/2015  D.J.Whale
#
# A guessing game, using a binary tree structure
# The binary tree is implemented using 4 lists
# This is a version for children who don't know about lists of lists yet

#TODO load file from disk

# the tree starts off empty
words     = []
yes       = []
no        = []

anothergo = True
while anothergo:
    # display banner
    print("GUESSING GAME")
    print("Think of an animal")

    finished = False
    pos = 0
    
    while not finished:
        # is it an empty list?
        if len(words) == 0: # list is empty
            # no questions to ask, so just learn an answer
            name = raw_input("What is it? ")
            
            # add new item to the tree
            words.append(name)
            yes.append(None)
            no.append(None)
            finished = True
            
        elif yes[pos] == None: # is it a leaf node?
            # ask a terminating question
            gotit = raw_input("Is it a " + words[pos] + "? ")
            # did I get it right?
            if gotit == "yes":
                # congratulate myself
                print("I guessed it!")
            else: # I didn't guess it
                # need to learn a question and an answer
                print("I didn't guess it!")
                name = raw_input("What is it? ")
                # ask distinguising question
                q = raw_input("Please give a question to distinguish between " + words[pos] + " and " + name + ":" )
                # ask answer for your new item
                a = raw_input("What is the answer to this question for " + name + "? ")
                
                # Move existing leaf node to a new node
                words.append(words[pos])
                yes.append(None)
                no.append(None)
                
                #add new leaf node for new name
                words.append(name)
                yes.append(None)
                no.append(None)

                # Change old leaf node into a branch node with the question
                words[pos] = q

                # wire up the yes/no branches correctly
                if a == "yes": # yes branch goes to new item
                    yes[pos] = len(words)-1
                    no[pos]  = len(words)-2
                else: # no branch goes to new item
                    no[pos]  = len(words)-1
                    yes[pos]= len(words)-2

            finished = True

        else: # It must be a branch node with two outcomes
            # Show some diagnostics
            print("Branch node: pos:" + str(pos))
            print("word:"  + words[pos])
            print("yes:"   + str(yes[pos]) + " which is:" + words[yes[pos]])
            print("no:"    + str(no[pos])  + " which is:" + words[no[pos]])

            # ask the question
            a = raw_input(words[pos] + "? ")
            if a == "yes":
                pos = yes[pos]
            else:
                pos = no[pos]
        

    again = raw_input("another go?")
    if again != "yes":
        anothergo = False
 
print("Thanks for playing the game")

#TODO save file to disk

    
