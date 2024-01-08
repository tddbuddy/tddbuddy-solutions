def parse_url(url):
    if not url.startswith(('http://', 'https://', 'ftp://', 'sftp://')):
        raise ValueError("Invalid URL")

    # Splitting the protocol
    protocol_split = url.split("://")
    protocol = protocol_split[0]
    rest = protocol_split[1]

    # Default ports
    default_ports = {'http': '80', 'https': '443', 'ftp': '21', 'sftp': '22'}

    # Initial values
    subdomain, domain, port, path = '', '', default_ports[protocol], ''

    # Splitting the rest of the URL
    if '/' in rest:
        domain_and_port, path = rest.split('/', 1)
        path = path.split('#')[0].split('?')[0]  # Removing fragment and query
    else:
        domain_and_port = rest

    # Handling subdomain and port
    if ':' in domain_and_port:
        domain_and_port, port = domain_and_port.split(':')

    # Splitting domain and subdomain
    domain_parts = domain_and_port.split('.')
    if len(domain_parts) == 1:
        # Case for 'localhost' or similar
        domain = domain_parts[0]
    elif len(domain_parts) == 2:
        # Regular domain with TLD
        domain = '.'.join(domain_parts)
    else:
        # Domain with subdomain and TLD
        domain = '.'.join(domain_parts[-2:])
        subdomain = '.'.join(domain_parts[:-2])

    return {
        'protocol': protocol,
        'subdomain': subdomain,
        'domain': domain,
        'port': port,
        'path': path
    }

