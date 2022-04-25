for i in range(5):
    if (i == 2):
        continue
    print(str(i))

    '''
    We realize 2 was jumped.
    
    the for loop runs and when it got to the if statement, it checked for the condition.
    Once the condition was met, the code below it didn't run then went back to the beginning
    That's what the CONTINUE keyword does
    '''