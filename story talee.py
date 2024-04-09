import random

start = ["once upon a time", "In galaxy far far away", "1000 years back"]
charecters = ["king", "dinosaur", "dragon", "empereor", "monkey"]
names = ["bob", "andy", "tom", "michael", "jessy"]
actions = ["went for a walk", "went cycling", "had a disco party", "had played"]
endings = ["the end", "they all lived happily ever after"]

def choose(from_list, list_name):
    print("please choose an item from " + list_name)
    for i in range(len(from_list)):
        print(i, ":", from_list[i])

    option = input("choose a value or leave blank to choose one at random")



    if option.isnumeric():
        return from_list[int(option)]
    elif option == "":
        return random.choice(from_list)
    else:
        return option

print("{} there was a {} called {}. They {} and met a {}. {}".format(
    choose(start, "story beginning"),
    choose(charecters, "charecter"),
    choose(names, "name"),
    choose(actions, "what happens"),
    choose(charecters, "who they met"),
    choose(endings, "how the story ends")
))


