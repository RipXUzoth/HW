import calendar

def display_months():
    print("List of all months:")
    for month in range(1, 13):
        print(calendar.month_name[month])

# Run the function
display_months()
