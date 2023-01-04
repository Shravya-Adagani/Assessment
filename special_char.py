def splitString(str):
    alpha = ""
    num = ""
    special = ""
    for i in range(len(str)):
        if (str[i].isdigit()):
            num = num + str[i]
        elif ((str[i] >= 'A' and str[i] <= 'Z') or
              (str[i] >= 'a' and str[i] <= 'z')):
            alpha += str[i]
        else:
            special += str[i]

    print(alpha)
    print(num)
    print(special)


if __name__ == "__main__":
    str = "zaheer.shaik@fissionlabs.com"
    splitString(str)