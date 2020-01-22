def funWithAnagrams(text):
     res = [text[0]]
     for i, j in enumerate(text):
         flag = [1 for k in res if sorted(k) == sorted(text[i])]
         if len(flag) == 0:
             res.append(j)
     return res


print(funWithAnagrams(['aaa', 'bbb', 'aaa', 'ccc']))

