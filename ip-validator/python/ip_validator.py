class IpValidator:
    def validate_ipv4_address(self, ip_address):
        if not ip_address or not isinstance(ip_address, str):
            return False

        parts = ip_address.split('.')
        if len(parts) != 4:
            return False

        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False

            if len(part) > 1 and part.startswith('0'):
                return False

        # Check if the last part is '0' or '255'
        return not (parts[3] == '0' or parts[3] == '255')

