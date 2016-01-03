from pysnmp.hlapi import *
import sys

target=str(sys.argv[1])
community=str(sys.argv[2])

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(community, mpModel=0),
           UdpTransportTarget((target, 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1][0] or '?'
        )
    )
else:
    for varBind in varBinds:
        print(' = '.join([ x.prettyPrint() for x in varBind ]))