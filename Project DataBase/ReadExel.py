import pandas as pd  
import nltk
import string

from collections import Counter
nltk.download()


path = "/home/robihidayat/Gawe/MediaTrac/DataMediaTrack/Project/test.csv"

def main():
  
   #buka file
    data = pd.read_csv(path, error_bad_lines=False)
    # kalkulasikan data
    # print("Total rows: {0}".format(len(data)))
    # print(list(data))
    # line     = []
    # expected = []
    # saw      = []     
    # cont     = True 

    # while cont == True:     
    #     try:
    #         data = pd.read_csv(path, error_bad_lines=False)
    #         print("Total rows: {0}".format(len(data)))
    #         cont = False
    #     except Exception as e:    
    #         errortype = e.message.split('.')[0].strip()                                
    #         if errortype == 'Error tokenizing data':                        
    #             cerror      = e.message.split(':')[1].strip().replace(',','')
    #             nums        = [n for n in cerror.split(' ') if str.isdigit(n)]
    #             expected.append(int(nums[0]))
    #             saw.append(int(nums[2]))
    #             line.append(int(nums[1])-1)
    #         else:
    #             cerror      = 'Unknown'
    #             print 'Unknown Error - 222'

def get_tokens():
   with open(path, 'r') as shakes:
    text = shakes.read()
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    no_punctuation = lowers.translate(None, string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
count = Counter(tokens)
print count.most_common(10)
   
      
if __name__ == "__main__":
    main()
    get_tokens()
    
    
 