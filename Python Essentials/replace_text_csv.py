import csv

# Összerendelés beolvasása egy 3 oszlopos mátrixba

csv_filename = 'D:\\osszerendeles.csv'

with open(csv_filename) as f:
    reader = csv.reader(f)
    lst = list(reader)

matrix = []
for row in lst:
    matrix.append(row[0].split(';'))

f.close()
print(len(matrix), "sor beolvasva")
input("Press Enter to continue...")

# input csv file beolvasása

textfile = open("D:\\Ultimate_esemenyek.csv", "r", encoding='utf-8')

text = ''.join([i for i in textfile])
textfile.close()

# szöveges cserék elvégzése

counter = 1
for m_row in matrix:
    text = text.replace(m_row[1], m_row[0])
    text = text.replace(m_row[2], m_row[0])
    print(counter, "rekord kész.")
    counter += 1

# # az eredmény kiírása csv file-ba

x = open("D:\\Ultimate_esemenyek_anonym.csv", "w", encoding='utf-8')
x.writelines(text)
x.close()
