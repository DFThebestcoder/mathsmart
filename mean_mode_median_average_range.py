import statistics

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(x) for x in numbers]

print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Mode:", statistics.mode(numbers))
print("Range:", max(numbers) - min(numbers))