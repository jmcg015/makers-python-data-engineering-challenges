def fizzbuzz(num):
    output = []
    for i in range(1, num + 1):
        fizz = i % 3 == 0
        buzz = i % 5 == 0
        if fizz and buzz:
            output.append("FizzBuzz")
        elif fizz:
            output.append("Fizz")
        elif buzz:
            output.append("Buzz")
        else:
            output.append(str(i))
    return ", ".join(output)