#!/usr/bin/env python
import requests, json

#http://activemq-domainname.rhcloud.com/demo/message/OPENSHIFT/DEMO?type=topic

activemq_url = "http://activemq-domainname.rhcloud.com/demo/message/OPENSHIFT/DEMO"
data = json.dumps({'type':'topic'}) 
r = requests.get(activemq_url)#, data)

print r.text
