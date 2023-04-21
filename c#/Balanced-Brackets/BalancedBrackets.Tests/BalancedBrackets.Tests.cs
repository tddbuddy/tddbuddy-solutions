using BalancedBracketsKata;

namespace BalancedBracketsKataTests
{

    /*
     * Partitions and Boundaries to be tested
     * 
     * Empty String
     * Balanced Brackets
     *  Simple []
     *  Multiple [][]
     *  Nested [[]][
     *  Complex Nested [[[][]]]
     * Unbalanced Brackets
     *  Simple ][
     *  Mulitiple ][][
     *  Balanced and unbalanced mix [][]][
     *  Nested unbalanced [[]][[[]
     *  
     */

    [TestFixture]
    public class BalancedBracketsTests
    {
        [Test]
        public void TestEmptyString()
        {
            // Arrange
            string input = "";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsTrue(result);
        }

        [Test]
        public void TestSimpleBalancedBrackets()
        {
            // Arrange
            string input = "[]";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsTrue(result);
        }

        [Test]
        public void TestMultipleBalancedPairs()
        {
            // Arrange
            string input = "[][]";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsTrue(result);
        }

        [Test]
        public void TestNestedBalancedPairs()
        {
            // Arrange
            string input = "[[]]";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsTrue(result);
        }

        [Test]
        public void TestComplexNestedBalancedPairs()
        {
            // Arrange
            string input = "[[[][]]]";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsTrue(result);
        }

        [Test]
        public void TestSimpleUnbalancedBrackets()
        {
            // Arrange
            string input = "][";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsFalse(result);
        }

        [Test]
        public void TestMultipleUnmatchedClosingBrackets()
        {
            // Arrange
            string input = "][][";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsFalse(result);
        }

        [Test]
        public void TestBalancedPairsFollowedByUnmatchedClosingBrackets()
        {
            // Arrange
            string input = "[][]][";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsFalse(result);
        }

        [Test]
        public void TestNestedUnbalancedBrackets()
        {
            // Arrange
            string input = "[[]][[[]";

            // Act
            bool result = new BalancedBrackets().IsBalanced(input);

            // Assert
            Assert.IsFalse(result);
        }
        
    }
}
