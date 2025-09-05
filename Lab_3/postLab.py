#reverse
st="python"
print("Reverse:",st[::-1])

#palindrome
st1="aba"
print(st1==st1[::-1])
print(st==st[::-1],"\n")

#only digits
st2="98766"
print(st2.isdigit())
print(st1.isdigit())

#longest word in a sentence
st4="python programming is fun"
words=st4.split()
print(max(words,key=len))

#last word
words=st4.strip().split()
print(len(words[-1])if words else 0)