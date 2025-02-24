#
# PySNMP MIB module NORTEL-SECURE-NETWORK-ACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-SECURE-NETWORK-ACCESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:14:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetPortNumber, InetAddressPrefixLength, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressPrefixLength", "InetAddressType", "InetAddress")
VlanId, VlanIdOrNone = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "VlanIdOrNone")
IdList, = mibBuilder.importSymbols("RAPID-CITY", "IdList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, Counter64, Integer32, TimeTicks, iso, ObjectIdentity, Bits, NotificationType, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Counter64", "Integer32", "TimeTicks", "iso", "ObjectIdentity", "Bits", "NotificationType", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
RowStatus, DisplayString, TruthValue, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention", "MacAddress")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
nortelSecureNetworkAccessMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 10))
nortelSecureNetworkAccessMib.setRevisions(('2007-06-29 00:00', '2007-05-21 00:00', '2007-04-18 00:00', '2007-03-13 00:00', '2006-11-30 00:00', '2006-07-07 00:00', '2006-05-22 00:00', '2006-05-19 00:00', '2006-04-26 00:00', '2006-02-24 00:00', '2005-10-24 00:00', '2005-08-18 00:00', '2005-08-10 00:00', '2005-07-28 00:00', '2005-07-18 00:00', '2005-07-07 00:00', '2005-06-22 00:00', '2005-06-02 00:00', '2005-05-04 00:00', '2005-04-21 00:00', '2005-04-19 00:00',))
if mibBuilder.loadTexts: nortelSecureNetworkAccessMib.setLastUpdated('200706290000Z')
if mibBuilder.loadTexts: nortelSecureNetworkAccessMib.setOrganization('Nortel Networks')
nsnaNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 10, 0))
nsnaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 10, 1))
class NsnaVlanIdOrNone(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), )
nsnaScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1))
nsnaEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaEnabled.setStatus('current')
nsnaNsnasConnectionState = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notConnected", 1), ("connected", 2), ("connecting", 3), ("closing", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasConnectionState.setStatus('current')
nsnaNsnasInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasInetAddressType.setStatus('current')
nsnaNsnasInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasInetAddress.setStatus('current')
nsnaNsnasSendHelloInterval = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasSendHelloInterval.setStatus('current')
nsnaNsnasInactivityInterval = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasInactivityInterval.setStatus('current')
nsnaNsnasStatusQuoInterval = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasStatusQuoInterval.setStatus('current')
nsnaMacAuthenticationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaMacAuthenticationEnabled.setStatus('current')
nsnaFailOpenEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaFailOpenEnabled.setStatus('current')
nsnaFailOpenVlan = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 11), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaFailOpenVlan.setStatus('current')
nsnaFailOpenFilterVlan = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 12), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaFailOpenFilterVlan.setStatus('current')
nsnaNsnasConnectionVersion = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasConnectionVersion.setStatus('current')
nsnaNsnasRadiusServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasRadiusServerEnabled.setStatus('current')
nsnaNsnasRadiusServerPort = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 1, 16), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaNsnasRadiusServerPort.setStatus('current')
nsnaNsnasTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2), )
if mibBuilder.loadTexts: nsnaNsnasTable.setStatus('current')
nsnaNsnasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1), ).setIndexNames((0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasAddressType"), (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasAddress"), (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasAddressMask"))
if mibBuilder.loadTexts: nsnaNsnasEntry.setStatus('current')
nsnaNsnasAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: nsnaNsnasAddressType.setStatus('current')
nsnaNsnasAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: nsnaNsnasAddress.setStatus('current')
nsnaNsnasAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 3), InetAddressPrefixLength())
if mibBuilder.loadTexts: nsnaNsnasAddressMask.setStatus('current')
nsnaNsnasPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 4), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(1024, 65535)).clone(5000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsnaNsnasPort.setStatus('current')
nsnaNsnasRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsnaNsnasRowStatus.setStatus('current')
nsnaPortTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3), )
if mibBuilder.loadTexts: nsnaPortTable.setStatus('current')
nsnaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1), ).setIndexNames((0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaPortIfIndex"))
if mibBuilder.loadTexts: nsnaPortEntry.setStatus('current')
nsnaPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nsnaPortIfIndex.setStatus('current')
nsnaPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("static", 2), ("dynamic", 3), ("uplink", 4), ("secure", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaPortMode.setStatus('current')
nsnaPortGreenVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 3), NsnaVlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaPortGreenVlanId.setStatus('current')
nsnaPortVoipVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 4), IdList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaPortVoipVlans.setStatus('current')
nsnaPortUplinkVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 5), IdList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaPortUplinkVlans.setStatus('current')
nsnaPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("red", 2), ("green", 3), ("yellow", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaPortState.setStatus('current')
nsnaPortDhcpState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blocked", 1), ("unblocked", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaPortDhcpState.setStatus('current')
nsnaPortHubModeEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaPortHubModeEnabled.setStatus('current')
nsnaPortHubModeMaxClients = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaPortHubModeMaxClients.setStatus('current')
nsnaVlanTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4), )
if mibBuilder.loadTexts: nsnaVlanTable.setStatus('current')
nsnaVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1), ).setIndexNames((0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaVlanId"))
if mibBuilder.loadTexts: nsnaVlanEntry.setStatus('current')
nsnaVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 1), VlanId())
if mibBuilder.loadTexts: nsnaVlanId.setStatus('current')
nsnaVlanColor = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("red", 2), ("green", 3), ("yellow", 4), ("voip", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaVlanColor.setStatus('current')
nsnaVlanFilterSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaVlanFilterSetName.setStatus('current')
nsnaVlanFilterSetId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaVlanFilterSetId.setStatus('current')
nsnaVlanYellowSubnetType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaVlanYellowSubnetType.setStatus('current')
nsnaVlanYellowSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaVlanYellowSubnet.setStatus('current')
nsnaVlanYellowSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 4, 1, 7), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nsnaVlanYellowSubnetMask.setStatus('current')
nsnaClientTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5), )
if mibBuilder.loadTexts: nsnaClientTable.setStatus('current')
nsnaClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1), ).setIndexNames((0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaClientIfIndex"), (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaClientMacAddress"))
if mibBuilder.loadTexts: nsnaClientEntry.setStatus('current')
nsnaClientIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nsnaClientIfIndex.setStatus('current')
nsnaClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 2), MacAddress())
if mibBuilder.loadTexts: nsnaClientMacAddress.setStatus('current')
nsnaClientDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("pc", 1), ("ipPhone", 2), ("passive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaClientDeviceType.setStatus('current')
nsnaClientVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 4), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaClientVlanId.setStatus('current')
nsnaClientAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaClientAddressType.setStatus('current')
nsnaClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaClientAddress.setStatus('current')
nsnaClientExpired = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaClientExpired.setStatus('current')
nsnaClientFilterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 8), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaClientFilterVlanId.setStatus('current')
nsnaClientStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("authenticatedByNsnas", 1), ("authenticatedLocally", 2), ("disallowedByNsnas", 3), ("isolatedByNsnas", 4), ("blacklistedByNsnas", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsnaClientStatus.setStatus('current')
nsnaStaticClientTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6), )
if mibBuilder.loadTexts: nsnaStaticClientTable.setStatus('current')
nsnaStaticClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1), ).setIndexNames((0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaStaticClientVlanId"), (0, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaStaticClientMacAddress"))
if mibBuilder.loadTexts: nsnaStaticClientEntry.setStatus('current')
nsnaStaticClientVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 1), VlanId())
if mibBuilder.loadTexts: nsnaStaticClientVlanId.setStatus('current')
nsnaStaticClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 2), MacAddress())
if mibBuilder.loadTexts: nsnaStaticClientMacAddress.setStatus('current')
nsnaStaticClientDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pc", 1), ("ipPhone", 2), ("passive", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsnaStaticClientDeviceType.setStatus('current')
nsnaStaticClientAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsnaStaticClientAddressType.setStatus('current')
nsnaStaticClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsnaStaticClientAddress.setStatus('current')
nsnaStaticClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 6, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsnaStaticClientRowStatus.setStatus('current')
nsnaIpPhoneSignatureTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 7), )
if mibBuilder.loadTexts: nsnaIpPhoneSignatureTable.setStatus('current')
nsnaIpPhoneSignatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 7, 1), ).setIndexNames((1, "NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaIpPhoneSignatureString"))
if mibBuilder.loadTexts: nsnaIpPhoneSignatureEntry.setStatus('current')
nsnaIpPhoneSignatureString = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 7, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: nsnaIpPhoneSignatureString.setStatus('current')
nsnaIpPhoneSignatureRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsnaIpPhoneSignatureRowStatus.setStatus('current')
nsnaNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 8))
nsnaClosedConnectionReason = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("snasClosedConnection", 2), ("dataStreamCorrupted", 3), ("bufferAllocationFailure", 4), ("messageProcessingFailure", 5), ("inactivityIntervalExpired", 6), ("nsnaAdministrativelyDown", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nsnaClosedConnectionReason.setStatus('current')
nsnaInvalidMessageHeader = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 10, 1, 8, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nsnaInvalidMessageHeader.setStatus('current')
nsnaClosedConnectionToSnas = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 10, 0, 1)).setObjects(("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaClosedConnectionReason"))
if mibBuilder.loadTexts: nsnaClosedConnectionToSnas.setStatus('current')
nsnaStatusQuoIntervalExpired = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 10, 0, 2))
if mibBuilder.loadTexts: nsnaStatusQuoIntervalExpired.setStatus('current')
nsnaInvalidMessageFromSnas = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 10, 0, 3)).setObjects(("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaInvalidMessageHeader"))
if mibBuilder.loadTexts: nsnaInvalidMessageFromSnas.setStatus('current')
nsnaSnasConnected = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 10, 0, 4)).setObjects(("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasInetAddressType"), ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasInetAddress"), ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasSendHelloInterval"), ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasInactivityInterval"), ("NORTEL-SECURE-NETWORK-ACCESS-MIB", "nsnaNsnasStatusQuoInterval"))
if mibBuilder.loadTexts: nsnaSnasConnected.setStatus('current')
mibBuilder.exportSymbols("NORTEL-SECURE-NETWORK-ACCESS-MIB", nsnaPortDhcpState=nsnaPortDhcpState, nsnaPortHubModeMaxClients=nsnaPortHubModeMaxClients, nsnaVlanYellowSubnetType=nsnaVlanYellowSubnetType, nsnaStaticClientDeviceType=nsnaStaticClientDeviceType, nsnaFailOpenFilterVlan=nsnaFailOpenFilterVlan, nsnaNsnasEntry=nsnaNsnasEntry, nsnaNsnasInetAddress=nsnaNsnasInetAddress, nsnaNsnasPort=nsnaNsnasPort, nsnaClosedConnectionToSnas=nsnaClosedConnectionToSnas, nsnaClientDeviceType=nsnaClientDeviceType, NsnaVlanIdOrNone=NsnaVlanIdOrNone, nsnaNsnasConnectionState=nsnaNsnasConnectionState, nsnaClientExpired=nsnaClientExpired, nsnaClientVlanId=nsnaClientVlanId, nsnaVlanFilterSetId=nsnaVlanFilterSetId, nortelSecureNetworkAccessMib=nortelSecureNetworkAccessMib, nsnaClientFilterVlanId=nsnaClientFilterVlanId, nsnaPortHubModeEnabled=nsnaPortHubModeEnabled, nsnaNsnasStatusQuoInterval=nsnaNsnasStatusQuoInterval, nsnaPortMode=nsnaPortMode, nsnaVlanEntry=nsnaVlanEntry, nsnaInvalidMessageFromSnas=nsnaInvalidMessageFromSnas, nsnaClosedConnectionReason=nsnaClosedConnectionReason, nsnaPortIfIndex=nsnaPortIfIndex, nsnaVlanTable=nsnaVlanTable, nsnaIpPhoneSignatureEntry=nsnaIpPhoneSignatureEntry, nsnaNsnasAddressMask=nsnaNsnasAddressMask, nsnaPortState=nsnaPortState, nsnaNotificationObjects=nsnaNotificationObjects, nsnaFailOpenVlan=nsnaFailOpenVlan, nsnaIpPhoneSignatureRowStatus=nsnaIpPhoneSignatureRowStatus, nsnaSnasConnected=nsnaSnasConnected, nsnaStaticClientRowStatus=nsnaStaticClientRowStatus, nsnaVlanFilterSetName=nsnaVlanFilterSetName, nsnaNsnasConnectionVersion=nsnaNsnasConnectionVersion, nsnaNotifications=nsnaNotifications, nsnaVlanId=nsnaVlanId, nsnaNsnasRadiusServerPort=nsnaNsnasRadiusServerPort, nsnaStaticClientMacAddress=nsnaStaticClientMacAddress, nsnaNsnasInetAddressType=nsnaNsnasInetAddressType, nsnaStaticClientAddressType=nsnaStaticClientAddressType, nsnaVlanYellowSubnet=nsnaVlanYellowSubnet, nsnaIpPhoneSignatureTable=nsnaIpPhoneSignatureTable, nsnaNsnasInactivityInterval=nsnaNsnasInactivityInterval, nsnaStaticClientEntry=nsnaStaticClientEntry, nsnaStaticClientAddress=nsnaStaticClientAddress, nsnaNsnasSendHelloInterval=nsnaNsnasSendHelloInterval, nsnaMacAuthenticationEnabled=nsnaMacAuthenticationEnabled, nsnaPortUplinkVlans=nsnaPortUplinkVlans, nsnaClientIfIndex=nsnaClientIfIndex, nsnaPortEntry=nsnaPortEntry, nsnaInvalidMessageHeader=nsnaInvalidMessageHeader, nsnaClientStatus=nsnaClientStatus, nsnaNsnasRowStatus=nsnaNsnasRowStatus, nsnaNsnasAddress=nsnaNsnasAddress, nsnaClientMacAddress=nsnaClientMacAddress, nsnaClientAddressType=nsnaClientAddressType, nsnaNsnasRadiusServerEnabled=nsnaNsnasRadiusServerEnabled, nsnaClientAddress=nsnaClientAddress, nsnaEnabled=nsnaEnabled, nsnaPortTable=nsnaPortTable, nsnaVlanColor=nsnaVlanColor, nsnaIpPhoneSignatureString=nsnaIpPhoneSignatureString, nsnaClientEntry=nsnaClientEntry, nsnaPortGreenVlanId=nsnaPortGreenVlanId, nsnaStatusQuoIntervalExpired=nsnaStatusQuoIntervalExpired, nsnaFailOpenEnabled=nsnaFailOpenEnabled, nsnaPortVoipVlans=nsnaPortVoipVlans, PYSNMP_MODULE_ID=nortelSecureNetworkAccessMib, nsnaStaticClientVlanId=nsnaStaticClientVlanId, nsnaVlanYellowSubnetMask=nsnaVlanYellowSubnetMask, nsnaStaticClientTable=nsnaStaticClientTable, nsnaClientTable=nsnaClientTable, nsnaObjects=nsnaObjects, nsnaNsnasTable=nsnaNsnasTable, nsnaScalars=nsnaScalars, nsnaNsnasAddressType=nsnaNsnasAddressType)
