# -*- coding: UTF-8 -*-
from optparse import OptionParser
import polib
import re
import sys


def parse_options():
    usage = """\n%prog [options] FILE1 FILE2\n"""
    parser = OptionParser(usage)

    (options, args) = parser.parse_args()
    return options, args


def diff(filepath1, filepath2):
    file1 = polib.pofile(filepath1)
    file2 = polib.pofile(filepath2)
    diff_po = polib.POFile()
    diff_po.metadata = file2.metadata

    for entry_file2 in file2:
        entry_file1 = file1.find(entry_file2.msgid,
                                 include_obsolete_entries=True)
        if not entry_file1:
            diff_po.append(entry_file2)
        # entry_file2.comment != entry_file1.comment or \
        elif entry_file2.msgstr != entry_file1.msgstr:
            diff_po.append(entry_file2)

    print(diff_po)


def main():
    options, args = parse_options()
    diff(*args)


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
