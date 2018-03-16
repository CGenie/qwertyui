# -*- coding: UTF-8 -*-
"""
This tool is creating unique entries po file from few po files
"""
from optparse import OptionParser
from polib_parser_fix import polib
import re
import sys


def parse_options():
    usage = """\n%prog [options] FILE1 FILE2\n"""
    parser = OptionParser(usage)

    (options, args) = parser.parse_args()
    return options, args


def uniq(filepaths):
    end_po = polib.POFile()
    for filepath in filepaths:
        pofile = polib.pofile(filepath, encoding='utf8')
        if pofile.metadata:
            end_po.metadata = pofile.metadata

        for entry_file in pofile:
            entry_file_end = end_po.find(entry_file.msgid,
                                         include_obsolete_entries=True)
            if not entry_file_end:
                end_po.append(entry_file)
            else:
                entry_file_end.occurrences = list(set(
                    entry_file_end.occurrences + entry_file.occurrences))
                entry_file_end.msgstr = entry_file.msgstr

    print(end_po)


def main():
    options, args = parse_options()
    uniq(args)


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
