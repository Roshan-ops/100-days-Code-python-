row1=["a", "b", "c"]
row2 =["d", "e", "f"]
row3 = ["g" "h", "i"]

map= [row1, row2, row3]
print(f"{row1}\n {row2}\n{row3}")

position = input("Where do you want to put the treasure ? ")
horizonal = position[0]
vertical = position[1]

selected_row = (map[vertical -1])
selected_row [horizonal -1] = "X"