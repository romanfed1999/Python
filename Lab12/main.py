import re


if __name__ == "__main__":
    logs304 = open("logs304", "r+")
    with open("access_log") as file:
        for line in file:
            if re.search('\\b304\\b', str(line)):
                logs304.write(line)


print("Done")
