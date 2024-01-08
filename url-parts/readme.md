# URL Parts
Decomposes a given URL into its parts.

## Example
When the URL `http://www.TDDBuddy.com` is decomposed into its parts:

- **Protocol**: http
- **Subdomain**: www
- **Domain**: TDDBuddy.com
- **Port**: 80 (Default for HTTP)
- **Path**: '' (Empty in our case)

## Considerations
Please be sure to handle the following:
- Only top level domains like `.com` or `.net`.
- Do not worry about second level domains like `.co.uk` or `.co.za`.
- Only the protocols specified in the default ports section below.
- Deal with local network hostname only cases. E.g., `http://localhost`.
- Do not use built-in classes like Uri to solve this.

## Default Ports
- **http**: 80
- **https**: 443
- **ftp**: 21
- **sftp**: 22

## Examples
1. URL: `http://foo.bar.com/foobar.html`
   - Protocol: http
   - Subdomain: foo
   - Domain name: bar.com
   - Port: 80
   - Path: foobar.html
2. URL: `https://www.foobar.com:8080/download/install.exe`
   - Protocol: https
   - Subdomain: www
   - Domain name: foobar.com
   - Port: 8080
   - Path: download/installer.exe
3. URL: `ftp://foo.com:9000/files`
   - Protocol: ftp
   - Subdomain: '' (empty string)
   - Domain name: foo.com
   - Port: 9000
   - Path: files
4. URL: `https://localhost/index.html#footer`
   - Protocol: https
   - Subdomain: '' (empty string)
   - Domain name: localhost
   - Port: 443
   - Path: index.html

## Hints
- Exclude the leading `/` when handling the path. E.g., `/download` becomes `download`.

