# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    word = 'Hello'
    print(word.lower())
    print(word.upper())
    print('1'+'2')
    print('Hi'+'there')

    #Replication
    print('12'*2)
    print('1'*2 + '2'*3)

    #Strip
    #Split
    #Slicing

    #List
    lts = [11,22,33]
    lts2 =[3,5,6]
    lts[1] = 95
    lts.append(44)
    lts.pop(2)
    lts.append(33)
    lts.remove(33)
    lts.append(lts2)

    for x, y in zip(lts,lts2):
        print(x,", ",y)


    ##Tuples
    tuple1 = ('Honda', 'Civic', 4, 2017)
    tuple1[1]

    #Objetc inmutable

    #Dictionaries
    dict = {('Ghostbusters', 2016): 5.4,
            ('Ghostbusters', 1984): 7.8}

    print(dict[('Ghostbusters',2016)])

    ##Adding to dict
    dict[('Cars', 2006)] = 7.1

    #Deleting
    dict.pop(('Ghostbusters', 2016))

    #List comprehension
    list1 = [i ** 2 for i in range(1, 11)]
    list2 = [i for i in range(0, 20, 2)]
    # Dict comprehension
    dictC = {i: chr(i) for i in range(65, 90)}


    #Sets
    leos_colors = set(['blue', 'green', 'red'])
    ilkays_colors = set(['blue', 'yellow'])
    either = ilkays_colors.union(leos_colors)
    both = ilkays_colors.intersection(leos_colors)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
