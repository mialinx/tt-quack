# -*- coding: utf-8 -*-

import logging
import re
import time

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "do nishtyak"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *arg, **kwargs):
        iter_count = 0
        while True:
            iter_count += 1
            if iter_count > 100000000:
                iter_count = 0
            if not iter_count % 100000:
                print(iter_count)