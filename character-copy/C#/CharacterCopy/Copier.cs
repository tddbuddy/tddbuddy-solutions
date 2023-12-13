namespace CharacterCopy
{
    public class Copier
    {
        private readonly ISource _source;
        private readonly IDestination _destination;

        public Copier(ISource source, IDestination destination)
        {
            _source = source ?? throw new ArgumentNullException(nameof(source));
            _destination = destination ?? throw new ArgumentNullException(nameof(destination));
        }

        public void Copy()
        {
            var nextChar = _source.ReadChar();
            while (nextChar != '\n')
            {
                _destination.WriteChar(nextChar);
                nextChar = _source.ReadChar();
            }
        }
    }
}

