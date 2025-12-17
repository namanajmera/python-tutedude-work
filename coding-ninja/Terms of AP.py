# Problem statement
# Write a program to print the first x terms of the mathematical series 3N + 2 which are not multiples of 4.
#
# The series is defined as:
#
# T(N) = 3N + 2, where N is a positive integer starting from 1. Your task is to print the first x terms of this series, but you should exclude any term that is a multiple of 4.

x=int(input())
n=1
count=0
while count<x:
    term=(3*n)+2
    if term % 4!=0:
        print(term,end=' ')
        count=count+1
    n=n+1