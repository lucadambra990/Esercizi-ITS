PATH:str = "Lezione_15/example.txt"
mode:str = "a" #r for read --- w for write ---- a for append ----- r+ for write and read
encoding:str = "utf-8"


# for p in ["Lezione_1/example.txt","Lezione_15/example.txt"]:
#     try:
#         file = open(p, mode, encoding=encoding)
#         output:str=file.read()
#         print(output)

#     except Exception as e: 
#         print(f"An error occured: {e}")
#     finally:
#         file.close()

file = open(PATH,mode=mode,encoding=encoding)
print(file)
input_text:str = input("Enter text to write to the file: ")
output:str=file.write(input_text)
print(output)
file.close()