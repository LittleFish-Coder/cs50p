def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")

def main():
    original = input("")
    emoji = convert(original)
    print(emoji)

main()
