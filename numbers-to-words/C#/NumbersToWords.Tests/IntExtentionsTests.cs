namespace NumbersToWords.Tests;

using NUnit.Framework;

[TestFixture]
public class NumberToWordsTests
{
    [Test]
    public void TestSingleDigits()
    {
        Assert.That(0.ToWords(), Is.EqualTo("zero"));
        Assert.That(5.ToWords(), Is.EqualTo("five"));
        Assert.That(8.ToWords(), Is.EqualTo("eight"));
    }

    [Test]
    public void TestDoubleDigits()
    {
        Assert.That(10.ToWords(), Is.EqualTo("ten"));
        Assert.That(21.ToWords(), Is.EqualTo("twenty-one"));
        Assert.That(77.ToWords(), Is.EqualTo("seventy-seven"));
    }

    [Test]
    public void TestThreeDigits()
    {
        Assert.That(100.ToWords(), Is.EqualTo("one hundred"));
        Assert.That(303.ToWords(), Is.EqualTo("three hundred three"));
        Assert.That(555.ToWords(), Is.EqualTo("five hundred fifty-five"));
    }

    [Test]
    public void TestFourDigits()
    {
        Assert.That(2000.ToWords(), Is.EqualTo("two thousand"));
        Assert.That(3466.ToWords(), Is.EqualTo("three thousand four hundred sixty-six"));
        Assert.That(2400.ToWords(), Is.EqualTo("two thousand four hundred"));
        Assert.That(5300.ToWords(), Is.EqualTo("five thousand three hundred"));
    }

    [Test]
    public void TestBoundaryValues()
    {
        Assert.That(20.ToWords(), Is.EqualTo("twenty"));
        Assert.That(99.ToWords(), Is.EqualTo("ninety-nine"));
        Assert.That(100.ToWords(), Is.EqualTo("one hundred"));
        Assert.That(999.ToWords(), Is.EqualTo("nine hundred ninety-nine"));
        Assert.That(1000.ToWords(), Is.EqualTo("one thousand"));
        Assert.That(9999.ToWords(), Is.EqualTo("nine thousand nine hundred ninety-nine"));
    }

    [Test]
    public void TestSpecialCases()
    {
        Assert.That(11.ToWords(), Is.EqualTo("eleven"));
        Assert.That(12.ToWords(), Is.EqualTo("twelve"));
        Assert.That(13.ToWords(), Is.EqualTo("thirteen"));
    }

    [Test]
    public void TestZeros()
    {
        Assert.That(1010.ToWords(), Is.EqualTo("one thousand ten"));
        Assert.That(1001.ToWords(), Is.EqualTo("one thousand one"));
    }

    [Test]
    public void TestExtremeCases()
    {
        Assert.That(1.ToWords(), Is.EqualTo("one"));
        Assert.That(9999.ToWords(), Is.EqualTo("nine thousand nine hundred ninety-nine"));
    }

    [Test]
    public void TestInvalidInput()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => (-1).ToWords());
        Assert.Throws<ArgumentOutOfRangeException>(() => 10000.ToWords());
    }
}
