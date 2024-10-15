def conway(tableau):
    temp = tableau[0]
    result = []
    occurence = 0
    for i in range(len(tableau)):
        if tableau[i] == temp:
            occurence += 1
        else:
            result.append(occurence)
            result.append(temp)
            occurence = 1
            temp = tableau[i]
    result.append(occurence)
    result.append(temp)
    return result

def tableauToChar(tableau):
    result = ''
    for element in tableau:
        result += str(element)
    return result


run = True
nb = int(input('Nb de ligne : '))
tableau = [1]

print(str(tableau[0]))
while nb != 0:
    tableau = conway(tableau)
    print(tableauToChar(tableau))
    nb -= 1


