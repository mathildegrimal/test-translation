#!/usr/bin/env python3

import os
import logging
import re
from datetime import datetime

def generate_po_file(directory, output_file, language, locale):
    po_header = '''msgid ""
msgstr ""
"PO-Creation-Date: {creation_date}\\n"
"PO-Revision-Date: {revision_date}\\n"
"Last-Translator: dev \\n"
"Language-Team: {language} <http://weblate.tools.pradeo.net/projects/mathilde/>\\n"
"Language: {locale}\\n"
"test-trad/{locale}/>\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=n > 1;\\n"
'''.format(
        creation_date=datetime.now().strftime('%Y-%m-%d %H:%M%z'),
        revision_date=datetime.now().strftime('%Y-%m-%d %H:%M%z'),
        language=language,
        locale=locale
    )

    po_entries = []

    for root, _, files in os.walk(directory):
        print(root)

        for file in files:
            if file.endswith('.yml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        match = re.match(r'^\s*(\w+):\s*(.+)\s*$', line)
                        if match:
                            key = match.group(1)
                            value = match.group(2)
                            msgid = key
                            msgstr = value  # Placeholder for translation
                            po_entry = '''#: {file}:{line_number}
msgid "{msgid}"
msgstr "{msgstr}"
'''.format(file=file_path, line_number=i + 1, msgid=msgid, msgstr=msgstr)
                            po_entries.append(po_entry)

    with open(output_file, 'w') as f:
        f.write(po_header)
        for entry in po_entries:
            f.write(entry)
            f.write('\n')

# Usage
generate_po_file('dictionnaries/en', 'en.po','English','en')

