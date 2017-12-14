#!/usr/bin/env python3

import argparse
from datetime import datetime
import logging
import os
import requests
from socket import getfqdn
from uuid import uuid4
import yaml


logger = logging.getLogger(__name__)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--dedup-key')
    p.add_argument('--event-action')
    args = p.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    token = os.environ['PD_TOKEN'] # pagerduty integration key
    data = {
        'routing_key': token,
        'dedup_key': args.dedup_key or uuid4().hex,
        'event_action': args.event_action or 'trigger',
        'client': 'Overwatch',
        'payload': {
            'summary': 'Test alert from overwatch-pagerduty on {hostname} @ {date}'.format(
                hostname=getfqdn(), date=datetime.utcnow().isoformat()),
            'severity': 'info',
            'source': 'Overwatch',
        },
    }
    print(yaml.dump(data))
    url = 'https://events.pagerduty.com/v2/enqueue'
    r = requests.post(url, json=data)
    logger.info('Response text: %s', r.text)
    r.raise_for_status()


if __name__ == '__main__':
    main()
