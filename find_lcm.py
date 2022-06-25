numbers = []

i = int(input("How many numbers ? "))

for i in range(1, i+1):
    a = int(input("Enter no. "+repr(i)+" :"))
    numbers.append(a)

h = numbers[0] # Assuming first element as highest number

for i in numbers:
    if (i > h):
        h = i # Replacing highest number with actual highest number
        
def lcm(h, numbers):
    l = h 
    for i in numbers:
        while l%i != 0:
            l = l+h
    
    return l

print("--- Your Result ---")
print(lcm(lcm(h, numbers), numbers))
