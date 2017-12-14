import argparse
import logging


logger = logging.getLogger(__name__)


def overwatch_pagerduty_main():
    p = argparse.ArgumentParser()
    args = p.parse_args()
    try:
        pass
    except BaseException as e:
        logger.exception('Overwatch Pagerduty failed: %r', e)
        sys.exit(repr(e))
