def findExpenseAnomoly():
    with open("./day01input.txt", 'r') as expensefile:
        # print("expensefile", expensefile)
        
        expensedata = expensefile.read()
        # print("expensedata", expensedata)

        expenselist = [int(string.strip()) for string in expensedata.splitlines()]
        # expenselist = []
        # for item in expensedata.splitlines():
        #     formatteditem = int(item.strip())
        #     expenselist.append(formatteditem)
        # print("expenselist", expenselist)

        for index1 in range(len(expenselist)):
            for index2 in range(index1 + 1, len(expenselist)):
                for index3 in range(index2 + 1, len(expenselist)):
                    expense1 = expenselist[index1]
                    expense2 = expenselist[index2]
                    expense3 = expenselist[index3]

                    if expense1 + expense2 + expense3 == 2020:
                        return expense1 * expense2 * expense3

solution = findExpenseAnomoly()
print("solution", solution)
