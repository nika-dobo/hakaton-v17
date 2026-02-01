# ფაილი: task5.py
# შესაფასებელი ქულა: 0-3
# ამოცანა:
# მომხმარებელს შემოაყვანინეთ პაროლი და გააკეთეთ მაგ პაროლის ვალიდაცია ანუ
# პროგრამამ უნდა:
# მოაცილოს სფეისები
# მოაცილოს დიდი ასოები 
# და არ უნდა იყოს პაროლი 8 ასოზე ნაკლები


def task5():
    password = input("შეიყვანეთ პაროლი: ")

    new_password = ""

    for i in password:
        if not i.isupper() and i != " ":
            new_password += i

    if len(new_password) >= 8:
        print("პაროლი მიღებულია")
        print("შედეგი:", new_password)
    else:
        print("8 სიმბოლოს არ უნდა აღმატებოდს")

task5()