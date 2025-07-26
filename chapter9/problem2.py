

def table(n):
    with open("table.txt","w") as export:
     for i in range(1,12):
        export.write(f"{n} x {i} = {n*i}\n")

table(12)    