import os

files = os.listdir("./set/valid/labels") #test valid

for file in files:
    print(file)
    if (file.endswith(".txt")):
        strings = list()
        new_strings = []
        with open("./set/valid/labels/" + file, "r") as fl:
            strings = fl.readlines()
        for string in strings:
            new_string = ""
            if string[0] == "0":
                new_string = "3" + string[1:]
            elif string[0] == "2":
                new_string = "2" + string[1:]
            elif string[0] == "1":
                new_string = "9" + string[1:]
            elif string[0] == "3":
                new_string = "3" + string[1:]
            new_strings.append(new_string)
        with open("./reworked/val/labels/" + file, "w+") as fl:
            for string in new_strings:
                fl.write(string)
            