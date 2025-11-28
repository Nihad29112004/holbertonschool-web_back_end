#!/usr/bin/env python3
"""initialize storage engine"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
