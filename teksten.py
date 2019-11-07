inputFileText = open("C:/Users/Dick Stada/Downloads/OpenTaal-210G-woordenlijsten/OpenTaal-210G-basis-gekeurd.txt", "r").read()
# print (inputFileText)   # de hele inhoud printen

# for line in open("C:/Users/Dick Stada/Downloads/OpenTaal-210G-woordenlijsten/OpenTaal-210G-basis-gekeurd.txt", "r").readlines():
# for line in open("C:/Users/Dick Stada/Downloads/OpenTaal-210G-woordenlijsten/OpenTaal-210G-basis-ongekeurd.txt", "r").readlines():
# for line in open("C:/Users/Dick Stada/Downloads/OpenTaal-210G-woordenlijsten/OpenTaal-210G-verwarrend.txt", "r").readlines():
for line in open("C:/Users/Dick Stada/Downloads/OpenTaal-210G-woordenlijsten/OpenTaal-210G-flexievormen.txt", "r").readlines():
#     print(line.strip())
#     print(len(line))

    if len(line) == 9:
        # print(line)
        line_new = line[0] + line[3] + line[6] + line[1] + line[4] + line[7] + line[2] + line[5] + line[8]
        if line.strip() == line_new:
            print(line)
        if line_new in inputFileText:
            print(line, line_new)

    # if len(line) == 16:
    #     # print(line)
    #     line_new = line[0] + line[4] + line[8] + line[12] + line[1] + line[5] + line[9] + line[13] + line[2] + line[6] + line[10] + line[14] + line[2] + line[3] + line[7] + line[11]
    #     if line.strip() == line_new:
    #         print(line)

