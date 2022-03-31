def fizz_buzz(begin, end):
    result = []
    for number in range(begin, end+1):
        if not number % 3 and not number % 5:
            result.append("FizzBuzz")
        elif not number % 3:
            result.append("Fizz")
        elif not number % 5:
            result.append("Buzz")
        else:
            result.append(str(number))
    return " ".join(result)
