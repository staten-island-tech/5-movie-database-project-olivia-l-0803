import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

print(len(data))

#Part One
def partone():
    for i in range(0, len(data)):
        print(data[i]["title"])

#part two


def partTWO():
    useranswer2 = int(input("Look up movies from after this year: "))
    for i in range(0, len(data)):
        year = data[i]["year"]
        if year > useranswer2:
            print(data[i]["title"])


#part three
def part3():
    useranswer3a = int(input("Movies after this year: "))
    useranswer3b = int(input("Movies before this year: "))

    
    for i in range(0, len(data)):
        year = data[i]["year"]
        if year > useranswer3a and year < useranswer3b :
            print(data[i]["title"])
#part3()

def part4():
    useranswer4 = int(input("Movies made "))
    for i in range(0, len(data)):
        year = data[i]["year"]
        if year == useranswer4
            print(data[i]["title"])