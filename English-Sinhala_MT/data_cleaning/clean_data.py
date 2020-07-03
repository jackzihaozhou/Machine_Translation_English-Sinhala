
# import Levenshtein

raw_train_en = open("enhi_parallel.train.en", "r",encoding="utf-8")
raw_train_af = open("enhi_parallel.train.hi", "r",encoding="utf-8")
# dev_en = open("wikipedia_en_ne_si_test_sets/wikipedia.dev.si-en.en", "r",encoding="utf-8")
# dev_si = open("wikipedia_en_ne_si_test_sets/wikipedia.dev.si-en.si", "r",encoding="utf-8")
# test_en = open("wikipedia_en_ne_si_test_sets/wikipedia.devtest.si-en.en", "r",encoding="utf-8")
# test_si = open("wikipedia_en_ne_si_test_sets/wikipedia.devtest.si-en.si", "r",encoding="utf-8")
new_train_en = {}
new_train_af = {}

# dev_and_test_en = []
# dev_and_test_si = []
# for line in dev_en:
#     dev_and_test_en.append(line[:50])
# for line in test_en:
#     dev_and_test_en.append(line[:50])
#
# for line in dev_si:
#     dev_and_test_si.append(line[:50])
# for line in test_si:
#     dev_and_test_si.append(line[:50])

punctuations = [',',':', ';', '?', '(', ')', '[', ']', '{', '}','&', '!', '*', '@', '#', '$', '\\','%', '<', '>', '/', '=','-','~']
number = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
bad_punc = [':', ';', '[', ']', '&', '*', '{', '}', '@', '#', '$', '\\', '%', '<', '>', '/', '=', '-', '_', '~']

en_list = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
en_letter = en_list.split(" ")
n = 1
remove_list = []
previous_two = ''
previous_one = ''
same_line = 0
long_line = 0
for line in raw_train_en:
    en_letter_num = 0
    line = line.replace(" ,", ",")
    line = line.replace(" .", ".")
    line = line.replace(" :", ":")
    line = line.replace(" ;", ";")
    line = line.replace(" !", "!")
    line = line.replace(" ?", "?")
    line = line.replace(" )", ")")
    line = line.replace("[", "")
    line = line.replace("]", "")
    new_train_en[n] = line
    # for word in line:
    #     if word in en_letter:
    #         en_letter_num += 1

    # sim1 = Levenshtein.ratio(line, previous_one)
    # sim2 = Levenshtein.ratio(line, previous_two)
    if line[-2:-1] == "-" or line[:1] == "-" or  line[-3:] =="..." :
        remove_list.append(n)
    # if line[:50] in dev_and_test_en and n not in remove_list:
    #     same_line += 1
    #     remove_list.append(n)
    if len(line) > 2000 and n not in remove_list:
        long_line += 1
        remove_list.append(n)

    # previous_two = previous_one
    # previous_one = line
    n = n + 1


n = 1
for line in raw_train_af:
    line = line.replace(" ,", ",")
    line = line.replace(" .", ".")
    line = line.replace(" :", ":")
    line = line.replace(" ;", ";")
    line = line.replace(" !", "!")
    line = line.replace(" ?", "?")
    line = line.replace(" )", ")")
    line = line.replace("[", "")
    line = line.replace("]", "")
    new_train_af[n] = line
    # for word in line:
    #     if word in en_letter and n not in remove_list:
    #         remove_list.append(n)
    # if line[:50] in dev_and_test_si and n not in remove_list:
    #     remove_list.append(n)
    #     same_line += 1
    if len(line) > 2000 and n not in remove_list:
        long_line += 1
        remove_list.append(n)

    n = n + 1

print("long line = ", long_line)
print("same line = ", same_line)
print("remove num = ", len(remove_list))
for i in remove_list:
    new_train_en.pop(i)
    new_train_af.pop(i)

right_en = open("enhi_parallel.train.en.new", "w",encoding="utf-8")
right_nso = open("enhi_parallel.train.hi.new", "w",encoding="utf-8")

for i in new_train_en.keys():
    right_en.write(new_train_en[i])
    right_nso.write(new_train_af[i])



raw_train_en.close()
raw_train_af.close()

right_nso.close()
right_en.close()
# dev_si.close()
# dev_en.close()
# test_en.close()
# test_si.close()