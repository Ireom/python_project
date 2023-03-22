#!/usr/bin/env python
# coding: utf-8

# In[5]:


length_in_cm = float(input("Enter a length in centimeters: "))
if length_in_cm < 0:
    print("Invalid entry. Length must be positive.")
else:
    length_in_inches = length_in_cm / 2.54
    print(f"{length_in_cm} centimeters is equal to {length_in_inches:.2f} inches.")


# In[ ]:


temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (Celsius or Fahrenheit): ")

if unit.lower() == "celsius":
    fahrenheit = (temperature * 9/5) + 32
    print(f"The temperature is {fahrenheit:.1f} degrees Fahrenheit.")
elif unit.lower() == "fahrenheit":
    celsius = (temperature - 32) * 5/9
    print(f"The temperature is {celsius:.1f} degrees Celsius.")
else:
    print("Invalid unit entered. Please enter either Celsius or Fahrenheit.")


# In[2]:


temperature = float(input("Enter a temperature in Celsius: "))

if temperature < -273.15:
    print("The temperature is invalid because it is below absolute zero.")
elif temperature == -273.15:
    print("The temperature is absolute 0.")
elif temperature < 0:
    print("The temperature is below freezing.")
elif temperature == 0:
    print("The temperature is at the freezing point.")
elif temperature <= 100:
    print("The temperature is in the normal range.")
elif temperature == 100:
    print("The temperature is at the boiling point.")
else:
    print("The temperature is above the boiling point.")


# In[3]:


credits = int(input("Enter the number of credits you have taken: "))

if credits <= 23:
    print("You are a freshman")
elif 24 <= credits <= 53:
    print("You are a sophomore")
elif 54 <= credits <= 83:
    print("You are a junior")
else:
    print("You are a senior")


# In[9]:


num = int(input("Enter a number: "))
divisors_sum = 0

for i in range(1, num+1):
    if num % i == 0:
        divisors_sum += i

print("The sum of the divisors of", num, "is", divisors_sum)


# In[10]:


def is_perfect(num):
    divisors = [1]
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    return False

perfect_nums = []
for i in range(2, 10000):
    if is_perfect(i):
        perfect_nums.append(i)
        
print(perfect_nums)


# In[12]:


num = int(input("Enter an integer: "))

# Check if the number is divisible by any perfect squares
for i in range(2, int(num ** 0.5) + 1):
    if num % (i*i) == 0:
        print(num, "is not squarefree")
        break
else:
    print(num, "is squarefree")


# In[14]:


# take input for x, y and z
x = input("Enter value for x: ")
y = input("Enter value for y: ")
z = input("Enter value for z: ")

# print the original values
print("Original values: x =", x, ", y =", y, ", z =", z)

# swap the values
temp = x
x = y
y = z
z = temp

# print the swapped values
print("Swapped values: x =", x, ", y =", y, ", z =", z)


# In[ ]:


scores = []
for i in range(10):
    score = float(input("Enter test score: "))
    if score > 100:
        print("Warning: A score over 100 has been entered.")
    scores.append(score)

# (a) highest and lowest scores
print("Highest score:", max(scores))
print("Lowest score:", min(scores))

# (b) average of scores
average = sum(scores) / len(scores)
print("Average score:", average)

# (c) second largest score
sorted_scores = sorted(scores, reverse=True)
second_largest = sorted_scores[1]
print("Second largest score:", second_largest)

# (e) average of remaining scores after dropping lowest 2
sorted_scores = sorted(scores)
dropped_scores = sorted_scores[2:]
average_dropped = sum(dropped_scores) / len(dropped_scores)
print("Average score after dropping lowest 2:", average_dropped)


# In[15]:


def is_perfect_power(n, power):
    root = int(n ** (1 / power))
    return root ** power == n

count = 0
for i in range(1, 1001):
    if not is_perfect_power(i, 2) and not is_perfect_power(i, 3) and not is_perfect_power(i, 5):
        count += 1

print("The number of integers from 1 to 1000 that are not perfect squares, perfect cubes, or perfect fifth powers is:", count)


# In[16]:


import random

for i in range(50):
    rand_int = random.randint(3, 6)
    print(rand_int)


# In[17]:


import random

# Generate random numbers
x = random.randint(1, 50)
y = random.randint(2, 5)

# Compute x^y
result = x ** y

# Print the result
print(f"{x}^{y} = {result}")


# In[18]:


import random

name = "Anita"
num = random.randint(1, 10)

for i in range(num):
    print(name)


# In[19]:


import random

# Generate a random decimal number between 1 and 10 with two decimal places of accuracy
num = round(random.uniform(1.00, 10.00), 2)

print(num)


# In[20]:


import random

numbers = []
for i in range(1, 52):
    num = random.uniform(1, i+1)
    numbers.append(num)

print(numbers)


# In[ ]:


# Ask the user to enter two numbers
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

# Compute k-x
k = 10   # you can change the value of k to whatever value you want
result = k - x

print("k - x = ", result)


# In[ ]:


#Enter an angle between -180° and 180°
angle = int(input("Enter an angle between -180° and 180°: "))

# Convert the angle to its equivalent between 0° and 360°
equivalent_angle = (angle % 360 + 360) % 360

print(f"The equivalent angle between 0° and 360° is: {equivalent_angle}°")


# In[ ]:


# Ask for the number of hours in the future
start_hour = int(input("Enter hour (between 1 and 12): "))
hours_ahead = int(input("How many hours ahead? "))

new_hour = (start_hour + hours_ahead) % 12
if new_hour == 0:
    print("New hour: 12 o'clock")
else:
    print("New hour:", new_hour, "o'clock")


# In[ ]:


##10(a)find out the last digit of a number is to mod the number by 10

power = int(input("Enter a power: "))
result = 2**power % 10
print("The last digit of 2^{} is {}".format(power, result))


# In[ ]:


##10(b)find out the last two digits of a number is to mod the number by 100

power = int(input("Enter a power: "))
result = 2**power % 100
print("The last two digits of 2^{} are {}".format(power, result))


# In[ ]:


##10(c)Write a program that asks the user to enter a power and how many digits they want

power = int(input("Enter a power: "))
n = int(input("Enter the number of digits you want: "))
result = str(2**power)[-n:]
print("The last {} digits of 2^{} are {}".format(n, power, result))


# In[ ]:


# Get weight in kilograms 
weight_kg = float(input("Enter weight in kilograms: "))

# Convert kilograms to pounds
weight_lb = weight_kg * 2.20462

# Round weight in pounds to nearest tenth
weight_lb_rounded = round(weight_lb, 1)

# Print result
print(f"{weight_kg} kilograms is approximately {weight_lb_rounded} pounds")


# In[ ]:


#input a number 
num = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1

# Calculate factorial
for i in range(1, num+1):
    factorial *= i

# Print result
print(f"The factorial of {num} is {factorial}")


# In[ ]:


import math

# input a number
num = float(input("Enter a number: "))
# Calculate sine, cosine, and tangent
sin_num = math.sin(num)
cos_num = math.cos(num)
tan_num = math.tan(num)
print(f"The sine of {num} is {sin_num:.2f}")
print(f"The cosine of {num} is {cos_num:.2f}")
print(f"The tangent of {num} is {tan_num:.2f}")


# In[ ]:


import math

angle_degrees = float(input("Enter an angle in degrees: "))
angle_radians = math.radians(angle_degrees)
sin_angle = math.sin(angle_radians)
print(f"The sine of {angle_degrees} degrees is {sin_angle:.2f}")


# In[ ]:




