from hashids import Hashids

pk = 123 # Your object's id
domain = 'satsbuster.herokuapp.com' # Your domain

# use the user name or the embed link as the salt
hashids = Hashids(salt='yo', min_length=6)
link_id = hashids.encode(pk)
url = 'http://{domain}/{link_id}'.format(domain=domain, link_id=link_id)

print(url)