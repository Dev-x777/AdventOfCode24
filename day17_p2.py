import sys

with open(sys.argv[1] if len(sys.argv) > 1 else './day_17.in') as f:
    reg, prog = f.read().split('\n\n')

prog = list(map(int, prog.split(': ')[1].split(',')))
rega, regb, regc = (int(line.split(': ')[1]) for line in reg.splitlines())

def get_combo(oper, rega, regb, regc):
    if 0 <= oper <= 3:
        return oper
    if oper == 4:
        return rega
    if oper == 5:
        return regb
    if oper == 6:
        return regc

def run(prog, rega, regb, regc):
    ip = 0
    out = []
    while ip < len(prog):
        oper = prog[ip+1]
        combo = get_combo(oper, rega, regb, regc)
        match prog[ip]:
            case 0:
                rega //= 2**combo
            case 1:
                regb ^= oper
            case 2:
                regb = combo%8
            case 3:
                if rega:
                    ip = oper
                    continue
            case 4:
                regb ^= regc
            case 5:
                out.append(combo%8)
            case 6:
                regb = rega//2**combo
            case 7:
                regc = rega//2**combo
        ip += 2
    return out

print(','.join(map(str, run(prog, rega, regb, regc))))

rega = 0
j = 1
istart = 0
while j <= len(prog) and j >= 0:
    rega <<= 3
    for i in range(istart, 8):
        if prog[-j:] == run(prog, rega+i, regb, regc):
            break
    else:
        j -= 1
        rega >>= 3
        istart = rega%8+1
        rega >>= 3
        continue
    j += 1
    rega += i
    istart = 0
print(rega)