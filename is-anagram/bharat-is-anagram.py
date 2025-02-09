# %%
def is_anagram(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    else:
        matches = 0
        lis_1 = list(str_1)
        lis_2 = list(str_2)
        for i in range(len(lis_1)):
            letter = lis_1[i]
            if letter in lis_2:
                elmnt = lis_1[i]
                lis_2.remove(elmnt)
                matches += 1
        if len(lis_1) == matches:
            return True
        else:
            return False
        
print(is_anagram("cautioned", "education"))
print(is_anagram("cat", "rat"))

# %%



