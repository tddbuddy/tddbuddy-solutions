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
    if '.' in domain_and_port:
        parts = domain_and_port.split('.')
        domain = parts[-2] + '.' + parts[-1]
        if len(parts) > 2:
            subdomain = '.'.join(parts[:-2])

    return {
        'protocol': protocol,
        'subdomain': subdomain,
        'domain': domain,
        'port': port,
        'path': path
    }

