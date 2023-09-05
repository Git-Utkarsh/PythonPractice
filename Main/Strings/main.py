#Question: Write a Python function that takes a string as input and returns the string with all the vowels replaced by the character '#'. For example, if the input is "Hello, how are you?", the function should return "H#ll#, h#w #r# yo#?".

def vowel_replace(strin):
    return strin.replace("a","#").replace("e","#").replace("i","#").replace("o","#").replace("u","#")
