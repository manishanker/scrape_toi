# Author : Manishanker Talusani

# Python file to remove bad words which would come while transcribing speech to text
# from Times of india news paper data
# !/usr/bin/python -tt
# -*- coding: utf-8 -*-

from nltk.tokenize import sent_tokenize
import subprocess as sbp
import os.path
import linecache
import cPickle as pickle



'''
    43 COIMBATORE: The Coimbatore city police arrested two persons on Saturday night for raping a mentally-challenged woman. Both of them were remanded to judicial custody.

'''
def populate_verb_forms(root_words):
    '''
    Function to create new text file in catvar_output with the search string
    and extract the verb forms of the search string
    '''
    glbl_bad_words= {}
    fin=set()
    if os.path.isfile('bad_words_dict.p'):
        glbl_bad_words = pickle.load(open("bad_words_dict.p", 'rb'))

    for x in root_words:
        arr=[]
        start=0           #CVsearch gives all the verb forms of all the words where the search string is a substring also
        end=0             # we are interested only in the search string
        #print "root word is ", x
        file_name = "catvar_output/" + x + ".txt"
        if not os.path.isfile(file_name):
            f=open(file_name, 'w')
            print "Going to call catvar"
            sbp.call(["perl", "catvar/CVsearch.pl", x], stdout=f)
            f.close()

            inp= open(file_name, 'r')
            print "opened the file", file_name
            for line_number, y in enumerate(inp.readlines()):
            #print y
                if x in y.split('\t') and start == 0:
                    start=line_number + 1
                    end =start
                if end !=0 and y.startswith('-'):
                    end = line_number + 1
                    break
            inp.close()

            print " start. end ", start, end
            for k in range(start, end):
                line = linecache.getline(file_name, k)
                p = line.split('\t')[0]
                if p not in arr:
                    arr.append(p)
            print "arr", arr
            glbl_bad_words[x] = arr
            pickle.dump(glbl_bad_words, open('bad_words_dict.p', 'wb'))
        #print glbl_bad_words

    for _,x in glbl_bad_words.iteritems():
        for k in x:
            fin.add(k)

    return fin

def detect_sentence(passage):
    try:
        sent_tokenize_list = sent_tokenize(passage)
        return sent_tokenize_list
    except:
        print "error", passage
        return []

def does_bad_word_exist(sent, bad_words_set):
    for x in bad_words_set:
        if x in sent:
            return True
    return False

if __name__ == '__main__':
    root_words = ['murder', 'rape', 'kill', 'kidnap', 'abuse', 'manslaughter' ]   #if the files murder.txt already exist, catvar will not be called, adding new words

    glbl_bad_words = populate_verb_forms(root_words)
    #print "final words", glbl_bad_words
    with open('TOI_CONTENT.txt', 'r') as inp:
        with open('final.txt', 'w') as out:
            for x in inp.readlines():
                sent_tokenize_list = detect_sentence(x.lower())
                if sent_tokenize_list:
                    #print "sent not empty0", sent_tokenize_list
                    for k in sent_tokenize_list:
                        ret = does_bad_word_exist(k, glbl_bad_words)
                        #print "ret", ret
                        if not ret:
                            out.write(k + "\n")