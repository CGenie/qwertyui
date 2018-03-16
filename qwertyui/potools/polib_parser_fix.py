import polib


def handle_oc(self):
    """Handle odoo format for occurences, standard polib parser is droping `:` in model paths """
    if self.current_state in ['mc', 'ms', 'mx']:
        self.instance.append(self.current_entry)
        self.current_entry = polib.POEntry(linenum=self.current_line)
    occurrences = self.current_token[3:].split()
    for occurrence in occurrences:
        self.current_entry.occurrences.append((occurrence, ''))
    return True


polib._POFileParser.handle_oc = handle_oc  # noqa
