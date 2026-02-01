# ფაილი: task3.py


# ამოცანა:
# მომხმარებელს შემოატანინეთ რამდენიმე სიტყვა 
# პროგრამამ უნდა:
# დაბეჭდოს მხოლოდ მხოლოდ ის სიტყვები, რომელთა თითოეული ასო უნიკალურია თვითონ სიტყვაში
# თითოეულ სიტყვას დაბეჭდოს ახალ ხაზზე.
 
def task3():
    list2 = []
    word = input("Enter a words:")
    list1 = word.split()
    final = ""

    for i in list1:
        for j in i:
            
            if j not in final:
                final += j

        if final == i:
            list2.append(i)
            final = ""

    for i in list2:
        print(i)
                


    


task3() 