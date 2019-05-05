from string import ascii_lowercase, ascii_uppercase, digits

characters = ascii_lowercase + ascii_uppercase + digits
hex_mirror = ["0", "1", "2", "3", "4", "5", "6", "7",
              "8", "9", "A", "B", "C", "D", "E", "F"]

with open(file="./Files/word/document.xml", mode="r", encoding="utf-8") as f:
    doc = f.read()
    space = 0
    hex_code = ""
    for char in doc:
        if char == " ":
            space += 1
        elif char != characters and space > 0:
            hex_code += hex_mirror[space]
            space = 0
        else:
            pass

print(hex_code)