def recurbuildseq(seq):
    counter=0
    oneortwo=0
    seqout=[]
    while counter<len(seq):
        seqout = seqout + [oneortwo+1]*seq[counter]
        counter = counter + 1
        oneortwo = (oneortwo + 1) % 2
    return seqout

def buildseq(seq,n):
    output=seq
    iteration=0
    while iteration < n:
        output = recurbuildseq(output)
        iteration = iteration +1
    return output

print buildseq([1,2],8)

    
    
