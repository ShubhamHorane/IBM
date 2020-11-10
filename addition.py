# function to check if two strings are
# anagram or not
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)) and (len(s1) and len(s2) in range(0,100)):
        print("True")
    else:
        print("False")

    # driver code


s1 = input(str())
s2 = input(str())
check(s1, s2)