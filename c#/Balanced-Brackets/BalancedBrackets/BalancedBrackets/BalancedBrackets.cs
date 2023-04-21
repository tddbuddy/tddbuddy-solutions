namespace BalancedBracketsKata
{
    public class BalancedBrackets
    {
        public bool IsBalanced(string input)
        {
            Stack<char> stack = new Stack<char>();

            foreach (char c in input)
            {
                if (c == '[')
                {
                    stack.Push(c);
                }
                else if (c == ']')
                {
                    if (stack.Count == 0 || stack.Pop() != '[')
                    {
                        return false;
                    }
                }
            }

            return stack.Count == 0;
        }
    }
}
