# list is  collection of  data of data type

marks=[12,32,54,54,"pradumn"];
print(marks);
print(marks[1]);
print(marks[-1]);
print(marks[-2]);
print(marks[0:3]);
 
print("**********") 
for mark in marks:
    print(mark);

marks.append(100);
print(marks);

marks.insert(1,101);
print(marks);
print(100 in marks);
print(99 in marks);
print(len(marks));

# to make list empty
marks.clear();
print( marks);