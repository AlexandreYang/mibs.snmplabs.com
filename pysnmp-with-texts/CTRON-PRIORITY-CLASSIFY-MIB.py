#
# PySNMP MIB module CTRON-PRIORITY-CLASSIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-PRIORITY-CLASSIFY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:30:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ctPriorityExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPriorityExt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, IpAddress, Counter64, Bits, MibIdentifier, NotificationType, ModuleIdentity, Integer32, ObjectIdentity, Unsigned32, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Counter64", "Bits", "MibIdentifier", "NotificationType", "ModuleIdentity", "Integer32", "ObjectIdentity", "Unsigned32", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ctPriClassify = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6))
if mibBuilder.loadTexts: ctPriClassify.setLastUpdated('200203121855Z')
if mibBuilder.loadTexts: ctPriClassify.setOrganization('Cabletron Systems, Inc')
if mibBuilder.loadTexts: ctPriClassify.setContactInfo(' Cabletron Systems, Inc. Postal: 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 Phone: (603) 332-9400 Email: support@cabletron.com Web: http://www.cabletron.com')
if mibBuilder.loadTexts: ctPriClassify.setDescription('The Cabletron Priority Classify MIB module for controlling Cabletron specific priority classification criteria based on packet content.')
ctPriClassifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1))
class CtPriClassifyType(TextualConvention, Integer32):
    description = 'Each enumerated value represents a unique classification type. Different types have different rules regarding how data is interpreted during classification. These rules are spelled out in the comments preceding each type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("etherType", 1), ("llcDsapSsap", 2), ("ipTypeOfService", 3), ("ipProtocolType", 4), ("ipxClassOfService", 5), ("ipxPacketType", 6), ("ipAddressSource", 7), ("ipAddressDestination", 8), ("ipAddressBilateral", 9), ("ipxNetworkSource", 10), ("ipxNetworkDestination", 11), ("ipxNetworkBilateral", 12), ("ipUdpPortSource", 13), ("ipUdpPortDestination", 14), ("ipUdpPortBilateral", 15), ("ipTcpPortSource", 16), ("ipTcpPortDestination", 17), ("ipTcpPortBilateral", 18), ("ipxSocketSource", 19), ("ipxSocketDestination", 20), ("ipxSocketBilateral", 21), ("macAddressSource", 22), ("macAddressDestination", 23), ("macAddressBilateral", 24), ("ipFragments", 25))

