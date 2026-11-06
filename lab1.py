
import statistics

# Get input from the user
data = list(map(float, input("Enter numbers separated by spaces: ").split()))

# Check whether the dataset contains enough values
if len(data) == 0:
    print("Error: Please enter at least one number.")

elif len(data) == 1:
    print("Mean:", statistics.mean(data))
    print("Median:", statistics.median(data))
    print("Mode:", statistics.multimode(data))
    print("Variance: Not defined for a single value (sample variance).")

else:
    # Calculate statistical measures
    mean_value = statistics.mean(data)
    median_value = statistics.median(data)
    mode_value = statistics.multimode(data)
    variance_value = statistics.variance(data)

    # Display results
    print("\nStatistical Measures")
    print("--------------------")
    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Mode:", mode_value)
    print("Variance:", variance_value)
