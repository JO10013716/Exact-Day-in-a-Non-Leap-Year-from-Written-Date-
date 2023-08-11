##This tool will tell you the exact day of the year the date that you enter is.

mdi = {
    "January": 1,
    "February": 32,
    "March": 60,
    "April": 91,
    "May": 121,
    "June": 152,
    "July": 182,
    "August": 213,
    "September": 244,
    "October": 274,
    "November": 305,
    "December": 335,
}

dat = input("Please enter a month and a day (e.g. 'January 1'): ")
datl = dat.split()
numberstr = str(datl[1])
number = int(datl[1])

if datl[0] == 'January' and number > 31:
    print("Error: There are only 31 days in January.")
elif datl[0] == 'February' and number > 28:
    print("Error: There are only 28 days in February.")
elif datl[0] == 'March' and number > 31:
    print("Error: There are only 31 days in March.")
elif datl[0] == 'April' and number > 30:
    print("Error: There are only 30 days in April.")
elif datl[0] == 'May' and number > 31:
    print("Error: There are only 31 days in May.")
elif datl[0] == 'June' and number > 30:
    print("Error: There are only 30 days in June.")
elif datl[0] == 'July' and number > 31:
    print("Error: There are only 31 days in July.")
elif datl[0] == 'August' and number > 31:
    print("Error: There are only 31 days in August.")
elif datl[0] == 'September' and number > 30:
    print("Error: There are only 30 days in September.")
elif datl[0] == 'October' and number > 31:
    print("Error: There are only 31 days in October.")
elif datl[0] == 'November' and number > 30:
    print("Error: There are only 30 days in November.")
elif datl[0] == 'December' and number > 31:
    print("Error: There are only 31 days in December.")
else:
    value = mdi[datl[0]] + number - 1
    valuestr = str(value)
    if '1' == valuestr[-1]:
        print(f'{dat} is the {value}st day of the year.')
    elif '2' == valuestr[-1]:
        print(f'{dat} is the {value}nd day of the year.')
    elif '3' == valuestr[-1]:
        print(f'{dat} is the {value}rd day of the year.')
    else:
        print(f'{dat} is the {value}th day of the year.')