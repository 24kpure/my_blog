#!/usr/bin/env python
# coding=utf-8

import uuid
import time


def next_id():
    t = time.time()
    return '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)
