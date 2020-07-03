import Levenshtein
raw_train_en = open("clean_7.en", "r",encoding="utf-8")
raw_train_si = open("clean_7.si", "r",encoding="utf-8")

new_train_en = {}
new_train_si = {}
remove_list = []

n = 0
for line in raw_train_en:
    new_train_en[n] = line
    prev_line = line

    n += 1


similar = {}
start = 54000
end = 64000
for i in range(start, end):
    similar[i] = []

for i in range(start, end):
    line = new_train_en[i]
    for j in range(i+1, end):
        other_line = new_train_en[j]
        likely = Levenshtein.ratio(line, other_line)
        if likely > 0.8:
            similar[i].append(j)
    # print(i, similar[i])

for i in similar.keys():
    if len(similar[i]) != 0:
        for sentence in similar[i]:
            if sentence not in remove_list:
                remove_list.append(sentence)


n = 0

for line in raw_train_si:
    new_train_si[n] = line
    n += 1


print("remove num = ", len(remove_list))
# print(remove_list)

for i in remove_list:
    new_train_en.pop(i)
    new_train_si.pop(i)

right_en = open("clean_final.en", "w",encoding="utf-8")
right_si = open("clean_final.si", "w",encoding="utf-8")

for i in new_train_en.keys():
    right_en.write(new_train_en[i])
    right_si.write(new_train_si[i])

raw_train_en.close()
raw_train_si.close()

right_si.close()
right_en.close()
