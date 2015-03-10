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
                a = raw_input("What is the answer to this question for " + name + "? ")
                
                # Move existing leaf node to a new node
                names.append(names[pos])
                questions.append(None)
                yes.append(None)
                no.append(None)
                
                #add new leaf node for new name
                names.append(name)
                questions.append(None)
                yes.append(None)
                no.append(None)

                # Change old leaf node into a branch node with the question
                names[pos] = None
                questions[pos] = q

                # wire up the yes/no branches correctly
                if a == "yes": # yes branch goes to new item
                    yes[pos] = len(names)-1
                    no[pos]  = len(names)-2
                else: # no branch goes to new item
                    no[pos]  = len(names)-1
                    yes[pos]= len(names)-2

            finished = True

        else: # It must be a branch node with two outcomes
            #TODO: ask multi choice question
            #   yes: take yes branch
            #   no:  take no branch
            print("Branch node: pos:" + str(pos))
            print("q:" + questions[pos])
            print("yes:" + str(yes[pos]))
            print("no:"  + str(no[pos]))
            print("questions:" + str(questions))
            print("names:" + str(names))
            finished = True
        

    again = raw_input("another go?")
    if again != "yes":
        anothergo = False
 
print("Thanks for playing the game")

#TODO save file to disk

    
