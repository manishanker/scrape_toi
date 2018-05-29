import numpy as np

with open('batch2.txt','r') as f:
	lines=f.readlines()


with open('cleaned_lines.txt','w') as f1:
	for line in lines:
		if '#' in line:
			continue
		if len(line.split())==0:
			continue
		line=line.rstrip()
		f1.write(line+'\n')
