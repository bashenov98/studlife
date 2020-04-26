import os
from django.core.exceptions import ValidationError

FILE_SIZE = 1024000
EXTENSIONS = ['.jpg', '.png']

def file_size_validator(value):
    if value.size > FILE_SIZE:
        raise ValidationError(f'max file size is: {FILE_SIZE}')

def extension_validator(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in EXTENSIONS:
            raise ValidationError(f'not allowed file, it can only be: {EXTENSIONS}')