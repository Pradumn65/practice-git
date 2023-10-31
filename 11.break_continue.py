subject=["math","science","physics","history","computer science","physical education"];

for sub in subject:
    if sub ==  "history":
        break;
    print(sub);

print("*******");

for sub in subject:
    if sub ==  "history":
        continue;
    print(sub);