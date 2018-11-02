import re
from pathlib import Path

list_hash = {}

list_hash["md5"] = '^[a-f0-9]{32}(:.+)?$'
list_hash["sha1"] = '^[a-f0-9]{40}(:.+)?$'
list_hash["sha224"] = '^[a-f0-9]{56}$'
list_hash["bcrypt"] = '^(\$2[axy]|\$2)\$[0-9]{2}\$[a-z0-9\/.]{53}$'
list_hash["drupal7"] = '^\$S\$[a-z0-9\/.]{52}$'
list_hash["Cisco-PIX(MD5)"] = '^[a-z0-9\/.]{16}$'
list_hash["Wordpress v2.6.0/2.6.1"] = '^\$H\$[a-z0-9\/.]{31}$'
list_hash["MySQL5.x"] = '^\*[a-f0-9]{40}$'
list_hash["Minecraft(AuthMe Reloaded)"] = '^\$sha\$[a-z0-9]{1,16}\$([a-f0-9]{32}|[a-f0-9]{40}|[a-f0-9]{64}|[a-f0-9]{128}|[a-f0-9]{140})$'
list_hash["PostgreSQL MD5"] = '^md5[a-f0-9]{32}$'
list_hash["Microsoft Office 2013"] = '^\$office\$\*2013\*[0-9]{6}\*[0-9]{3}\*[0-9]{2}\*[a-z0-9]{32}\*[a-z0-9]{32}\*[a-z0-9]{64}$'
list_hash["Android PIN"] = '^[a-f0-9]{40}:[a-f0-9]{16}$'



def find_hash(string):    
    for hash_name, regex in list_hash.items():
        print(re.compile(regex, re.IGNORECASE).match(string))


find_hash("68b329da9893e34099c7d8ad5cb9c940") # md5
find_hash("*BE1BDEC0AA74B4DCB079943E70528096CCA985F8") #mysql5
