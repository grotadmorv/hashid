import re
import argparse
import wikipedia


list_hash = {}
list_hash_wikipedia = {}
wikipedia.set_lang("en")

list_hash["md5"] = '^[a-f0-9]{32}(:.+)?$'
list_hash_wikipedia['md5'] = "md5"

list_hash["sha1"] = '^[a-f0-9]{40}(:.+)?$'
list_hash_wikipedia['sha1'] = "sha-1"

list_hash["sha2"] = '^[a-f0-9]{56}$'
list_hash_wikipedia['sha2'] = "SHA-2#SHA-224"

list_hash["Blowfish(bcrypt)"] = '^(\$2[axy]|\$2)\$[0-9]{2}\$[a-z0-9\/.]{53}$'
list_hash_wikipedia['Blowfish(bcrypt)'] = "Blowfish_(cipher)"

list_hash["drupal7"] = '^\$S\$[a-z0-9\/.]{52}$'
list_hash_wikipedia['drupal7'] = "Drupal"

list_hash["Cisco-PIX"] = '^[a-z0-9\/.]{16}$'
list_hash_wikipedia['Cisco_PIX'] = "Cisco_PIX"

list_hash["Wordpress v2.6.0/2.6.1"] = '^\$H\$[a-z0-9\/.]{31}$'
list_hash_wikipedia['Wordpress v2.6.0/2.6.1'] = "WordPress"

list_hash["MySQL5.x"] = '^\*[a-f0-9]{40}$'
list_hash_wikipedia["MySQL5.x"] = "MySQL"

list_hash["Minecraft(AuthMe Reloaded)"] = '^\$sha\$[a-z0-9]{1,16}\$([a-f0-9]{32}|[a-f0-9]{40}|[a-f0-9]{64}|[a-f0-9]{128}|[a-f0-9]{140})$'
list_hash_wikipedia["Minecraft(AuthMe Reloaded)"] = "Minecraft"

list_hash["PostgreSQL"] = '^md5[a-f0-9]{32}$'
list_hash_wikipedia["PostgreSQL"] = "PostgreSQL"

list_hash["Microsoft Office 2013"] = '^\$office\$\*2013\*[0-9]{6}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{64}$'
list_hash_wikipedia["Microsoft Office 2013"] = "Microsoft_Office_2013"

list_hash["IPMI2 RAKP HMAC-SHA1"] = '^[a-f0-9]{130}(:[a-f0-9]{40})?$'
list_hash_wikipedia["IPMI2 RAKP HMAC-SHA1"] = "HMAC-based_One-time_Password_algorithm"

def find_hash(string):    
    for hash_name, regex in list_hash.items():
            if re.compile(regex, re.IGNORECASE).match(string) is not None:
                    return hash_name


parser = argparse.ArgumentParser(description='Find hash')
parser.add_argument('hash', metavar='hash', type=str, help='The Hash to find')
parser.add_argument('--list', dest='hash_list', action='store_const',
                    const=True, default=False,
                    help='List of hashes know')
parser.add_argument('--wikipedia', dest='hash_wikipedia', action='store_const',
                    const=True, default=False,
                    help='First wikipedia paragraph about the hash')

args = parser.parse_args()

if args.hash_list:
        print("List of hash : ")
        for hash_name, regex in list_hash.items():
                print(hash_name)

if args.hash_wikipedia:
        if find_hash(args.hash) is not None:
                print(wikipedia.summary( list_hash_wikipedia[find_hash(args.hash)] , sentences=2))

print(find_hash(args.hash))

