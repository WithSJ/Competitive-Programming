def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM":
        if int(s[:2]) < 12:
            return s[:2]+s[2:-2]
        else:
            return "00"+s[2:-2]
    elif s[-2:] == "PM":
        if int(s[:2]) < 12:
            return str(int(s[:2])+12)+s[2:-2]
        else:
            return str(int(s[:2])+0)+s[2:-2]


if __name__ == '__main__':
    s = "07:05:45PM"
    result = timeConversion(s)

    print(result)
