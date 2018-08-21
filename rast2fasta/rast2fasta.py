import os,sys

def rast2fasta(input_file):
    annotation=open(input_file)
    annotation.readline()
    annotation_fasta=open(input_file.replace(".txt","")+".fasta","w+")

    for i in annotation:
        i=i.split("\t")
        if len(i[12])>1:
            annotation_fasta.write(">"+i[3].replace("|","_")+"\n"+i[12])
    annotation.close()
    annotation_fasta.close()
	
for myfile in sys.argv[1:]:
    rast2fasta(myfile)
    print "Done with "+myfile