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

def load(filename):
    """Load from a named database"""
    global words, yes, no    

    print("Loading database...")
    try:
        f = open(filename)
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


def save(filename):
    """Save the database to a file"""

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
    

def banner():
    """Display a friendly banner on the screen"""
    print("\nGUESSING GAME")
    print("Think of an animal")    


def isDatabaseEmpty():
    """Work out if the database is empty or not"""
    if len(words) == 0:
        return True
    return False


def isLeaf(pos):
    """Is this node a leaf node?"""
    if yes[pos] == None:
        return True
    return False


def appendLeaf(name):
    """Add this name as a leaf node to end of database"""
    global words, yes, no
    words.append(name)
    yes.append(None)
    no.append(None)


def makeBranch(pos, question, yespos, nopos):
    """Turn node at pos into a branch node"""
    global wirds, yes, no
    words[pos] = q
    yes[pos]   = yespos
    no[pos]    = nopos


def restructureTree(pos, question, name, answer):
    """Restructure the tree at pos to insert a new item"""
    appendLeaf(words[pos]) # move existing leaf node to a new node
    appendLeaf(name) # add a new leaf node for the new name

    # work out positions of two leafs, for ease of use later
    lastpos = len(words)-2 # pos of last asked leaf
    newpos  = len(words)-1 # pos of new answer leaf

    # Change old leaf node into a branch node with the question and two answers
    if a == "yes":
        makeBranch(pos, q, newpos, lastpos)
    else:
        makeBranch(pos, q, lastpos, newpos)


def walkTree(pos, answer):
    """Walk the tree from this node, based on the answer.
       Returns the new position in the tree"""
    if a == "yes":
        newpos = yes[pos]
    else:
        newpos = no[pos]
    return newpos


# MAIN PROGRAM

load(DATABASE_NAME)

# Main game loop
anothergo = True
while anothergo:
    banner()

    finished = False
    pos = 0

    # Question asking loop
    while not finished:
        # Ask the next question
        
        if isDatabaseEmpty():
            # no questions to ask, so just learn an answer
            name = raw_input("What is it? ")
            appendLeaf(name)
            finished = True

        elif isLeaf(pos):
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

                # Restructure the tree to account for question and new answer
                restructureTree(pos, q, name, a)
                
            finished = True

        else: # must be a branch node with two outcomes
            # ask the question
            a = raw_input(words[pos] + "? ")

            # walk the tree based on the answer
            pos = walkTree(pos, a)
        

    again = raw_input("another go? ")
    if again != "yes":
        anothergo = False
 
print("Thanks for playing the game!")

save(DATABASE_NAME)

    
