# setup test env
import logging
import os
import settings
import sys


# setup logger
sherlock_logger = logging.getLogger('core.sherlock')
sherlock_logger.setLevel(logging.DEBUG)
filename = 'sherlock.tests.log.txt'

if settings.LOG_PATH:
    hdlr = logging.FileHandler(os.path.join(settings.LOG_PATH, filename))
else:
    hdlr = logging.StreamHandler(sys.__stdout__)

if hdlr:
    sherlock_logger.addHandler(hdlr)


def adjust_test_settings():
    """Adjusts the settings to support the unit tests"""
    # include the file suffixes available in the '/tests/text' dir
    settings.INCLUDE_FILE_SUFFIX = (
        '.h',
        '.m',
        '.c',
        '.cpp',
        '.py',
    )


def run_all():
    """Runs all unit tests
    """
    import test_indexer
    import test_searcher
    import test_transformer

    print 'Logging to "%s"' % (settings.LOG_PATH if settings.LOG_PATH else 'stdout')

    adjust_test_settings()
    test_indexer.run()
    test_searcher.run()
    #test_transformer.run()
