import re
import argparse


list_hash = {}

list_hash["md5"] = '^[a-f0-9]{32}(:.+)?$'
list_hash["sha1"] = '^[a-f0-9]{40}(:.+)?$'
list_hash["sha224"] = '^[a-f0-9]{56}$'
list_hash["Blowfish(bcrypt)"] = '^(\$2[axy]|\$2)\$[0-9]{2}\$[a-z0-9\/.]{53}$'
list_hash["drupal7"] = '^\$S\$[a-z0-9\/.]{52}$'
list_hash["Cisco-PIX"] = '^[a-z0-9\/.]{16}$'
list_hash["Wordpress v2.6.0/2.6.1"] = '^\$H\$[a-z0-9\/.]{31}$'
list_hash["MySQL5.x"] = '^\*[a-f0-9]{40}$'
list_hash["Minecraft(AuthMe Reloaded)"] = '^\$sha\$[a-z0-9]{1,16}\$([a-f0-9]{32}|[a-f0-9]{40}|[a-f0-9]{64}|[a-f0-9]{128}|[a-f0-9]{140})$'
list_hash["PostgreSQL"] = '^md5[a-f0-9]{32}$'
list_hash["Microsoft Office 2013"] = '^\$office\$\*2013\*[0-9]{6}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{64}$'
list_hash["IPMI2 RAKP HMAC-SHA1"] = '^[a-f0-9]{130}(:[a-f0-9]{40})?$'


def find_hash(string):    
    for hash_name, regex in list_hash.items():
            if re.compile(regex, re.IGNORECASE).match(string) is not None:
                    return hash_name


parser = argparse.ArgumentParser(description='Find hash')
parser.add_argument('hash', metavar='INPUT', type=str, help='The Hash to find')

args = parser.parse_args()
print(find_hash(args.hash))

