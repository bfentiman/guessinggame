# guess_4lists.py  10/03/2015  D.J.Whale
#
# A guessing game, using a binary tree structure
# The binary tree is implemented using 4 lists
# This is a version for children who don't know about lists of lists yet

#TODO load file from disk

# the tree starts off empty
names     = []
questions = []
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
        if len(names) == 0: # list is empty
            name = raw_input("What is it? ")
            
            # add item to the tree
            names.append(name)
            questions.append(None)
            yes.append(None)
            no.append(None)
            finished = True
            
        elif questions[pos] == None: # is it a leaf node?
            # ask a terminating question
            gotit = raw_input("Is it a " + names[pos] + "? ")
            # did I get it right?
            if gotit == "yes":
                # congratulate myself
                print("I guessed it!")
            else: # I didn't guess it
                print("I didn't guess it")
                name = raw_input("What is it? ")
                # ask distinguising question
                q = raw_input("Please give a question to distinguish between " + names[pos] + " and " + name+ ":" )
                # ask answer for your new item
                a = raw_input("What is the answer to this question for " + name + "?" )
                #TODO: add new leaf node for new name
                #TODO: move old leaf node to a new node
                #TODO: change leaf node to a branch node, to join two leaf nodes
                #make sure the y/n branches are correct
            finished = True

        else: # It must be a branch node with two outcomes
            #   ask multi choice question
            #   yes: take yes branch
            #   no:  take no branch
            finished = True
        



    again = raw_input("another go?")
    if again != "yes":
        anothergo = False
 
print("Thanks for playing the game")

#TODO save file to disk

    
