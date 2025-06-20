# multithreding and demonstrate

import threading
import time
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)
        
def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(1)
        
# Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
# Starting threads
t1.start()
t2.start()
# Wait for threads to finish
t1.join()
t2.join()
print("Both threads finished.")