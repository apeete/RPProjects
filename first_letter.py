prompt = raw_input("Tell me your password:")

if prompt is "":
    prompt = raw_input("Come again?")
    print prompt[0].upper()
else:
    print prompt[0].upper()
