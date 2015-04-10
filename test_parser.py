#!/usr/bin/env python

import unittest
from parser import parse


class TestParser(unittest.TestCase):
    def test_parse_identifies_leftover_tasks(self):
        text = '''\
starting task A
starting task B
finishing task B
starting task C
starting task D
finishing task A'''
        expected = ['task C', 'task D']
        result = parse(text)
        self.assertItemsEqual(result, expected)

    def test_parse_works_when_all_tasks_finish(self):
        text = '''\
starting task A
starting task B
finishing task B
finishing task A'''
        expected = []
        result = parse(text)
        self.assertItemsEqual(result, expected)

    def test_parse_ignores_repeating_task_start_lines(self):
        text = '''\
starting task A
starting task B
starting task A
finishing task B
finishing task A'''
        expected = []
        result = parse(text)
        self.assertItemsEqual(result, expected)

    def test_parse_ignores_repeating_task_finish_lines(self):
        text = '''\
starting task A
starting task B
finishing task B
finishing task B
finishing task A'''
        expected = []
        result = parse(text)
        self.assertItemsEqual(result, expected)

    def test_parse_order_doesnt_matter(self):
        text = '''\
finishing task A
starting task A'''
        expected = []
        result = parse(text)
        self.assertItemsEqual(result, expected)

    def test_finishing_without_starting_is_ignored(self):
        text = '''\
finishing task B
'''
        expected = []
        result = parse(text)
        self.assertItemsEqual(result, expected)

    def test_weird_task_names(self):
        text = '''\
starting &#^@)*(^@)()
starting ^%#$^@#&(*&)
finishing ^%#$^@#&(*&)
starting !@G%G%G%
starting (GKM*FJ$*)
finishing &#^@)*(^@)()'''
        expected = ['(GKM*FJ$*)', '!@G%G%G%']
        result = parse(text)
        self.assertItemsEqual(result, expected)

    def test_maliciously_named_tasks_dont_cause_trouble(self):
        text = '''\
starting task starting task
starting task finishing task
starting task
finishing task starting task
'''
        expected = ['task finishing task', 'task']
        result = parse(text)
        self.assertItemsEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
