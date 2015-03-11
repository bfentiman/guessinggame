# guess_3lists.py  10/03/2015  D.J.Whale
#
# A guessing game, using a binary tree structure
# The binary tree is implemented using 3 lists
# This is a version for children who don't know about lists of lists yet

DATABASE_NAME = "animals.txt"

# the tree starts off empty
words     = []
yes       = []
no        = []

# load file from disk
print("Loading database...")
try:
    f = open(DATABASE_NAME)
    for line in f.readlines():
        line = line.strip() # remove newline
        print(line)
        word, ypos, npos = line.split(",", 2)
        words.append(word)
        if ypos == "None":
            yes.append(None)
        else:
            yes.append(int(ypos))
        if npos == "None":
            no.append(None)
        else:
            no.append(int(npos))
    f.close()
    print("Done")
    
except IOError:
    print("No database, starting empty")



# Main game loop
anothergo = True
while anothergo:
    # display banner
    print("\nGUESSING GAME")
    print("Think of an animal")

    finished = False
    pos = 0

    # Question asking loop
    while not finished:
        # Ask the next question
        
        # is it an empty list?
        if len(words) == 0: # list is empty
            # no questions to ask, so just learn an answer
            name = raw_input("What is it? ")
            
            # add new item to the tree
            words.append(name)
            yes.append(None)
            no.append(None)
            finished = True

        # is it a leaf node?
        elif yes[pos] == None:
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
                    yes[pos] = len(words)-2

            finished = True

        # It must be a branch node with two outcomes
        else:
            # ask the question
            a = raw_input(words[pos] + "? ")
            if a == "yes":
                pos = yes[pos]
            else:
                pos = no[pos]
        

    again = raw_input("another go? ")
    if again != "yes":
        anothergo = False
 
print("Thanks for playing the game!")

# save file to disk

print("Saving data base...")
f = open(DATABASE_NAME, "wt")
for pos in range(len(words)):
    word = words[pos]
    y    = yes[pos]
    n    = no[pos]
    line = word + "," + str(y) + "," + str(n) + "\n"
    f.write(line)
f.close()

print("Database saved")

    
