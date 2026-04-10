from pypdf import PdfReader

abs_path = "C:/users/desktop/"
supply_file = "First Grade School Supply List.pdf"

reader = PdfReader(f"C:/users/cj/desktop/{supply_file}")
# fields = reader.get_fields()
# for fn, field in fields.items():
#     print(f"{fn}: {field}")

str = reader.pages[0].extract_text()

lines = []
temp = ""
    
for l in str:
    
    if l == "\n":
        lines.append(temp.replace("\n",""))
        temp = ""

    temp += l

print(f"There are {len(lines)} lines.")
for x in lines:
    if x[0].isdigit():
       
       x = x.replace(f"{x[0]} ",f"{x[0]} x ")
       print(f"{x}")
