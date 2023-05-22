while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except KeyboardInterrupt:
        print("Exiting...")
        break
    except:
        print("Sorry, something went wrong...")
