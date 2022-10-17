class Solution:
    def canBeTypedWords1(self, text: str, brokenLetters: str) -> int:
        broken=set(brokenLetters)
        res=0
        text_list=text.split(' ')
        for word in text_list:
            if word.__len__()==0: continue
            for letter in word:
                if letter in broken:
                    res+=1
                    break
        return len(text_list)-res
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken=set(brokenLetters)
        res=0
        text_list=text.split(' ')
        for word in text_list:
            temp_set=set(word)
            if temp_set.intersection(broken).__len__()>=1:res+=1
        return len(text_list)-res

