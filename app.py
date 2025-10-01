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
    useranswer = int(input("Look up movies from after this year: "))
    for i in range(0, len(data)):
        year = data[i]["year"]
        if year > useranswer:
            print(data[i]["title"])


#part three
def part3():
    useranswer1 = int(input("Movies after this year: "))
    useranswer2 = int(input("Movies before this year: "))

    
    for i in range(0, len(data)):
        year = data[i]["year"]
        if year > useranswer1 and year < useranswer2 :
            print(data[i]["title"])
part3()