#
# PySNMP MIB module ZYXEL-DHCP-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-DHCP-RELAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, iso, Integer32, Counter32, Counter64, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, NotificationType, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "iso", "Integer32", "Counter32", "Counter64", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "NotificationType", "TimeTicks", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDhcpRelay = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18))
if mibBuilder.loadTexts: zyxelDhcpRelay.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelDhcpRelay.setOrganization('Enterprise Solution ZyXEL')
zyxelDhcpRelaySetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1))
zyxelDhcpRelayGlobalRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1))
zyxelDhcpRelayVlanRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2))
zyDhcpRelayGlobalRelayState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpRelayGlobalRelayState.setStatus('current')
zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers.setStatus('current')
zyxelDhcpRelayGlobalRelayRemoteServerTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 3), )
if mibBuilder.loadTexts: zyxelDhcpRelayGlobalRelayRemoteServerTable.setStatus('current')
zyxelDhcpRelayGlobalRelayRemoteServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 3, 1), ).setIndexNames((0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayGlobalRelayRemoteServerIpAddress"))
if mibBuilder.loadTexts: zyxelDhcpRelayGlobalRelayRemoteServerEntry.setStatus('current')
zyDhcpRelayGlobalRelayRemoteServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: zyDhcpRelayGlobalRelayRemoteServerIpAddress.setStatus('current')
zyDhcpRelayGlobalRelayRemoteServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyDhcpRelayGlobalRelayRemoteServerRowStatus.setStatus('current')
zyDhcpRelayGlobalRelayOption82Profile = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpRelayGlobalRelayOption82Profile.setStatus('current')
zyDhcpRelayGlobalRelayMaxNumberOfOption82Port = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpRelayGlobalRelayMaxNumberOfOption82Port.setStatus('current')
zyxelDhcpRelayGlobalRelayOption82PortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 6), )
if mibBuilder.loadTexts: zyxelDhcpRelayGlobalRelayOption82PortTable.setStatus('current')
zyxelDhcpRelayGlobalRelayOption82PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 6, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelDhcpRelayGlobalRelayOption82PortEntry.setStatus('current')
zyDhcpRelayGlobalRelayOption82PortProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 1, 6, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyDhcpRelayGlobalRelayOption82PortProfile.setStatus('current')
zyDhcpRelayVlanRelayMaxNumberOfRelays = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpRelayVlanRelayMaxNumberOfRelays.setStatus('current')
zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers.setStatus('current')
zyxelDhcpRelayVlanRelayRemoteServerTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3), )
if mibBuilder.loadTexts: zyxelDhcpRelayVlanRelayRemoteServerTable.setStatus('current')
zyxelDhcpRelayVlanRelayRemoteServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3, 1), ).setIndexNames((0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayVlanRelayRemoteServerServeVid"), (0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayVlanRelayRemoteServerIpAddress"))
if mibBuilder.loadTexts: zyxelDhcpRelayVlanRelayRemoteServerEntry.setStatus('current')
zyDhcpRelayVlanRelayRemoteServerServeVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: zyDhcpRelayVlanRelayRemoteServerServeVid.setStatus('current')
zyDhcpRelayVlanRelayRemoteServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: zyDhcpRelayVlanRelayRemoteServerIpAddress.setStatus('current')
zyDhcpRelayVlanRelayRemoteServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyDhcpRelayVlanRelayRemoteServerRowStatus.setStatus('current')
zyxelDhcpRelayVlanRelayTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 4), )
if mibBuilder.loadTexts: zyxelDhcpRelayVlanRelayTable.setStatus('current')
zyxelDhcpRelayVlanRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 4, 1), ).setIndexNames((0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayVlanRelayRemoteServerServeVid"))
if mibBuilder.loadTexts: zyxelDhcpRelayVlanRelayEntry.setStatus('current')
zyDhcpRelayVlanRelayOption82Profile = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 4, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpRelayVlanRelayOption82Profile.setStatus('current')
zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort.setStatus('current')
zyxelDhcpRelayVlanRelayOption82VlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 6), )
if mibBuilder.loadTexts: zyxelDhcpRelayVlanRelayOption82VlanPortTable.setStatus('current')
zyxelDhcpRelayVlanRelayOption82VlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 6, 1), ).setIndexNames((0, "ZYXEL-DHCP-RELAY-MIB", "zyDhcpRelayVlanRelayRemoteServerServeVid"), (0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelDhcpRelayVlanRelayOption82VlanPortEntry.setStatus('current')
zyDhcpRelayVlanRelayOption82VlanPortProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 18, 1, 2, 6, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyDhcpRelayVlanRelayOption82VlanPortProfile.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-DHCP-RELAY-MIB", zyxelDhcpRelayVlanRelayOption82VlanPortTable=zyxelDhcpRelayVlanRelayOption82VlanPortTable, zyxelDhcpRelayVlanRelayEntry=zyxelDhcpRelayVlanRelayEntry, zyDhcpRelayVlanRelayRemoteServerRowStatus=zyDhcpRelayVlanRelayRemoteServerRowStatus, zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort=zyDhcpRelayVlanRelayMaxNumberOfOption82VlanPort, zyxelDhcpRelayGlobalRelay=zyxelDhcpRelayGlobalRelay, zyDhcpRelayGlobalRelayState=zyDhcpRelayGlobalRelayState, zyxelDhcpRelayVlanRelayRemoteServerTable=zyxelDhcpRelayVlanRelayRemoteServerTable, zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers=zyDhcpRelayGlobalRelayRemoteServerMaxNumberOfServers, zyDhcpRelayGlobalRelayRemoteServerIpAddress=zyDhcpRelayGlobalRelayRemoteServerIpAddress, zyDhcpRelayVlanRelayRemoteServerIpAddress=zyDhcpRelayVlanRelayRemoteServerIpAddress, zyxelDhcpRelayGlobalRelayOption82PortTable=zyxelDhcpRelayGlobalRelayOption82PortTable, zyxelDhcpRelaySetup=zyxelDhcpRelaySetup, zyxelDhcpRelayVlanRelayTable=zyxelDhcpRelayVlanRelayTable, zyxelDhcpRelayGlobalRelayRemoteServerEntry=zyxelDhcpRelayGlobalRelayRemoteServerEntry, zyDhcpRelayVlanRelayOption82Profile=zyDhcpRelayVlanRelayOption82Profile, zyxelDhcpRelayGlobalRelayRemoteServerTable=zyxelDhcpRelayGlobalRelayRemoteServerTable, zyxelDhcpRelay=zyxelDhcpRelay, zyDhcpRelayVlanRelayRemoteServerServeVid=zyDhcpRelayVlanRelayRemoteServerServeVid, zyDhcpRelayVlanRelayOption82VlanPortProfile=zyDhcpRelayVlanRelayOption82VlanPortProfile, zyDhcpRelayGlobalRelayMaxNumberOfOption82Port=zyDhcpRelayGlobalRelayMaxNumberOfOption82Port, PYSNMP_MODULE_ID=zyxelDhcpRelay, zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers=zyDhcpRelayVlanRelayRemoteServerMaxNumberOfServers, zyxelDhcpRelayVlanRelayOption82VlanPortEntry=zyxelDhcpRelayVlanRelayOption82VlanPortEntry, zyDhcpRelayGlobalRelayOption82Profile=zyDhcpRelayGlobalRelayOption82Profile, zyxelDhcpRelayGlobalRelayOption82PortEntry=zyxelDhcpRelayGlobalRelayOption82PortEntry, zyxelDhcpRelayVlanRelayRemoteServerEntry=zyxelDhcpRelayVlanRelayRemoteServerEntry, zyDhcpRelayGlobalRelayOption82PortProfile=zyDhcpRelayGlobalRelayOption82PortProfile, zyDhcpRelayGlobalRelayRemoteServerRowStatus=zyDhcpRelayGlobalRelayRemoteServerRowStatus, zyDhcpRelayVlanRelayMaxNumberOfRelays=zyDhcpRelayVlanRelayMaxNumberOfRelays, zyxelDhcpRelayVlanRelay=zyxelDhcpRelayVlanRelay)
