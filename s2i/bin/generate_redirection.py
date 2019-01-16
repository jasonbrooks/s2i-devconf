#!/usr/bin/python3
redirects = {
    301: 'permanent',
    302: 'redirect'
}

import json
import sys
if len(sys.argv) > 1:
    f = json.loads(open(sys.argv[1]).read())
    for i in f['hosting']['redirects']:
        i['type'] = redirects[i['type']]
        print("rewrite {source} {destination} {type};".format(**i))
