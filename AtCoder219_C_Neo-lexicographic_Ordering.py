X = input("自分の好みのアルファベットの順番を記載してください：")
pos = {}
for i in range(26):
    pos[X[i]] = i + 1
#print(pos)

N = input("国民数を入力してください：")
S = []
for n in range(int(N)):
    name = input("国民の名前を入力してください：")
    S.append(name)

for j in range(int(N)):
    for k in range((int(N)-1), j, -1):
        word_count1 = len(S[k])
        word_count2 = len(S[k - 1])
        if word_count2 <= word_count1:
            for l in range(word_count2):
                if int(pos.get(list(S[k - 1])[l])) == int(pos.get(list(S[k])[l])):
                    continue
                elif int(pos.get(list(S[k - 1])[l])) < int(pos.get(list(S[k])[l])):
                    S[k], S[k - 1] = S[k], S[k -1]
                    #print(S)
                    break
                elif int(pos.get(list(S[k - 1])[l])) > int(pos.get(list(S[k])[l])):
                    S[k - 1], S[k] = S[k], S[k -1]
                    #print(S)
                    break
                else:
                    pass
        else:
            #word_count2 > word_count1
            for m in range(word_count1):
                if int(pos.get(list(S[k - 1])[m])) == int(pos.get(list(S[k])[m])):
                    continue
                elif int(pos.get(list(S[k - 1])[m])) < int(pos.get(list(S[k])[m])):
                    S[k], S[k - 1] = S[k], S[k -1]
                    #print(S)
                    break
                elif int(pos.get(list(S[k - 1])[m])) > int(pos.get(list(S[k])[m])):
                    S[k - 1], S[k] = S[k], S[k -1]
                    #print(S)
                    break
                else:
                    S[k - 1], S[k] = S[k], S[k -1]
                    #print(S)
            #print(S)



for x in range(int(N)):
    print(S[x])
