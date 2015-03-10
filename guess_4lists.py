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
    #pos = 0
    
    while not finished:
        # is pos a branch node?
        #   ask multi choice question
        #   yes: take yes branch
        #   no:  take no branch
        
        # is it a leaf node?
        #   ask "is it a"
        #   did I get it right?
        #       congratulate myself
        #   not right
        #       ask "what is it"
        #       ask "distinguishing question"
        #       ask "answer for your new item"
        #   finished = True

        # is it an empty list?
        if len(names) == 0: # list is empty
            name = raw_input("What is it?")
            finished = True

    again = raw_input("another go?")
    if again != "yes":
        anothergo = False
 
print("Thanks for playing the game")

#TODO save file to disk

    
