'''
PROBLEM) Strings: Making Anagrams
'''

# my solution
def makeAnagram(a, b):
    common_num = 0
    a_dict = {c:a.count(c) for c in a}
    for key in a_dict:
        common_num += min(a_dict[key], b.count(key))
    return len(a)+len(b)-2*common_num

# another solution using Counter
from collections import Counter
def makeAnagram_v2(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())


'''
PROBLEM) Alternating Characters
'''

def alternatingCharacters(s):
    l = list(s)
    for i in range(len(l)-1):
        if s[i:i+2] == 'AA' or s[i:i+2] == 'BB':
            l.remove(s[i])
    return ''.join(l)
        

'''
PROBLEM) Sherlock and the Valid String
'''

# first trial - fails to pass 4/20 test cases
# because AABBC should return 'YES'
def isValid(s):
    from collections import Counter
    ctr = Counter(s)
    freq = Counter(ctr.values()).most_common()
    length = len(freq)
    # if all of the characters are with the same frequency
    if length == 1:
        return 'YES'
    # when there's only two types of frequencies (3, 3, 2, 2), (4, 1), ...
    # and the character with the least frequency is 1, we can take it out
    elif length == 2:
        # frequncies of frequencies (3:2, 2:2), (4:1, 1:1), ...
        if (freq[1][1]*freq[1][0] == 1) or (freq[1][1] == 1 and abs(freq[0][0]-freq[1][0]) == 1):
            return 'YES'
    return 'NO'
    # or in elif block
    # elif length == 2:
    # if ctr[key1] == 1 and (key1-1 == key2 or key1 == 1):
    #     return 'YES'
    # elif ctr[key2] == 1 and (key2-1 == key1 or key2 == 1):
    #     return 'YES'



'''
PROBLEM) Special String Again
''' 

# first trial - 14/17 fails to pass (timeout)
def substrCount(n, s):
    count = n
    for i in range(n-1):
        for j in range(i+1, n):
            temp = s[i:j+1]
            boolean = True
            prev = None
            for k in range(len(temp)//2):
                if (temp[k] != temp[-k-1]) or (prev != None and prev != temp[k]):
                    boolean = False
                    break
                prev = temp[k]
            if boolean:
                count += 1
    return count

def substrCount_v2(n, s):
    for i in range(n):
        first = s[i]
        for length in range(1, n, 2):   # length is 1, 3, 5, ...


        #for length in range(2, n, 2):   # length is 2, 4, 6 ...
                count += 1
            
        




if __name__ == '__main__':
    print(alternatingCharacters('AAAA'))
    print(alternatingCharacters('ABABABA'))

    print("- - - - - - - - - - - - - - -")

    print(isValid('aabbcd'))                # NO    {2:2, 1:2}
    print(isValid('AABBC'))                 # YES   {2:2, 1:1}
    print(isValid('abcdefghhgfedecba'))     # YES   {2:7, 3:1}
    print(isValid('aaaab'))                 # YES   {4:1, 1:1}
    s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    print(isValid(s))                       # YES   {111:9, 1:1}
    print(isValid('aaaabbcc'))              # NO    {2:2, 4:1}

    print("- - - - - - - - - - - - - - -")

    print(substrCount(5, 'asasd'))     # 7 (a,s,a,s,d,asa,sas)
    print(substrCount(7, 'abcbaba'))   # 10
    print(substrCount(4, 'aaaa'))      # 10

    print(substrCount_v2(5, 'asasd'))     # 7 (a,s,a,s,d,asa,sas)
    print(substrCount_v2(7, 'abcbaba'))   # 10
    print(substrCount_v2(4, 'aaaa'))      # 10