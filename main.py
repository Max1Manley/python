meep = input("what are you looking for?")
zoo = ["elephant", "tiger", "lion", "bear"]
count = 0
for i in zoo:
    if meep == i:
        print("wow. very cool, I found a", i)
    else:
        count += 1
    print(count)
    if count >= len(zoo):
        print('no matches found')
#just seeing if i can cause some problems!
        #adding more comments for practice.