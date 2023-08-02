from statistics import mean, median, mode, variance

weekdays = {
    "Monday": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "Tuesday": ["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],
    "Wednesday": ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],
    "Thursday": ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],
    "Friday": ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]
}

color_counts = {}
totalcounts = []
for weekday, colors in weekdays.items():
    for color in colors:
        color_counts[color] = color_counts.get(color, 0) + 1

for color, count in color_counts.items():
    totalcounts.append(count)
    print(f"{color}: {count}")

mean_value = round(mean(totalcounts))

# Median
median_value = median(totalcounts)

# Mode
mode_value = mode(totalcounts)

# Variance
variance_value = variance(totalcounts)

print(f"\nMean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Variance: {variance_value}")


