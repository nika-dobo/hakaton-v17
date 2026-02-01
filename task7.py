# ფაილი: task7.py
# შესაფასებელი ქულა: 0-3
# ამოცანა:
# მომხმარებელს შემოატანინეთ რიცხვი შემდეგ 
# თქვენი დავალებაა:

# რამდენი რიცხვი არის ლუწი და კენტი შემოყვანილ რიცხვამდე
# შემდგომ ტერმინალში გამოიტანეთ რამდენი კენტი და რამდენი ლუწი რიცხვი იქნება 

def task7():
    limit = int(input("შეიყვანეთ რიცხვი: "))

    even_count = 0
    odd_count = 0  

    for i in range(1, limit):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"even: {even_count}")
    print(f"odd: {odd_count}")

task7()




