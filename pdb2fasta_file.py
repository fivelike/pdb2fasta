import sys

if len(sys.argv) <= 1:
    print 'usage: python pdb2fasta.py file.pdb > file.fasta'
    exit()
    
input_file = open(sys.argv[1])

letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
           'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
           'TYR':'Y','VAL':'V'}
name=(sys.argv[1].split('.',1)[0])
filename=name+'.fasta'
name='>'+name+'\n';
f=file(filename,"w+")

f.writelines(name)
#print name
#print '>',name[0:len(name)]
prev = '-1'
for line in input_file:
    toks = line.split()
    if len(toks)<1: continue
    if toks[0] != 'ATOM': continue
    if toks[5] != prev:
        f.write('%c' % letters[toks[3]])
    prev = toks[5]

#sys.stdout.write('\n')
f.close()
input_file.close()
