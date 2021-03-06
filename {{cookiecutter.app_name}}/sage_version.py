from re import findall
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

# Obtain the different Sage versions
def get_all_version_names(mirror_url, idx = None, distribution = '{{cookiecutter.travis_ubuntu_version}}'):
    if idx is None:
        idx = 0
    else:
        idx = int(idx)
    site = urlopen(mirror_url).read().decode('utf-8')
    ans = findall('(sage-([0-9.]*?)-{dist}.tar.bz2)'.format(dist=distribution), site)
    all_version_names = []
    for fname, ver in ans:
        if fname not in all_version_names:
            all_version_names.append(fname)
    return all_version_names[idx]
