def strformat(n: int):
    align = len(bin(n)[2:])
    for i in range(1,n + 1,1):
        #print(f"{str(i):>{align}} {oct(i)[2:]:>{align}} {hex(i)[2:].upper():>{align}} {bin(i)[2:]:>{align}}")
        #print(str(i).rjust(align,' '),oct(i)[2:].rjust(align,' '),hex(i)[2:].upper().rjust(align,' '),bin(i)[2:].rjust(align,' '))
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = align))
def main():
    strformat(17)
if __name__=="__main__":
    main()