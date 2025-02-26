#
# PySNMP MIB module VPMT-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPMT-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Unsigned32, Integer32, Counter64, Counter32, MibIdentifier, iso, Gauge32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Integer32", "Counter64", "Counter32", "MibIdentifier", "iso", "Gauge32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2))
class DisplayString(OctetString):
    pass

cdx6500VPMTCfgTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26), )
if mibBuilder.loadTexts: cdx6500VPMTCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgTable.setDescription('An VPMT Configuration Table.')
cdx6500VPMTCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1), ).setIndexNames((0, "VPMT-OPT-MIB", "cdx6500VPMTCfgEntryNum"))
if mibBuilder.loadTexts: cdx6500VPMTCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgEntry.setDescription('Entry in the VPMT Configuration Table. Each entry contains an index(cdx6500VPMTCfgEntryNum), and other configuration parameters fot a single VPMT table')
cdx6500VPMTCfgEntryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgEntryNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgEntryNum.setDescription('This indicate the VPMT Entry Number')
cdx6500VPMTCfgvpType = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("vpmt-ptype-null", 1), ("vpmt-ptype-voice", 2), ("vpmt-ptype-pri-voice", 3), ("vpmt-ptype-bypass-voice", 4), ("vpmt-ptype-tdm-data", 5), ("vpmt-ptype-pri-data", 6), ("vpmt-ptype-bypass-data", 7), ("vpmt-ptype-trans-ccs-voice", 8), ("vpmt-ptype-ccs-bypass", 9), ("vpmt-ptype-bri-voice", 10), ("vpmt-ptype-aam", 11), ("vpmt-ptype-num", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgvpType.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgvpType.setDescription("Specify the type of Virtual Port: NULL : No Configuration TDM-VOICE : Voice port operates on a configured DS0 PRI-VOICE : Voice port operates on a DS0 determined by the ISDN/QSIG D-Channel Transparent-CCS-VOICE : Voice port associated with a TBOP signaling channel BYPASS-VOICE : Voice and signaling transparently switched between configured DS0's TDM-DATA : Data port operates on a configured DS0 PRI-DATA : Data port operates on a DS0 determined by the ISDN/QSIG D-Channel BYPASS-DATA : Data transparently switched between configured DS0's CCS-BYPASS : Data or Voice switched between two ISDN/QSIG D-channel")
cdx6500VPMTCfgvpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgvpNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgvpNum.setDescription('Specify the Virtual Port Number, 100-254.')
cdx6500VPMTCfgdslNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgdslNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgdslNum.setDescription('Specify the Interface Number associated with this Virtual Port, 4-7 (1 based). Interface Number 1 supports TDM or PRI Data Ports only, Interface Number 2 and 3 not supported')
cdx6500VPMTCfgds0Rate = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("vpmt-rate-56k", 1), ("vpmt-rate-64k", 2), ("vpmt-rate-num", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgds0Rate.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgds0Rate.setDescription('Specify the DS0 Rate. For TDM-DATA this parameter controls the speed of the port. For PRI-DATA this parameter controls the speed of the port only for outbound calls from this node. The speed for an inbound call is determined by the incoming Call Request.')
cdx6500VPMTCfgsrcTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgsrcTimeSlot.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgsrcTimeSlot.setDescription('Specify the Time Slot assignments No of DS0/B-channel 1-24 for T1 No of DS0/B-channel 1-31 for E1 - TDM-DATA No of DS0/B-channel 1-15,17-31 for E1 - TDM-VOICE Note: Only TDM-DATA virtual port type can use more than 1 time slot. INT. 1 Supports max. 31 data ports. INT. 4 & 5 Supports max 31 data ports and 30 voice ports INT. 6 & 7 Supports max 31 data ports and 30 voice ports ')
cdx6500VPMTCfgdestTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgdestTimeSlot.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgdestTimeSlot.setDescription('Specify the number of Time Slot on the Destination interface: 1-24 for T1 1-31 for E1')
cdx6500VPMTCfglocalDialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfglocalDialNum.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfglocalDialNum.setDescription("Enter the Local Subscriber Address (ISDN number) for this virtual port/CCS Bypass connection. Use the space bar to blank the parameter. 1 to 20 characters For Outgoing Call: For Data Calls - This will be passed as the outgoing Calling Party number. Only valid characters are 0 - 9. For Voice Calls - This will be passed as the outgoing Calling Party number if the 'Calling Address Replacement' parameter is configured in the T1/E1 port record. Only valid characters are 0 - 9. For CCS Bypass - This parameter is not applicable. For Incoming Call: For Data Calls - The Called Party number received by the aggregate interface is compared to this parameter. Enter a trailing asterisk(*) as a wild-card. For Voice Calls - This will be passed as the ingoing Calling Party number if the 'Calling Address Replacement' parameter is configured in the T1/E1 port record. Only valid characters are 0 - 9. For CCS Bypass - The Called Party Number received by the aggregate interface is compared to this parameter. If a match is found, the ISDN/QSIG call will be forwarded to the adjacent T1/E1 port. If the first character is a '!' the call will be BYPASS if the remaining number does not match the Called Party Number. If the first character is a '@' the call will be will not be BYPASS if the remaining number matches the Called Party Number and the search for BYPASS match will be aborted")
cdx6500VPMTCfgsubAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgsubAddress.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgsubAddress.setDescription('Outgoing Call: This subaddress will be sent in the Call Setup Message. Incomin Call: This subaddress will be used for call verification if provided')
cdx6500VPMTCfgcallPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("out", 1), ("inc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgcallPermission.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgcallPermission.setDescription('Clear Circuit Mode call permission criteria. This defines the types of call handling criteria for the ISDN line. OUT - Initiates call only; does not accept call. INC - Accepts call only; does not send call to the network.')
cdx6500VPMTCfgnum_ccs_bypass_connections = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 11), Integer32()).setLabel("cdx6500VPMTCfgnum-ccs-bypass-connections").setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgnum_ccs_bypass_connections.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgnum_ccs_bypass_connections.setDescription('Specifies the maximum number of simultaneous CCS Bypass connections allowed to the called number.')
cdx6500VPMTCfgPhysical_Port = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 26, 1, 12), Integer32()).setLabel("cdx6500VPMTCfgPhysical-Port").setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500VPMTCfgPhysical_Port.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500VPMTCfgPhysical_Port.setDescription('Specify the Physical Port Number.')
mibBuilder.exportSymbols("VPMT-OPT-MIB", cdx6500VPMTCfglocalDialNum=cdx6500VPMTCfglocalDialNum, codex=codex, cdxProductSpecific=cdxProductSpecific, cdx6500VPMTCfgnum_ccs_bypass_connections=cdx6500VPMTCfgnum_ccs_bypass_connections, cdx6500VPMTCfgEntryNum=cdx6500VPMTCfgEntryNum, DisplayString=DisplayString, cdx6500Configuration=cdx6500Configuration, cdx6500VPMTCfgsrcTimeSlot=cdx6500VPMTCfgsrcTimeSlot, cdx6500CfgGeneralGroup=cdx6500CfgGeneralGroup, cdx6500VPMTCfgds0Rate=cdx6500VPMTCfgds0Rate, cdx6500VPMTCfgEntry=cdx6500VPMTCfgEntry, cdx6500VPMTCfgsubAddress=cdx6500VPMTCfgsubAddress, cdx6500VPMTCfgcallPermission=cdx6500VPMTCfgcallPermission, cdx6500VPMTCfgdslNum=cdx6500VPMTCfgdslNum, cdx6500VPMTCfgPhysical_Port=cdx6500VPMTCfgPhysical_Port, cdx6500VPMTCfgvpType=cdx6500VPMTCfgvpType, cdx6500VPMTCfgdestTimeSlot=cdx6500VPMTCfgdestTimeSlot, cdx6500VPMTCfgTable=cdx6500VPMTCfgTable, cdx6500=cdx6500, cdx6500VPMTCfgvpNum=cdx6500VPMTCfgvpNum)
