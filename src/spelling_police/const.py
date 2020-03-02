# -*- coding: utf-8 -*-
# Copyright: (C) 2019-2020 Lovac42
# Support: https://github.com/lovac42/SpellingPolice
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


import re, os
from aqt.qt import qtminor
from pathlib import Path


ALT_BUILD_VERSION = qtminor < 10

RE_DICT_EXT_ENABLED = re.compile(r'\.bdic$', re.I)

RE_DICT_EXT_DISABLED = re.compile(r'\.bdic\.disabled$', re.I)

if not ALT_BUILD_VERSION:
    DICT_DIR = os.path.join(self.pm.base, "dictionaries")
else:
    from aqt import moduleDir
    # Wins only, prob won't work on mac or linux w/o permission
    DICT_DIR = os.path.join(moduleDir, "qtwebengine_dictionaries")
os.environ["QTWEBENGINE_DICTIONARIES_PATH"] = DICT_DIR

try:
    Path(DICT_DIR).mkdir(parents=True, exist_ok=True)
except:
    print("Can't create dictionary folder, check permissions.")


ALT_BUILD_INSTRUCTIONS = """\
You are using an alternate build of Anki that uses an older toolkit. Spell checking functionality requires special setup. Make sure you have read-write permissions.<br><br>
1) Create a folder called qtwebengine_dictionaries in the anki.exe folder. If you're on a mac or linux, google is your friend here. It uses the qtwebengine_dictionaries directory relative to the executable.<br><br>
2) Put all dictionaries in this folder.<br><br>
3) Restart Anki-alt and spell checking should start working. Test this on a new card first.
<br><br>
<img src="data:image/png;base64,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" />
"""
