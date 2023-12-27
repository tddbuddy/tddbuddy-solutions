namespace LastSunday;

public class DateUtils
{
    public static List<DateTime> LastSunday(int year)
    {
        if (year < 1)
        {
            throw new ArgumentException("Year must be a positive integer.");
        }

        var lastSundays = new List<DateTime>();
        for (int month = 1; month <= 12; month++)
        {
            var lastDayOfMonth = new DateTime(year, month, DateTime.DaysInMonth(year, month));
            int daysToSubtract = (int)(lastDayOfMonth.DayOfWeek - DayOfWeek.Sunday + 7) % 7;
            lastSundays.Add(lastDayOfMonth.AddDays(-daysToSubtract));
        }
        return lastSundays;
    }
}

