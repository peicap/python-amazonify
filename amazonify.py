"""The simplest way to build Amazon Affiliate links, in Python."""


from urlparse import urlparse, urlunparse


def amazonify(url, affiliate_tag):
    """Generate an Amazon affiliate link given any Amazon link and affiliate
    tag.

    :param str url: The Amazon URL.
    :param str affiliate_tag: Your unique Amazon affiliate tag.
    :rtype: str or None
    :returns: An equivalent Amazon URL with the desired affiliate tag included,
        or None if the URL is invalid.

    Usage::

        >>> from amazonify import amazonify
        >>> url = 'someamazonurl'
        >>> tag = 'youraffiliatetag'
        >>> print amazonify(url, tag)
        ...
    """
    # Firstly, ensure the URL we're getting is valid:
    new_url = urlparse(url)
    if not new_url.netloc:
        return None

    # Secondly, remove all querystrings from the URL:
    new_url = new_url[:4] + ('',) + new_url[5:]

    return urlunparse(new_url)
