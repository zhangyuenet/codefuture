#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

dist = 'testpath'
if not os.path.exists(dist) :
	os.mkdir(dist)
	n = 0
	while n < 10:
		os.mkdir('%s/subdir%d' % (dist, n) )
		n = n + 1


