file_name = raw_input("Name of the file?\nShortcuts: 1 = 'table.txt', 0 = exit\n>> ")

if file_name == '1':
    file_name = "table.txt"
elif file_name == '0':
    exit()

try:
    F = open(file_name,'r')
except:
    print "Error! File " + file_name + " not found."
    exit()

VL = raw_input("Vertical lines? [Y-N].\n>> ")
if VL == "N":
    VL = 0;
else:
    VL = 1;

HL = raw_input("Horizontal lines? [Y-N].\n>> ")
if HL == "N":
    HL = 0;
else:
    HL = 1;
    
align = raw_input("Text align? [l-c-r].\n>> ")    
if align != "l":
    if align != "r":
        align = "c"
        
if VL == 1:
    align = "|" + align 

A = []

for f in F:
    B = []
    t = ""
    for i in f:
        if str.isspace(i) == False:
            t += i;
        else:
            if len(t) > 0:
                B.append(t)
                t = ""
    A.append(B)

new_file = "NEW" + file_name

F2 = open(new_file,'w')

Nr = len(A)
Nc = 0
for i in A:
    Nc = max(Nc,len(i))

F2.write("\\begin{table}[ht!]\n\\begin{center}\n\\begin{tabular}{")
for i in range(Nc):
    F2.write(align)
if VL == 1:
    F2.write("|}\n")
else:
    F2.write("}\n")
    
n = 1

if HL == 1:
    F2.write("\t\\hline\n")

for l in A:
    if n > 0:
        F2.write("\t")
    n = len(l)
    for i in range(n - 1):
        if l[i] != '%':
            F2.write(l[i] + " & ")
        else:
            F2.write(" & ")
    if n != 0: 
        if l[n - 1] != '%':
            F2.write(l[n - 1])
        while n < Nc:
            n += 1
            F2.write(" & ")
        F2.write("\\\\\n")
        if HL == 1:
            F2.write("\t\\hline\n")
    else:
        print "Warning! Blank line found. Line ignored."
        
F2.write("\\end{tabular}\n\\end{center}\n\\end{table}")

print "----------------------------------------"
print "File " + new_file + " created successfully."
print "----------------------------------------"

F.close()
F2.close()
