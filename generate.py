def getOp(char):
    if char == '1':
        return '2'
    elif char == '2':
        return '1'

def makeSequence(begin):
    return makeSequenceOpt(begin, 1)

def makeSequenceOpt(begin, startAt):
    starting = begin[:startAt]
    for i in begin[startAt:]:
        add = getOp(starting[-1])
        if i == '2':
            starting = starting + add + add
        elif i == '1':
            starting = starting + add
    return starting

def getGrowthSequence(begin, n):
    growth = []
    length = [len(begin)]
    current = begin
    for i in range(n):
        lenBefore = len(current)
        current = makeSequence(current)
        lenAfter = len(current)
        growth.append(lenAfter - lenBefore)
        length.append(lenAfter)
    return (length, growth)
