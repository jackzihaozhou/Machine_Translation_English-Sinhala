raw_train_en = open("WikiMatrix.en-si.txt.en", "r",encoding="utf-8")
raw_train_si = open("WikiMatrix.en-si.txt.si", "r",encoding="utf-8")

punctuations = [',',':', ';', '?', '(', ')', '[', ']', '{', '}', '&', '!', '*', '@', '#', '$', '\\', '%', '<', '>', '/', '=', '-', '_', '~']
new_train_en = {}
new_train_si = {}
remove_list = []
bad_punc = [':', ';', '[', ']', '&', '*', '{', '}', '@', '#', '$', '\\', '%', '<', '>', '/', '=', '-', '_', '~']

n = 0
for line in raw_train_en:
    line = line.replace("[", "")
    line = line.replace("]", "")
    new_train_en[n] = line

    # if line[-3:] == "...":
    #     remove_list.append(n)
    # for word_n in range(len(line)):
    #     word = line[word_n]
    #     if word in bad_punc and n not in remove_list:
    #         remove_list.append(n)
    #         break
    #     if word == '.' and line[word_n+1] == '.' and line[word_n+2] == '.':
    #         if n not in remove_list:
    #             remove_list.append(n)
    #         break
    if len(line.split(" ")) <= 2:
        remove_list.append(n)

    n += 1


n = 0

for line in raw_train_si:
    new_train_si[n] = line
    for word_n in range(len(line)):
        word = line[word_n]
        if word in bad_punc and n not in remove_list:
            remove_list.append(n)
            break
        if word == '.' and line[word_n + 1] == '.' and line[word_n + 2] == '.':
            if n not in remove_list:
                remove_list.append(n)
            break
    n += 1

print("remove num = ", len(remove_list))
# print(remove_list)
for i in remove_list:
    new_train_en.pop(i)
    new_train_si.pop(i)

right_en = open("wiki-clean.en", "w",encoding="utf-8")
right_si = open("wiki-clean.si", "w",encoding="utf-8")

for i in new_train_en.keys():
    right_en.write(new_train_en[i])
    right_si.write(new_train_si[i])

raw_train_en.close()
raw_train_si.close()

right_si.close()
right_en.close()
