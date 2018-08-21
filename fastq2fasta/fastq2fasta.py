import sys,string

def fastq2fasta(fastq_name):
    fastq = open(fastq_name, 'r')
    fasta = open(((fastq_name[::-1]).replace('qtsaf', 'atsaf', 1))[::-1], 'w')
   
    while True:
        line = fastq.readline()
        line = string.strip(line)
        if line == '':
            break
        line = '>' + line[1:]
        seq_len = 0 - len(line)
        while line[0] != '+':
            seq_len = seq_len + len(line)
            fasta.write("%s\n" % (line))
            line = fastq.readline()
            line = string.strip(line)
        while seq_len != 0:
            line = fastq.readline()
            line = string.strip(line)
            seq_len = seq_len - len(line)
    fasta.close()
    fastq.close()
    
for fastq_name in sys.argv[1:]:
    fastq2fasta(fastq_name)
    print "Done with "+fastq_name
