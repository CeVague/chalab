from contextlib import contextmanager
from zipfile import ZipFile

from .fs import tmp_dir


@contextmanager
def unzip_fp(f):
    with tmp_dir() as tmp:
        zf = ZipFile(f, mode='r')
        members = zf.namelist()

        members = [m for m in members
                   if (('__MACOS' not in m) and
                       (not m.startswith('/')) and
                       (not '..' in m))]

        for member in members:
            zf.extract(member, path=tmp)

        yield tmp
