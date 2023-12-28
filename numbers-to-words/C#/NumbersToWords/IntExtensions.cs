namespace NumbersToWords;

public static class IntExtensions
{
    private static readonly string[] Units = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    private static readonly string[] Teens = { "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" };
    private static readonly string[] Tens = { "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" };

    public static string ToWords(this int number)
    {
        if (number < 0 || number > 9999)
        {
            throw new ArgumentOutOfRangeException(nameof(number), "Number out of range (0-9999)");
        }

        if (number < 100)
        {
            return TwoDigitNumberToWords(number);
        }
        else if (number < 1000)
        {
            return Units[number / 100] + " hundred" + (number % 100 != 0 ? " " + TwoDigitNumberToWords(number % 100) : "");
        }
        else
        {
            return TwoDigitNumberToWords(number / 1000) + " thousand" + (number % 1000 != 0 ? " " + ToWords(number % 1000) : "");
        }
    }

    private static string TwoDigitNumberToWords(int number)
    {
        if (number < 10)
        {
            return Units[number];
        }
        else if (number < 20)
        {
            return Teens[number - 10];
        }
        else
        {
            return Tens[number / 10] + (number % 10 != 0 ? "-" + Units[number % 10] : "");
        }
    }
}

