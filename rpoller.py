from pysnmp.hlapi import *
import sys

target=str(sys.argv[1])
community=str(sys.argv[2])
counter = 0

for errorIndication, \
    errorStatus, \
    errorIndex, \
    varBinds in nextCmd(SnmpEngine(),
                        CommunityData(community, mpModel=1),
                        UdpTransportTarget((target, 161)),
                        ContextData(),
                        ObjectType(ObjectIdentity('1.3.6.1.2.1.4.24.4.1.1')),
                        #ObjectType(ObjectIdentity('1.3.6.1.2.1.4.24.4.1.2')),
                        #ObjectType(ObjectIdentity('1.3.6.1.2.1.4.24.4.1.6')),
                        #ObjectType(ObjectIdentity('1.3.6.1.2.1.4.24.4.1.4')),
                        lexicographicMode=False):
    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1][0] or '?'
            )
        )
        break
    else:
        for name, val in varBinds:
            counter += 1
            print('route #%s, value = %s' % (counter, val.prettyPrint()))
            #At this point perform route lookup in a database
            #if new route, poll rest of info and add to db
            #if existing route, skip