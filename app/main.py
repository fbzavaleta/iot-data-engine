import numpy as np
import time


def main():
 cicle = 0
 max_cicle = 100
 while(True):
    random_number = np.random.rand()
    cicle += 1
    print(f"this is the cicle {cicle} with randon number: {random_number}")
    if cicle > max_cicle:
         print("cicle value was stored")
    time.sleep(0.5)

if __name__ == "__main__":
   main()