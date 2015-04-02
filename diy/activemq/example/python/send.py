#!/usr/bin/env python

import requests, json


#curl -d "body=strong" http://activemq-wrappers.rhcloud.com/demo/message/OPENSHIFT/DEMO?type=topic


server_name  = "activemq"
domain = "domainname"
queue_name= "DEMO"


activemq_url = "http://%s-%s.rhcloud.com/demo/message/OPENSHIFT/%s" % (server_name,domain,queue_name)
#activemq_url = "http://activemq-wrappers.rhcloud.com/demo/message/OPENSHIFT/DEMO?body="

body_tag="?body="
body_text="Ping!"

body= body_tag + body_text


r = requests.post(activemq_url+body)

print "returned with status code %i" % r.status_code




