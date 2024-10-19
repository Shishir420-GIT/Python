def count_word_frequency(sentence):
    if sentence == "":
        return {}
    word_list = sentence.split(" ")
    my_records = {}
    for word in word_list:
        if my_records.get(word):
            my_records[word] += 1
        else:
            my_records[word] = 1
        
    return my_records
