import sys
from Bio import SeqIO

def n50(myfasta):
    contigsLength = []
    sum = 0
    
    for seq_record in SeqIO.parse(open(myfasta), "fasta"):
        sum += len(seq_record.seq)
        contigsLength.append(len(seq_record.seq))

    teoN50 = sum / 2.0    
    contigsLength.sort()  
    contigsLength.reverse()    
       
    #checking N50
    testSum = 0
    N50 = 0
    for con in contigsLength:
        testSum += con
        if teoN50 < testSum:
            N50 = con
            break
       
    print myfasta+' N50: ' + str(N50)  


for myfasta in sys.argv[1:]:
    n50(myfasta)