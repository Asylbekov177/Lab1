from time import sleep
import math

number = int(input())

milliseconds = int(input())

sleep(milliseconds/1000)

print("Square root of {n} after {m} miliseconds is {sq}".format(n=number, m= milliseconds, sq = math.sqrt(number)))