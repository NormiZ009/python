def sort_three_integers(a, b, c):
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    middle = (a + b + c) - minimum - maximum
    print(minimum, middle, maximum)

# Example usage:
a = int(input("enter no: "))
b = int(input("enter no: "))
c = int(input("enter no: "))
sort_three_integers(a,b,c)