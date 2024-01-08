import pytest
from parse_url import parse_url 

def test_standard_http_url():
    url = "http://foo.bar.com/foobar.html"
    expected = {
        'protocol': 'http',
        'subdomain': 'foo',
        'domain': 'bar.com',
        'port': '80',
        'path': 'foobar.html'
    }
    assert parse_url(url) == expected

def test_https_with_port_and_path():
    url = "https://www.foobar.com:8080/download/install.exe"
    expected = {
        'protocol': 'https',
        'subdomain': 'www',
        'domain': 'foobar.com',
        'port': '8080',
        'path': 'download/install.exe'
    }
    assert parse_url(url) == expected

def test_ftp_with_custom_port():
    url = "ftp://foo.com:9000/files"
    expected = {
        'protocol': 'ftp',
        'subdomain': '',
        'domain': 'foo.com',
        'port': '9000',
        'path': 'files'
    }
    assert parse_url(url) == expected

def test_https_localhost():
    url = "https://localhost/index.html#footer"
    expected = {
        'protocol': 'https',
        'subdomain': '',
        'domain': 'localhost',
        'port': '443',
        'path': 'index.html'
    }
    assert parse_url(url) == expected

def test_invalid_url():
    with pytest.raises(ValueError):
        parse_url("this_is_not_a_valid_url")

