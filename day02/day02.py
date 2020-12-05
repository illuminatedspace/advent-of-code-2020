def validatePasswords(passworddata):
    validpasswordcount = 0
    for line in passworddata.splitlines():
        policy, policyletter, password = line.split(" ")
        print(policy, policyletter, password)
        
        index1, index2 = policy.split('-')
        letter1 = password[int(index1)-1]
        letter2 = password[int(index2)-1]
        print(letter1, letter2, policyletter)
        if letter1 == policyletter[0] and letter2 == policyletter[0]:
            continue
        if letter1 == policyletter[0] or letter2 == policyletter[0]:
            validpasswordcount += 1

    return validpasswordcount


with open("./day02input.txt", 'r') as passwordfile:

    passworddata = passwordfile.read()
    
    solution = validatePasswords(passworddata)
    print(solution)

