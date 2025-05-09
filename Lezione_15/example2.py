# with open("example.txt", mode="w", encoding="utf-8") as file:

#     message:str="Hello,world!\n"
#     written_char:int = file.write(message)
#     print(f"Written characters are: {written_char}")

import time
class Stopwatch: # per capire come funziona with
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type,exc_value,traceback):
        self.end_time=time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time:.8f} seconds")

        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"An error occured: {exc_value}")
            print(f"Traceback: {traceback}")
        return False
    
pass
    
with Stopwatch():
    list_num:list[int]=[35,25,18,6,98,59]
    sorted_array = sorted(list_num)
    list_num[9]
    for i in sorted_array:
        if i%2==0:
            print("Pari")
        else:
            print("Dispari")
    print(f"Original array: {list_num}")
    print(f"Sorted array: {sorted_array}")