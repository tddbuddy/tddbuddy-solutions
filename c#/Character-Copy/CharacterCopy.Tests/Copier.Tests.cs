using NSubstitute;

namespace CharacterCopy.Tests
{
    [TestFixture]
    public class CopierTests
    {

        [Test]
        public void Ctor_GivenNullSource_ShouldThrowArgumentNullException()
        {
            // arrange
            var destination = Substitute.For<IDestination>();
            // act
            var result = Assert.Throws<ArgumentNullException>(() => new Copier(null, destination));
            // assert
            Assert.That(result.ParamName, Is.EqualTo("source"));
        }

        [Test]
        public void Ctor_GivenNullDestination_ShouldThrowArgumentNullException()
        {
            // arrange
            var source = Substitute.For<ISource>();
            // act
            var result = Assert.Throws<ArgumentNullException>(() => new Copier(source, null));
            // assert
            Assert.That(result.ParamName, Is.EqualTo("destination"));
        }

        [Test]
        public void Copy_GivenSingleChar_ShouldCopyChar()
        {
            // arrange
            var expectedChar = 'a';
            var source = CreateSource('a', '\n');
            var destination = CreateDesitination();
            var sut = new Copier(source, destination);
            // act
            sut.Copy();
            // assert
            source.Received(2).ReadChar();
            destination.Received(1).WriteChar(expectedChar);
        }

        [Test]
        public void Copy_GivenManyChar_ShouldCopyAllCharUntilNewline()
        {
            // arrange
            var source = CreateSource('a', 'b', 'c', 'd', '\n');
            var destination = CreateDesitination();
            var sut = new Copier(source, destination);
            // act
            sut.Copy();
            // assert
            source.Received(5).ReadChar();
            destination.Received(4).WriteChar(Arg.Any<char>());
        }

        // factory methods used in tests
        public ISource CreateSource(params char[] dataToRead)
        {
            var source = Substitute.For<ISource>();
            source.ReadChar().Returns(dataToRead[0], dataToRead.Skip(1).ToArray());
            return source;
        }

        public IDestination CreateDesitination()
        {
            return Substitute.For<IDestination>();
        }
    }
}
