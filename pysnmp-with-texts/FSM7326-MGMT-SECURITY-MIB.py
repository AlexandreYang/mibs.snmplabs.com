#
# PySNMP MIB module FSM7326-MGMT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSM7326-MGMT-SECURITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
fsm7326, = mibBuilder.importSymbols("FSM7326-REF-MIB", "fsm7326")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, TimeTicks, Gauge32, Integer32, ModuleIdentity, Counter32, Counter64, Unsigned32, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "TimeTicks", "Gauge32", "Integer32", "ModuleIdentity", "Counter32", "Counter64", "Unsigned32", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsm7326MgmtSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11))
fsm7326MgmtSecurity.setRevisions(('2003-11-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fsm7326MgmtSecurity.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: fsm7326MgmtSecurity.setLastUpdated('200311210000Z')
if mibBuilder.loadTexts: fsm7326MgmtSecurity.setOrganization('Netgear')
if mibBuilder.loadTexts: fsm7326MgmtSecurity.setContactInfo('')
if mibBuilder.loadTexts: fsm7326MgmtSecurity.setDescription('')
agentSSLConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 1))
agentSSLAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLAdminMode.setStatus('current')
if mibBuilder.loadTexts: agentSSLAdminMode.setDescription('Configures whether the SSL service is enabled on this switch. The default value is disable(2).')
agentSSLSecurePort = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLSecurePort.setStatus('current')
if mibBuilder.loadTexts: agentSSLSecurePort.setDescription('Configures the port the SSL service will respond on. The default value is 443.')
agentSSLProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssl30", 1), ("tls10", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLProtocolLevel.setStatus('current')
if mibBuilder.loadTexts: agentSSLProtocolLevel.setDescription('Configures which protocol versions of SSL are enabled on this switch. The default value is both(3).')
agentSSHConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 2))
agentSSHAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHAdminMode.setStatus('current')
if mibBuilder.loadTexts: agentSSHAdminMode.setDescription('Configures whether the SSH service is enabled on this switch. The default value is disable(2).')
agentSSHProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssh10", 1), ("ssh20", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHProtocolLevel.setStatus('current')
if mibBuilder.loadTexts: agentSSHProtocolLevel.setDescription('Configures which protocol versions of SSH are enabled on this switch. The default value is both(3).')
agentSSHSessionsCount = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHSessionsCount.setStatus('current')
if mibBuilder.loadTexts: agentSSHSessionsCount.setDescription('Current number of active SSH sessions on this switch.')
mibBuilder.exportSymbols("FSM7326-MGMT-SECURITY-MIB", agentSSLProtocolLevel=agentSSLProtocolLevel, agentSSLConfigGroup=agentSSLConfigGroup, agentSSHSessionsCount=agentSSHSessionsCount, fsm7326MgmtSecurity=fsm7326MgmtSecurity, agentSSHAdminMode=agentSSHAdminMode, PYSNMP_MODULE_ID=fsm7326MgmtSecurity, agentSSLSecurePort=agentSSLSecurePort, agentSSHProtocolLevel=agentSSHProtocolLevel, agentSSHConfigGroup=agentSSHConfigGroup, agentSSLAdminMode=agentSSLAdminMode)
