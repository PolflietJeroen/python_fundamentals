'''
    some comment
'''
def to_piglatin(st4):
    '''
    some comment
    '''
    st3 = ' '
    count = first = len(st4)
    vowel = "aeiou"
    for letter in vowel:
        if letter in st4:
            count = st4.index(letter)
        if count < first:
            first = count
    if first == len(st4):
        st3 = st4[:first] +'-ay'
    else:
        st3 = st4[first:] + '-' + st4[:first] + 'ay'
    return st3
def from_piglatin(st4):
    '''
    some comment
    '''
    st5 = ' '
    index = st4.index("-")
    indexx = st4.index("ay")
    st5 = st4[index+1:indexx] + st4[:index]
    return st5

if __name__ == "__main__":
    F = open("text.txt", "r")
    FI = open("piglatin.txt", "w")
    FIL = open("result.txt", "w")
    for line in F:
        line2 = ''
        l = line.split()
        for st in l:
            st2 = to_piglatin(st)+' '
            line2 += st2
        FIL.write(line[:len(line)-1] + ' => ' +line2 + '\n')
        FI.write(line2 + '\n')
    F.close()
    FI.close()
    FIL.close()

    FF = open("piglatin.txt", "r")
    FFII = open("finalresult.txt", "w")
    for line in FF:
        line2 = ''
        l = line.split()
        for st in l:
            st2 = from_piglatin(st)+' '
            line2 += st2
        FFII.write(line[:len(line)-1] + ' => ' +line2 + '\n')
    FF.close()
    FFII.close()
