#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverse(sentence, reverse_word):
    if  type(reverse_word) != str:
        return "invalid input"
    lst = sentence.split()
    if reverse_word not in lst:
        return "The word was not found"
    else:
        for i in range(len(lst)):
            if lst[i] == reverse_word:
                lst[i] = rev(lst[i])
                break
        ans = ""
        for i in range(len(lst)-1):
            ans += lst[i] + " "
        ans += lst[len(lst)-1]    
        return ans


def rev(word):
    new_word = ''
    for i in range(len(word)):
        new_word += word[len(word)-1-i]
    return new_word

