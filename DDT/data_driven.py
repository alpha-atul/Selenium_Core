import pandas as PD
from selenium import webdriver

#Write data into an excel
write_path = "C:/Users/atul.singh/Desktop/writer.xlsx"
data = PD.DataFrame({"Atul"})
writer = PD.ExcelWriter(write_path)
data.to_excel(writer,"Sheet1")
writer.save()

#Read data from an excel
read_path = "C:/Users/atul.singh/Desktop/Product_Versioning.xlsx"
rows = data.shape[0]
cols = data.shape[1]
#column = data[["Scenarios","Version 2"]]
print("Rows: ",rows)
print("Cols: ",cols)

#row = data.head(4)
#print(row)

sorted_table = data.sort_values("Scenarios", ascending = True)
print(sorted_table)

for i in range(10):
    print(data.iloc[i])
print(data.iloc[2,2])
for i in range(0,rows):
    for j in range(0,cols):
        value = data.iloc[i,j]
        print(value, end=" ")
    print(" ")