class PortList(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'."
    status = 'current'

ctPriClassifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyStatus.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyStatus.setDescription('Allows the Priority Classification feature to be globally enabled/disabled. A value of disable(2), functionally supersedes the RowStatus of individual entries in the ctPriClassifyTable, but does not change their actual RowStatus value.')
ctPriClassifyMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyMaxEntries.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyMaxEntries.setDescription('The maximum number of entries allowed in the ctPriClassifyTable.')
ctPriClassifyNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyNumEntries.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyNumEntries.setDescription('The current number of entries in the ctPriClassifyTable.')
ctPriClassifyTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4), )
if mibBuilder.loadTexts: ctPriClassifyTable.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyTable.setDescription('A table containing configuration information for each Priority classification configured into the device by (local or network) management. All entries are permanent and will be restored after the device is reset.')
ctPriClassifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1), ).setIndexNames((0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPriority"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMeaning"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataVal"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMask"))
if mibBuilder.loadTexts: ctPriClassifyEntry.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyEntry.setDescription('Describes a particular entry of ctPriClassifyTable.')
ctPriClassifyPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: ctPriClassifyPriority.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyPriority.setDescription('The priority for this entry. Any packet meeting the classification criteria specified by this conceptual row will be given the priority indicated by this object.')
ctPriClassifyDataMeaning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 2), CtPriClassifyType())
if mibBuilder.loadTexts: ctPriClassifyDataMeaning.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyDataMeaning.setDescription('The meaning of the ctPriClassifyDataVal leaf for this conceptual row. The ctPriClassifyDataVal specifies a particular value which, when compared to packet data, is used to classify that packet to a particular priority. The part of the packet (if any), to which this data comparison applies, is determined by this object. For example, the value ipAddressBilateral(8) means that the value ctPriClassifyDataVal for this entry is an IP address. It further means that the given IP address will be compared against both source and destination IP address fields in a packet. Such an entry obviously would not not match against any non-IP packets. Additionally, the value of this leaf will impose certain implicit ranges and interpretations of data contained within the ctPriClassifyDataVal leaf for this entry. The specific limitations of each type should be spelled out in the comments for that type.')
ctPriClassifyDataVal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: ctPriClassifyDataVal.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyDataVal.setDescription('The data value associated with ctPriClassifyDataMeaning. The explicit range of this value is any unsigned 32-bit integer(0..4294967295). This range may vary, however, depending upon the value of ctPriClassifyDataMeaning. Illegal values should not be allowed.')
ctPriClassifyDataMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 4), Unsigned32())
if mibBuilder.loadTexts: ctPriClassifyDataMask.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyDataMask.setDescription("This object is the one's complement of a 32-bit mask. This mask is applicable to the data comparison of ctPriClassifyDataVal. The mask is applied to the actual packet data under consideration through a logical bitwise AND operation. This result is then compared to the data. For example, we want to classify according to a bilateral IP address of 134.141.0.0 with a mask of 255.255.240.0. This would be reflected by the following values: ctPriClassifyDataMeaning: ipAddressBilateral(8) ctPriClassifyDataVal: 0x868d0000 ctPriClassifyDataMask: 0x00000fff Again there are contextual implications for this leaf depending upon the value of ctPriClassifyDataMeaning. Not all types will use the mask, and others will impose restrictions. This value should however be a true indication of the masking operation. In other words, data types that don't use a mask should only allow a value of zero, indicating that all data bits are significant in the comparison. The specific restrictions of each type should be spelled out in the comments for that type. Illegal values should not be allowed.")
ctPriClassifyIngressList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 5), PortList().clone(hexValue="0000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctPriClassifyIngressList.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyIngressList.setDescription('The set of ports on which this classification rule applies. Classification occurs on ingress. An agent implementation should allow a set operation of this object to create a row if it does not exist.')
ctPriClassifyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctPriClassifyRowStatus.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyRowStatus.setDescription("This object provides both control and status for the associated conceptual row in the table. Rows can be created in two ways. createAndGo - The specified row will be created and activated if the instance is allowable. If not, an inconsistentValue exception will be returned and the row will not be created. This provides the most optimal method of creating an active row, but provides the user no explanation if the row cannot be created. createAndWait - The specified row will be created and put in the notInService state if the instance is allowable. A subsequent activation of this row will bring it into the active state. If the instance is not allowable, the row will be created and put in the notReady state. A subsequent activation of this row will fail. Since the inappropriate information is always contained in the indexing leaves, activation will never succeed and the row should be removed by the management station. When a row is in the notReady state, the ctPriClassifyRowInfo may be retrieved to obtain a plain English explanation of why this row cannot be activated. createAndWait is the preferred method for this reason. Both methods described above leave ctPriClassifyIngressList in it's default state, requiring an additional set operation in order to modify it. An even more optimal twist on the createAndWait method is to set the ctPriClassifyIngressList to it's desired value as a method for row creation. This will essentially cause an implicit createAndWait since it too will leave the row in either the notInService or notReady state. This leaves only activation or error analysis as the last step. Any rows left in the notReady or notInService state for more than 5 minutes should be automatically removed by the agent implementation.")
ctPriClassifyRowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyRowInfo.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyRowInfo.setDescription("This object provides info about this row in the form of an ASCII string, suitable for display purposes. The intended purpose of this object is to provide an 'agent-specific' explanation as to why the ctPriClassifyRowStatus for this conceptual row is in the 'notReady' state. A management station should read this object and display it to the user in this case. A conceptual row that does not fall into this category may simply return a single NULL, but may also provide any useful info of its choice. A management station may attempt to display such info if it so chooses, but is under no burden to do so.")
ctPriClassifyTOSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyTOSStatus.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyTOSStatus.setDescription('This object indicates whether an IP Type Of Service (TOS) value, defined by ctPriClassifyTOSValue, should be written into the TOS field of the IP header for any packet matching the classification specified by this conceptual row. This object may be set to enable only for the conceptual rows whose ctPriClassifyDataMeaning and ctPriClassifyDataVal have the following values: ctPriClassifyDataMeaning ctPriClassifyDataVal ------------------------ -------------------- etherType(1) 0x0800 (IP) llcDsapSsap(2) 0x0606 (IP) ipTypeOfService(3) any ipProtocolType(4) any ipAddressSource(7) any ipAddressDestination(8) any ipAddressBilateral(9) any ipUdpPortSource(13) any ipUdpPortDestination(14) any ipUdpPortBilateral(15) any ipTdpPortSource(16) any ipTdpPortDestination(17) any ipTdpPortBilateral(18) any ipFrag(25) not applicable A conceptual row that does not fall into these categories may be set to disable(2) and will return disable(2).')
ctPriClassifyTOSValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyTOSValue.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyTOSValue.setDescription('The value to be written into the IP TOS field of the IP header of any packet that matches the classification specified by the conceptual row.')
ctPriClassifyAbilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5), )
if mibBuilder.loadTexts: ctPriClassifyAbilityTable.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyAbilityTable.setDescription('A table containing information for each of the priority classification types. Types for which there is no corresponding row are not supported by this device.')
ctPriClassifyAbilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1), ).setIndexNames((0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyAbility"))
if mibBuilder.loadTexts: ctPriClassifyAbilityEntry.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyAbilityEntry.setDescription('Describes a particular entry of ctPriClassifyAbilityTable.')
ctPriClassifyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 1), CtPriClassifyType())
if mibBuilder.loadTexts: ctPriClassifyAbility.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyAbility.setDescription('The priority classification type associated with this entry.')
ctPriClassifyPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyPorts.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyPorts.setDescription('The set of ports on which the classification type specified by ctPriClassifyAbility is supported.')
ctPriClassifyTableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyTableLastChange.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyTableLastChange.setDescription('Indicates the sysUpTime at which the last change was made to the ctPriClassifyTable.')
ctPriClassifyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2))
ctPriClassifyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1))
ctPriClassifyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2))
ctPriClassifyBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1, 1)).setObjects(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyMaxEntries"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyNumEntries"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyIngressList"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowInfo"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSValue"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPorts"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTableLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctPriClassifyBaseGroup = ctPriClassifyBaseGroup.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyBaseGroup.setDescription('A collection of objects providing device level control and status information for Priority classification.')
ctPriClassifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2, 1)).setObjects(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctPriClassifyCompliance = ctPriClassifyCompliance.setStatus('current')
if mibBuilder.loadTexts: ctPriClassifyCompliance.setDescription('The compliance statement for devices that support Priority classification.')
mibBuilder.exportSymbols("CTRON-PRIORITY-CLASSIFY-MIB", ctPriClassifyTOSValue=ctPriClassifyTOSValue, ctPriClassify=ctPriClassify, ctPriClassifyRowStatus=ctPriClassifyRowStatus, ctPriClassifyAbilityTable=ctPriClassifyAbilityTable, PortList=PortList, ctPriClassifyRowInfo=ctPriClassifyRowInfo, ctPriClassifyCompliances=ctPriClassifyCompliances, ctPriClassifyBaseGroup=ctPriClassifyBaseGroup, ctPriClassifyEntry=ctPriClassifyEntry, ctPriClassifyMaxEntries=ctPriClassifyMaxEntries, ctPriClassifyPorts=ctPriClassifyPorts, CtPriClassifyType=CtPriClassifyType, ctPriClassifyStatus=ctPriClassifyStatus, ctPriClassifyTableLastChange=ctPriClassifyTableLastChange, ctPriClassifyDataVal=ctPriClassifyDataVal, ctPriClassifyIngressList=ctPriClassifyIngressList, ctPriClassifyDataMeaning=ctPriClassifyDataMeaning, ctPriClassifyPriority=ctPriClassifyPriority, ctPriClassifyGroups=ctPriClassifyGroups, PYSNMP_MODULE_ID=ctPriClassify, ctPriClassifyDataMask=ctPriClassifyDataMask, ctPriClassifyAbilityEntry=ctPriClassifyAbilityEntry, ctPriClassifyAbility=ctPriClassifyAbility, ctPriClassifyTable=ctPriClassifyTable, ctPriClassifyTOSStatus=ctPriClassifyTOSStatus, ctPriClassifyConformance=ctPriClassifyConformance, ctPriClassifyCompliance=ctPriClassifyCompliance, ctPriClassifyObjects=ctPriClassifyObjects, ctPriClassifyNumEntries=ctPriClassifyNumEntries)
