import numpy as np
import nltk

with open('toi.txt','r') as f:
	lines=f.readlines()

stop_chars=[',','_',';',')','(','{','}','[',']','*','&','^','%','$','#','@','!','~','|','/','+','`',':']
with open('final_toi.txt','w') as f1:
	for line in lines:
		line=line.rstrip()
		sentences=nltk.sent_tokenize(line)
		for sent in sentences:
			new_sent=""
			for i in sent:
				if i not in stop_chars:
					new_sent+=i
			sen=new_sent.split('.')
			
			for s in sen:
				l=len(s.split())
				if(l<25 and l>3):
				
					f1.write(s+"\n")
				else:
					continue
				
			
	


