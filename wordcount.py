# put your code here.
def word_count(file_name):
    file_opened = open(file_name)

    word_count_dict = {}
    #words_list = []

    for line in file_opened: #iterable for each line in file
        line_list = line.rstrip().split(" ")
        #print(line_list)

        for words in line_list:   #iterable for each word in lines of file
            #print(words)
            lower_word = words.rstrip(",").lower()
            word_count_dict[lower_word] = word_count_dict.get(lower_word,0) + 1
        
    return word_count_dict
        #word_count = {}
        # for letter in phrase: 
            #letter_count[letter] = letter_count.get(letter,0) + 1 
            #{ "Word" : count in numbers, "secon" : count in numbers }

    















    file_opened.close() 