import time

def create_list(n):
    result = []
    for i in range(n):
        result.insert(len(result), i)
    return result

# Measure the time taken by create_list function
n = 10  # You can change this value as needed
start_time = time.time()  # Start the timer
result = create_list(n)
end_time = time.time()  # End the timer

elapsed_time = end_time - start_time  # Calculate the elapsed time

# Print the result and the elapsed time
print(f"Result: {result}")
print(f"Time taken to create the list: {elapsed_time} seconds")

