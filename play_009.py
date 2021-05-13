
#rite a function that stutters a word as if someone is struggling to read it. 
# The first two letters are repeated twice with an ellipsis ... and space after each, 
# and then the word is pronounced with a question mark ?.
#

def stutter(str):

    repeat = str[0:3] + '... '

    return repeat+repeat+str+'?'



print(stutter('exclusive'))

