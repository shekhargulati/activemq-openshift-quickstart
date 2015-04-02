#!/usr/bin/env python
import requests, json, sys, getopt

#http://activemq-domainname.rhcloud.com/demo/message/OPENSHIFT/DEMO?type=topic

default_server  = "activemq"
default_domain = "domainname"
default_queue = "DEMO"
default_message ="Ping!"
default_sender = True


def usage():
    print 'wrapper.py [--sender/--receiver]  [-s <server>] [-d <domain>] [-q <queue>] [-m <message>]'
    sys.exit()




def run(isSender, server, domain, queue, message):
    if (isSender is None):
        isSender = default_sender
    if (server is None):
        server = default_server
    if (domain is None):
        domain = default_domain
    if (queue is None):
        queue = default_queue
    if (message is None):
        message = default_message

    body="&body=%s" % message
    activemq_url = "http://%s-%s.rhcloud.com/demo/message/OPENSHIFT/%s" % (server,domain,queue)
    #activemq_url = "http://%s-%s.rhcloud.com/demo/message/%s?type=queue" % (server,domain,queue)

    if (isSender) :
        print "Sender: Performing a POST request"
        req = requests.post(activemq_url+body)
    else :
        print "Performing  GET request as a receiver"
        req = requests.get(activemq_url)
	
    retval = ""
    if (req.status_code == requests.codes.ok) :
        retval += "got status OK"
        if ((not req.text is None) and (not req.text== "")) :
            retval += "\nHere is your message:\n"
            retval += req.text
    else: 
        retval += "returned with status code: %i" % req.status_code
        
    return retval





def main(argv):
    try:
        opts, args = getopt.getopt(argv,"SRhs:d:q:m:",["receiver""sender","server=","domain=","queue=","message="])
    except getopt.GetoptError:
        usage()    

    (isSender,server,domain,queue,message) = (None,None,None,None,None)
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-S", "--sender"):
            isSender  = True
        elif opt in ("-R", "--receiver"):
            isSender  = False
        elif opt in ("-s", "--server"):
            server = arg
        elif opt in ("-d", "--domain"):
            domain = arg
        elif opt in ("-q", "--queue"):
            queue = arg
        elif opt in ("-m", "--message"):
            message = arg

#    print "run(%s,%s,%s,%s,%s)" % (isSender,server,domain,queue,message)
    print run(isSender,server,domain,queue,message)

        
        

if __name__ == "__main__":
    main(sys.argv[1:])
    


