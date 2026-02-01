# ფაილი: task4.py
# შესაფასებელი ქულა: 0-3
# ამოცანა:
# დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებელს შემოატანინებს წინადადებას.
# პროგრამამ უნდა ჩაატაროს:
# თითოეული სიტყვის გასუფთავება პუნქტუაციისგან ანუ უნდა მოაცილოთ თითეულ სიტყვას (წერილი მძიმე ძახილის ნიშანი და კითხვის ნიშანი).
# დაბეჭდოს ყველა სიტყვა, რომელიც ბოლო ასო "a"-თი მთავრდება.
# ასევე დაბეჭდოს ერთიდაიგივე სიტყვების რაოდენობა.

def task4():
    ran3 = input("enter sentence:")

    res = ""

    random5 = ran3.split(" ")
    random6 = set(random5)

    list1 = []

    for i in ran3:
        if i.isalpha():
            res += i

    for i in random5:
        a = i.lower()
        if a.endswith("a"):
            list1.append(i)



    list2 = []

    for i in random6:
        if random5.count(i) >= 2:
            list2.append(f"{i} is in the sentence {random5.count(i)} times")
    ran3 = input("enter sentence:")

    res = ""

    random5 = ran3.split(" ")
    random6 = set(random5)

    list1 = []

    for i in ran3:
        if i.isalpha():
            res += i

    for i in random5:
        a = i.lower()
        if a.endswith("a"):
            list1.append(i)



    list2 = []

    for i in random6:
        if random5.count(i) >= 2:
            list2.append(f"{i} is in the sentence {random5.count(i)} times")
            ran3 = input("enter sentence:")

    res = ""

    random5 = ran3.split(" ")
    random6 = set(random5)

    list1 = []

    for i in ran3:
        if i.isalpha():
            res += i

    for i in random5:
        a = i.lower()
        if a.endswith("a"):
            list1.append(i)



    list2 = []

    for i in random6:
        if random5.count(i) >= 2:
            list2.append(f"{i} is in the sentence {random5.count(i)} times")

task4()