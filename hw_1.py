str1 = "The Zen of Python, by Tim Peters"
print(str1)
dzen = "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex." \
       "\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense." \
       "\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats " \
       "purity. " \
       "\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the " \
       "temptation to guess." \
       "\nThere should be one-- and preferably only one --obvious way to do it. " \
       "\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never." \
       "\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea." \
       "\nIf the implementation is easy to explain, it may be a good idea. " \
       "\nNamespaces are one honking great idea -- let's do more of those!"
print(dzen.upper())
words = dzen.split()
counter = 0
for i in words:
    if i == "better" or i == "never" or i == "is":
        counter += 1
print("\nYou can meet words: 'is', 'better', 'never'", counter, "times")
replaced_dzen = dzen.replace('i', "&")
print("\n***replaced dzen***", "\n" + replaced_dzen)

# for i in words:
#        slovo = i
#        for j in range(len(slovo)):
#               if slovo[j] == "i":
#                      print("yes")
#                      print(slovo)
#                      slovo[j] = "&"
#                      print(slovo)
#               continue

