using System;
using System.Linq;

namespace Validator
{
    public class IpValidator
    {
        public bool ValidateIpv4Address(string ipAddress)
        {
            if (string.IsNullOrWhiteSpace(ipAddress))
                return false;

            var parts = ipAddress.Split('.');
            if (parts.Length != 4)
                return false;

            foreach (var part in parts)
            {
                if (!byte.TryParse(part, out byte bytePart))
                    return false;

                if (part.Length > 1 && part.StartsWith("0"))
                    return false;
            }

            // Check if the last part is "0" or "255"
            return !(parts[3] == "0" || parts[3] == "255");
        }
    }
}
