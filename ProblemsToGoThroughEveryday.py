#find out the leap year
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
## good year
year = int(input())
print(is_leap(year))
