# put your code here.
def word_count(file_name):
    file_opened = open(file_name)

    word_count_dict = {}
    #words_list = []

    for line in file_opened:
        line_list = line.rstrip().split(" ")
        print(line_list)  #list per line
        














    file_opened.close() 