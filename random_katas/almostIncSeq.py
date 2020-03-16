def almostIncreasingSequence(sequence):
    def firstbad(sequence):
        for i in range(len(sequence)-1):
            if sequence[i]>=sequence[i+1]:
                return i
        return -1
    j = firstbad(sequence)
    if j==-1:
        return True
    if firstbad(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    if firstbad(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True
    return False
