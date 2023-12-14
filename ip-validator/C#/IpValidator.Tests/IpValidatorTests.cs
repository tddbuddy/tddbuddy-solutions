using Validator;

namespace IpValidationKata.Tests
{
    [TestFixture]
    public class IpValidatorTests
    {
        private IpValidator CreateValidator()
        {
            return new IpValidator();
        }

        [TestCase("1.1.1.1", true)]
        [TestCase("192.168.1.1", true)]
        [TestCase("10.0.0.1", true)]
        [TestCase("127.0.0.1", true)]
        public void ValidateIpv4Address_BasicFormatTests(string ipAddress, bool expectedResult)
        {
            // Arrange
            var validator = CreateValidator();

            // Act
            var result = validator.ValidateIpv4Address(ipAddress);

            // Assert
            Assert.That(result, Is.EqualTo(expectedResult));
        }

        [TestCase("256.1.1.1", false)]
        [TestCase("192.300.1.1", false)]
        [TestCase("10.0.0.256", false)]
        public void ValidateIpv4Address_RangeTests(string ipAddress, bool expectedResult)
        {
            // Arrange
            var validator = CreateValidator();

            // Act
            var result = validator.ValidateIpv4Address(ipAddress);

            // Assert
            Assert.That(result, Is.EqualTo(expectedResult));
        }

        [TestCase("01.1.1.1", false)]
        [TestCase("192.168.01.1", false)]
        [TestCase("10.0.0.01", false)]
        public void ValidateIpv4Address_LeadingZeroTests(string ipAddress, bool expectedResult)
        {
            // Arrange
            var validator = CreateValidator();

            // Act
            var result = validator.ValidateIpv4Address(ipAddress);

            // Assert
            Assert.That(result, Is.EqualTo(expectedResult));
        }

        [TestCase("192.168.1.0", false)]
        [TestCase("0.0.0.0", false)]
        [TestCase("255.255.255.255", false)]
        public void ValidateIpv4Address_NetworkAndBroadcastAddressTests(string ipAddress, bool expectedResult)
        {
            // Arrange
            var validator = CreateValidator();

            // Act
            var result = validator.ValidateIpv4Address(ipAddress);

            // Assert
            Assert.That(result, Is.EqualTo(expectedResult));
        }

        [TestCase(null, false)]
        [TestCase("", false)]
        [TestCase(" ", false)]
        [TestCase("not.an.ip", false)]
        [TestCase("1234.1234.1234.1234", false)]
        [TestCase("....", false)]
        public void ValidateIpv4Address_EdgeCaseTests(string ipAddress, bool expectedResult)
        {
            // Arrange
            var validator = CreateValidator();

            // Act
            var result = validator.ValidateIpv4Address(ipAddress);

            // Assert
            Assert.That(result, Is.EqualTo(expectedResult));
        }
    }
}
