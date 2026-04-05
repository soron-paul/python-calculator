#calculator.2

def calculator():
    val=[]
    answer=0
    op="+"

#input

    while True:
        a=input()
        if a=="=":
            break
        else:
            val.append(a)

#calculation

    for i in val:
        if i not in ["+","*","-","/"]:
            num=float(i)
            if op=="+":
                answer+=num
            elif op=="-":
                answer-=num

            elif op=="*":
                answer*=num

            elif op=="/":
                answer/=num

        else:
            op=i

    print("answer:",answer)





calculator()










