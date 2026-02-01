# ფაილი: task3.py


# ამოცანა:
# მომხმარებელს შემოატანინეთ რამდენიმე სიტყვა 
# პროგრამამ უნდა:
# დაბეჭდოს მხოლოდ მხოლოდ ის სიტყვები, რომელთა თითოეული ასო უნიკალურია თვითონ სიტყვაში
# თითოეულ სიტყვას დაბეჭდოს ახალ ხაზზე.
 
def task3():
    list = []
    word = input("Enter a words:")
    final = ""

    for i in word:
        if i not in list:
            final += i
            list.append(i)

        if final == word:
            print(final)


task3() 