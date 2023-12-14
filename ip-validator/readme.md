# IP Validator

Create a class with one method called `ValidateIpv4Address`. The method takes a string and returns `true` if it is a valid host assignable IP address and `false` if not.

IPv4 addresses are 32 bits long and grouped into 4 one-byte blocks separated by dotted-decimal notation, e.g., `192.168.1.1`.

Most IP addresses ending in 0 represent the entire network segment and cannot be used as host addresses. Similarly, most IP addresses ending in 255 represent a broadcast address and cannot be used as a host address. For the sake of this Kata, any address ending in 0 or 255 is not considered a valid host address.

**Note:** Do not use regular expressions to solve this Kata.

## Examples

| IP Address       | Result |
|------------------|--------|
| `1.1.1.1`        | `true` |
| `192.168.1.1`    | `true` |
| `10.0.0.1`       | `true` |
| `127.0.0.1`      | `true` |
| `192.168.1.0`    | `true` |
| `0.0.0.0`        | `false`|
| `255.255.255.255`| `false`|
| `10.0.1`         | `false`|
| `192.168.01.1`   | `false`|
| `192.168.1.00`   | `false`|
