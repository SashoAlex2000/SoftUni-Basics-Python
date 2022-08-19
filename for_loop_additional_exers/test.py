sbor = 0

for i in range(100):
    cic = input()
    if cic == "end":
        print("CICI")
        break
    else:
        cic = int(cic)
        sbor += cic

print(sbor)
