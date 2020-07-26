import re


def main():
    string = 'References (71)'

    s = re.search(r"(\d+)", string)
    if s:
        print(s.group(0))


if __name__ == "__main__":
    main()