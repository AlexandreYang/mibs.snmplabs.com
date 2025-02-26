#
# PySNMP MIB module GW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:20:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter32, NotificationType, Gauge32, iso, Integer32, MibIdentifier, ModuleIdentity, Bits, ObjectIdentity, experimental, TimeTicks, Counter64, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "NotificationType", "Gauge32", "iso", "Integer32", "MibIdentifier", "ModuleIdentity", "Bits", "ObjectIdentity", "experimental", "TimeTicks", "Counter64", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usr = MibIdentifier((1, 3, 6, 1, 4, 1, 429))
nas = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1))
gw = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 18))
gwTe = MibIdentifier((1, 3, 6, 1, 4, 1, 429, 1, 18, 1))
gwTeTable = MibTable((1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1), )
if mibBuilder.loadTexts: gwTeTable.setStatus('mandatory')
if mibBuilder.loadTexts: gwTeTable.setDescription('Table containing objects to enable traps on the Gateway Cards in the chassis.')
gwTeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1), ).setIndexNames((0, "GW-MIB", "gwTeIndex"))
if mibBuilder.loadTexts: gwTeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: gwTeEntry.setDescription('There is one entry for each Gateway Card in the chassis.')
gwTeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwTeIndex.setStatus('mandatory')
if mibBuilder.loadTexts: gwTeIndex.setDescription('A unique index identifying the Gateway Card to which the trap enable objects pertain.')
gwTegwNetworkFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gwTegwNetworkFailed.setStatus('mandatory')
if mibBuilder.loadTexts: gwTegwNetworkFailed.setDescription('Enable generation of an SNMP trap upon detection of an network failure of the specified gateway.')
gwTegwNetworkRestored = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enableTrap", 1), ("disableAll", 2), ("enableLog", 3), ("enableAll", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gwTegwNetworkRestored.setStatus('mandatory')
if mibBuilder.loadTexts: gwTegwNetworkRestored.setDescription('Enable generation of an SNMP trap upon detection of an network restore of the specified gateway.')
gwTegwIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwTegwIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: gwTegwIPAddress.setDescription('The Gateway IP Address.')
gwTeArNetFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gwTeArNetFailed.setStatus('mandatory')
if mibBuilder.loadTexts: gwTeArNetFailed.setDescription('This script is triggered when a Gateway NAC sends the NMC a network fail event.')
gwTeArNetRestored = MibTableColumn((1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gwTeArNetRestored.setStatus('mandatory')
if mibBuilder.loadTexts: gwTeArNetRestored.setDescription('This script is triggered when a Gateway NAC sends the NMC a network restored event.')
mibBuilder.exportSymbols("GW-MIB", gwTeEntry=gwTeEntry, gwTeArNetFailed=gwTeArNetFailed, gwTe=gwTe, gwTeArNetRestored=gwTeArNetRestored, gwTegwNetworkFailed=gwTegwNetworkFailed, gwTegwIPAddress=gwTegwIPAddress, nas=nas, gw=gw, gwTeTable=gwTeTable, gwTeIndex=gwTeIndex, gwTegwNetworkRestored=gwTegwNetworkRestored, usr=usr)
