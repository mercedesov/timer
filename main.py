from timer import countdown_timer

def main():
    user_input = input("Insert time to count down (h:m:s) ")
    try:
        hours, minutes, seconds = map(int, user_input.split(':'))
        total_seconds = hours * 3600 + minutes * 60 + seconds
        countdown_timer(total_seconds)
    except ValueError:
        print("Invalid input format. Please use the format h:m:s")

if __name__ == "__main__":
    main()
