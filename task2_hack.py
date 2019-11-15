query = int(input().strip())
for i in range(query):
    string_ = input().strip()
    main_word = 'hackerrank'
    p = 0
    for l in string_:
        if l == main_word[p]:
            p += 1
        if p == len(main_word):
            break
    if p == len(main_word):
        print('YES')
    else:
        print('NO')
        


##регулярные выражения--search(pattern,string)
# import sys
# import re

# query = int(input().strip())
# for i in range(q):
#     string_ = input().strip()
    
#     pattern = ".*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*"
#     m = re.search(pattern, s)
#     if m is not None:
#         print("YES")
#     else:
#         print("NO")