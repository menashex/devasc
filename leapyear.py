def is_year_leap(year):
    if ((year%4==0) and (year%100!=0)) or (year%400==0): return True
    else: return False

def days_in_month(year, month):
    months=[0,31,28,31,30,31,30,31,31,30,31,30,31] #0 through 12, 13 values
    if(is_year_leap(year)): months[2]=29
    return months[month]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
