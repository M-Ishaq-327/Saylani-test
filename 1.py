#First try : 
# #for number of words:
# number_of_words = 0
# num_lines = 0
# with open(r'SampleFile.txt','r') as file:

#     data = file.read()
#     lines = data.split()
#     number_of_words += len(lines)
# print("number of words are:",number_of_words)


# #for number of lines:

# file = open("SampleFile.txt", "r")
# num_lines = 0

# for line in file:
#     num_lines += 1

# file.close()

# print("Number of lines:", num_lines)     

#second try:
def analyze_file():
    
    inputFile = r"SampleFile.txt" 
    count_char = 0
    mylist = []
    
    with open(inputFile, 'r') as file: #open file as read mode.
        
        lines = file.readlines()
        for line in lines:
            count_char += len(line)
            line = line.split(" ")
            for word in line:
                if word != '\n':   #space_sequence character use kiya h.                     
                    mylist.append(word)
              
    print(f"number of characters is {count_char}") # space bh shamil h.
    print(f"number of words is {len(mylist)}")
    print(f"number of lines is {len(lines)}")
        
analyze_file()


text = open("SampleFile.txt", "r") 
d = dict() 
def search_word():

    for line in text: 
        line = line.strip() #space khtm krta h
        line = line.lower() #all char convert into lower case
        words = line.split(" ") #line into word
                            
        for word in words: 
            if word in d: #check word is already in dict
                d[word] = d[word] + 1 
            else: 
                d[word] = 1

    # Print the contents of dictionary 
    for key in list(d.keys()): # dict ki sari keys mngwa li by using built_in method of keys() of dictionary.
        print(key, ":", d[key]) # key print hogi then : 'd[key]' ya uski value hogi like 1 or 2 or any number.

search_word()

    

