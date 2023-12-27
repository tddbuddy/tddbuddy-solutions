def number_to_words(number):
    if not 0 <= number <= 9999:
        raise ValueError("Number out of range (0-9999)")

    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def two_digit_number_to_words(n):
        if n < 10:
            return units[n]
        elif 10 <= n < 20:
            return teens[n-10]
        else:
            return tens[n//10] + ("-" + units[n%10] if n%10 != 0 else "")

    if number < 100:
        return two_digit_number_to_words(number)
    elif number < 1000:
        return units[number // 100] + " hundred" + (" " + two_digit_number_to_words(number % 100) if number % 100 != 0 else "")
    else:
        return two_digit_number_to_words(number // 1000) + " thousand" + (" " + number_to_words(number % 1000) if number % 1000 != 0 else "")

