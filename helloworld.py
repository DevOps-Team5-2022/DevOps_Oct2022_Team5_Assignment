def helloworld(input):
    #check if input is empty
    if not input.strip():
        print("Input string is empty!");
        return "Input string is empty!"

    #check if input is longer than 10 char
    elif len(input) > 10:
        print("Input string too long!");
        return "Input string too long!"
    
    else:
        print("Hello " + input + "! Welcome to Hello World File!");
        return "Hello " + input + "! Welcome to Hello World File!"
