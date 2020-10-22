options = open("option_select_picker.html", "w")
data = open("allData.txt", "w")
f = open("C:/Users/Max/Downloads/data_non_accumulative.csv", "r")
content = f.read()
lines = content.split("\n")
for i, line in enumerate(lines):
    columns = line.split(",")
    for j, col in enumerate(columns):
        if j == 0:
            options.write("<option data-tokens=" + col + ">" + col + "</option>")
            options.write("\n")
        else:
            if j == 1:
                data.write("[")
            data.write(col)
            if j < len(columns) - 1:
                data.write(",")
            if j == len(columns) - 1:
                data.write("],")
    data.write("\n")

options.close()
data.close()
