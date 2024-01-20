with open('input_file.txt','r') as ipf:#created a file named input_file and used read and split functions to read the file and split the words into several words as per the question
    line=ipf.read()
    word=line.split()
    with open('output_file.txt','w') as opf:
        for i in word: # Here i have iterated through word variable where the split of words are returned 
            opf.write(i+':'+str(word.count(i))+'\n')      
opf=open('output_file.txt','r')
print(opf.read())
