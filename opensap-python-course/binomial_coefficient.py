"""
Exercise: Calculating the binomial coefficient
The binomial coefficient can be used to calculate how many number of ways  𝑘  objects can be chosen from a set of  𝑛  objects. 
This is for example the case when playing the lottery. Using the binomial coefficient it is possible to calculate 
the possible combination for the German lottery. Here 6 numbers are drawn from the numbers 1 to 49.

The number of possible combinations is given by the formula:  49! / (6!(49−6)!) 
The general formula for calculating the binomial coefficient is:  𝑛! / (𝑘!(𝑛−𝑘)!) 

Write a function binomial, that takes the numbers 'n' and 'k' as a parameter and calculates the binomial coefficient as a result. 
Reuse your factorial function from the unit 3 of the current week. Alternatively use the example given below as a starting point.
"""

def factorial(n):
    result = 1

    if n > 1:
        for i in range(2, n + 1):
            result *= i

    return result

def binomial(k, n):
    return factorial(n) / (factorial(k) * (factorial(n - k)))

print("The general formula for calculating the binomial coefficient is:  𝑛! / (𝑘!(𝑛−𝑘)!) ")
num_n = int(input("Please enter n: "))
num_k = int(input("Please enter k: "))

print(int(binomial(num_n, num_k)))

print(
    f"The possible number of combinations to draw 6 numbers from 49 numbers is {int(binomial(6, 49))}."
)
# The possible number of combinations to draw 6 numbers from 49 numbers is 13983816.