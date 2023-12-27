namespace LastSunday.Tests;

public class DateUtilTests
{
    [Test]
    public void TestLastSundayInvalidYear()
    {
        Assert.Throws<ArgumentException>(() => DateUtils.LastSunday(-1));
    }

    [Test]
    public void TestLastSunday()
    {
        var expected2013 = new List<DateTime>
        {
            new DateTime(2013, 1, 27),
            new DateTime(2013, 2, 24),
            new DateTime(2013, 3, 31),
            new DateTime(2013, 4, 28),
            new DateTime(2013, 5, 26),
            new DateTime(2013, 6, 30),
            new DateTime(2013, 7, 28),
            new DateTime(2013, 8, 25),
            new DateTime(2013, 9, 29),
            new DateTime(2013, 10, 27),
            new DateTime(2013, 11, 24),
            new DateTime(2013, 12, 29)
        };

        var result2013 = DateUtils.LastSunday(2013);
        Assert.That(result2013, Is.EqualTo(expected2013));
    }

    [Test]
    public void LastSunday_WhenLeapYearWhereLastSundayIsLeapDay_ExpectLastSundayOfFebruaryIs29th()
    {
        var expected2032 = new List<DateTime>
        {
            new DateTime(2032, 1, 25),
            new DateTime(2032, 2, 29), // Leap year check: Last Sunday of February on the 29th
            new DateTime(2032, 3, 28),
            new DateTime(2032, 4, 25),
            new DateTime(2032, 5, 30),
            new DateTime(2032, 6, 27),
            new DateTime(2032, 7, 25),
            new DateTime(2032, 8, 29),
            new DateTime(2032, 9, 26),
            new DateTime(2032, 10, 31),
            new DateTime(2032, 11, 28),
            new DateTime(2032, 12, 26)
        };

        var result2032 = DateUtils.LastSunday(2032);
        Assert.That(result2032, Is.EqualTo(expected2032));
    }

}
