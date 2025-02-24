#
# PySNMP MIB module HPN-ICF-PPPOE-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-PPPOE-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, MibIdentifier, iso, ModuleIdentity, Counter32, Counter64, TimeTicks, Bits, NotificationType, ObjectIdentity, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "ModuleIdentity", "Counter32", "Counter64", "TimeTicks", "Bits", "NotificationType", "ObjectIdentity", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfPPPoEServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102))
hpnicfPPPoEServer.setRevisions(('2009-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfPPPoEServer.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: hpnicfPPPoEServer.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: hpnicfPPPoEServer.setOrganization('')
if mibBuilder.loadTexts: hpnicfPPPoEServer.setContactInfo('')
if mibBuilder.loadTexts: hpnicfPPPoEServer.setDescription('The MIB module is used for PPPoE server.')
hpnicfPPPoEServerObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1))
hpnicfPPPoEServerMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPPPoEServerMaxSessions.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoEServerMaxSessions.setDescription('The maximum sessions supported by PPPoE server.')
hpnicfPPPoEServerCurrSessions = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPPPoEServerCurrSessions.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoEServerCurrSessions.setDescription('The number of current sessions on the PPPoE server.')
hpnicfPPPoEServerAuthRequests = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPPPoEServerAuthRequests.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoEServerAuthRequests.setDescription('The number of authentication requests.')
hpnicfPPPoEServerAuthSuccesses = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPPPoEServerAuthSuccesses.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoEServerAuthSuccesses.setDescription('The number of authentication succeses.')
hpnicfPPPoEServerAuthFailures = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPPPoEServerAuthFailures.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoEServerAuthFailures.setDescription('The number of authentication failure.')
hpnicfPPPoESAbnormOffsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPPPoESAbnormOffsThreshold.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoESAbnormOffsThreshold.setDescription('The threshold of abnormal offline count.')
hpnicfPPPoESAbnormOffPerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPPPoESAbnormOffPerThreshold.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoESAbnormOffPerThreshold.setDescription('The threshold of abnormal offline percent.')
hpnicfPPPoESNormOffPerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPPPoESNormOffPerThreshold.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoESNormOffPerThreshold.setDescription('The threshold of normal offline percent.')
hpnicfPPPoEServerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2))
hpnicfPPPoeServerTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2, 0))
hpnicfPPPoESAbnormOffsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2, 0, 1))
if mibBuilder.loadTexts: hpnicfPPPoESAbnormOffsAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoESAbnormOffsAlarm.setDescription('This trap is generated when the PPPoE server abnormal offline counts over threshold in five minutes.')
hpnicfPPPoESAbnormOffPerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2, 0, 2))
if mibBuilder.loadTexts: hpnicfPPPoESAbnormOffPerAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoESAbnormOffPerAlarm.setDescription('This trap is generated when the PPPoE server abnormal offline percent over threshold in five minutes.')
hpnicfPPPoESNormOffPerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2, 0, 3))
if mibBuilder.loadTexts: hpnicfPPPoESNormOffPerAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPPPoESNormOffPerAlarm.setDescription('This trap is generated when the PPPoE server normal offline percent under threshold in five minutes.')
mibBuilder.exportSymbols("HPN-ICF-PPPOE-SERVER-MIB", hpnicfPPPoEServerAuthSuccesses=hpnicfPPPoEServerAuthSuccesses, hpnicfPPPoEServer=hpnicfPPPoEServer, hpnicfPPPoEServerAuthFailures=hpnicfPPPoEServerAuthFailures, hpnicfPPPoESNormOffPerThreshold=hpnicfPPPoESNormOffPerThreshold, hpnicfPPPoEServerCurrSessions=hpnicfPPPoEServerCurrSessions, hpnicfPPPoESAbnormOffsAlarm=hpnicfPPPoESAbnormOffsAlarm, hpnicfPPPoEServerTraps=hpnicfPPPoEServerTraps, PYSNMP_MODULE_ID=hpnicfPPPoEServer, hpnicfPPPoEServerMaxSessions=hpnicfPPPoEServerMaxSessions, hpnicfPPPoeServerTrapPrefix=hpnicfPPPoeServerTrapPrefix, hpnicfPPPoEServerObject=hpnicfPPPoEServerObject, hpnicfPPPoESAbnormOffPerAlarm=hpnicfPPPoESAbnormOffPerAlarm, hpnicfPPPoEServerAuthRequests=hpnicfPPPoEServerAuthRequests, hpnicfPPPoESNormOffPerAlarm=hpnicfPPPoESNormOffPerAlarm, hpnicfPPPoESAbnormOffsThreshold=hpnicfPPPoESAbnormOffsThreshold, hpnicfPPPoESAbnormOffPerThreshold=hpnicfPPPoESAbnormOffPerThreshold)
