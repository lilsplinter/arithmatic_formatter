def arithmetic_arranger(problems ,true=False):
    try:
        if len(problems) > 6:
            return 19 / 0
    except:
        return "Error: Too many problems."
    try:
        for i in problems:
            li = i.split()
            if li[1] not in "+-":
                int("hello")
    except:
                return "Error: Operator must be '+' or '-'."
    try:
        for i in problems:
            li = i.split()
            int(li[0])
            int(li[2])
    except:
        return "Error: Numbers must only contain digits."
    try:
        for i in problems:
            li = i.split()
            if len(li[0]) > 4 or len(li[2]) > 4:
                return 4 / 0
    except:
        return "Error: Numbers cannot be more than four digits."
    else:
        every_operator = []
        first = []
        second = []
        third = []
        forth = []
        for problem in problems:
                every_operator.append(problem.split())
        for li in every_operator:
                space = max(len(li[0]), len(li[2])) - min(len(li[0]), len(li[2]))
                if len(li[0]) != len(li[2]):
                        if len(li[0]) > len(li[2]):
                                li[2] = f"{space * ' '}{li[2]}"
                        else:
                                li[0] = f"{space * ' '}{li[0]}"
        for i in every_operator:
                first.append(f"  {i[0]}")
                second.append(f"{i[1]} {i[2]}")
        for i in first:
                
                third.append(len(i) * "-")
        if true:
                x = 0
                for i in problems:
                        space = len(third[x]) - len(str(eval(i)))
                        forth.append(f"{space * ' '}{str(eval(i))}")
                        x += 1
        firstline = "    ".join(first)
        secondline = "    ".join(second)
        thirdline = "    ".join(third)
        forthline = "    ".join(forth)
        arranged_problems = f"{firstline}\n{secondline}\n{thirdline}\n{forthline}"
        return arranged_problems
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
