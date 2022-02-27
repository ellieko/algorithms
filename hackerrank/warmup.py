from timeit import repeat


def repeatedString(s, n):
    return s.count('a')*(n//len(s)) + s[:n%len(s)].count('a')

    # got it wrong because didn't have parentheis in retun line. (n//len(s)) ...
    # it did make the result different
    
if __name__ =='__main__':
    # print(repeatedString('abc', 10)) 
    # print(repeatedString('a', 1000000000000))
    s = 'epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq'
    print(repeatedString(s, 549382313570))
    print('16481469408')