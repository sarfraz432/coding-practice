

def group_anagrams(words):
    main_dict = {}
    for word in words:
        cur_dict = {}
        key = "".join(sorted(word))
        if key in main_dict:
            main_dict[key].append(word)  
        else: 
            main_dict[key] = [word]

    return list(main_dict.values())

words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
out_list = group_anagrams(words_list)

print(out_list)