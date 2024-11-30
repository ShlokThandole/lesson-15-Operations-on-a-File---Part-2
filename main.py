with open('empty.txt', 'w') as file:
    file.write("IN A WAR OF EGO THE LOSER ALWAYS WINS -BUDDAH")
file.close()

with open('empty.txt', 'r') as file:
    data = file.readlines()
    print("words in the file are........")
    for buddah in data:
        disciple = buddah.split()
        print(disciple)
file.close()