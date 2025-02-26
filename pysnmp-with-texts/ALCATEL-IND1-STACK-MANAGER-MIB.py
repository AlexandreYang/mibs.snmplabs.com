#
# PySNMP MIB module ALCATEL-IND1-STACK-MANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-STACK-MANAGER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:19:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1StackMgr, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1StackMgr")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter32, TimeTicks, Gauge32, NotificationType, MibIdentifier, Integer32, ModuleIdentity, iso, Bits, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter32", "TimeTicks", "Gauge32", "NotificationType", "MibIdentifier", "Integer32", "ModuleIdentity", "iso", "Bits", "Counter64", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1StackMgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1))
alcatelIND1StackMgrMIB.setRevisions(('2009-02-06 00:00', '2007-04-03 00:00', '2005-07-15 00:00', '2004-07-01 00:00', '2004-04-23 00:00', '2004-04-08 00:00', '2004-04-04 00:00', '2004-03-22 00:00', '2004-03-08 00:00', '2001-08-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setRevisionsDescriptions(('Added alaStackMgrOperStackingMode and alaStackMgrAdminStackingMode objects. Added AlaStackMgrStackingMode TEXTUAL-CONVENTION.', 'Updated copyright information.', 'New trap alaStackMgrBadMixTrap has been added. AlaStackMgrSlotState & AlaStackMgrLinkNumber textual convention have been modified.', 'Updates on definitions for link states. Updates on pass through slot range.', 'New trap alaStackMgrOutOfPassThruSlotsTrap has been added.', 'alaStackMgrPassThruTrap has been split in three traps to assure backwards compatibility with previous releases of the Birds Of Prey products.', '-Command action and command status objects added to the chassis table. -Link state textual conventions have been updated.', 'Objects to handle information about token usage.', 'Objects to support the pass through mode added.', 'Addressing discrepancies with Alcatel Standard.',))
if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setLastUpdated('200902060000Z')
if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1StackMgrMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): For the Birds Of Prey Product Line Stack Manager The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1StackMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1))
alcatelIND1StackMgrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2))
alcatelIND1StackMgrTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3))
alaStackMgrTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4))
class AlaStackMgrLinkNumber(TextualConvention, Integer32):
    description = 'Lists the port numbers that the stackable ports can hold. Also the values are the same as the one marked on the Stack chassis pannel. These values are hardware dependent as follows: - First generation stackable switches - 24 ports: linkA27=27, linkB28=28, - First generation stackable switches - 48 ports: linkA51=51, linkB52=52, - 1st version of 2nd generation stackable switches : linkA31=31, linkB32=32. - 2nd version of 2nd generation stackable switches 24-port : linkA25=25, linkB26=26, - 2nd version of 2nd generation stackable switches 48-port : linkA29=29, linkB30=30.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(27, 28, 51, 52, 31, 32, 25, 26, 29, 30, 1, 2))
    namedValues = NamedValues(("linkA27", 27), ("linkB28", 28), ("linkA51", 51), ("linkB52", 52), ("linkA31", 31), ("linkB32", 32), ("linkA25", 25), ("linkB26", 26), ("linkA29", 29), ("linkB30", 30), ("linkA", 1), ("linkB", 2))

class AlaStackMgrNINumber(TextualConvention, Integer32):
    description = 'The numbers allocated for the stack NIs are as follows: - 0 = invalid slot number; - 1..8 = valid and assigned slot numbers corresponding values from the entPhysicalTable; - 1001..1008 = switches operating in pass through mode; - 255 = unassigned slot number.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1008)

class AlaStackMgrLinkStatus(TextualConvention, Integer32):
    description = 'Provides the logical stack link status. The logical link is considered operational if the physical link is operational and communication with the adjacent switch is active. The possible values are: - up(1), - down(2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class AlaStackMgrSlotRole(TextualConvention, Integer32):
    description = 'Indicates the role of each switch within the stack as follows: - unassigned(0), - primary(1), - secondary(2), - idle(3), - standalone(4), - passthrough(5)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unassigned", 0), ("primary", 1), ("secondary", 2), ("idle", 3), ("standalone", 4), ("passthrough", 5))

class AlaStackMgrStackStatus(TextualConvention, Integer32):
    description = 'Indicates whether the stack ring is or not in loop as follows: - loop(1), - noloop(2)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("loop", 1), ("noloop", 2))

class AlaStackMgrSlotState(TextualConvention, Integer32):
    description = "Current operational state of a stack element as follows: - running(1) : switch is fully operational, - duplicateSlot(2): switch operates in pass through mode due to slot duplication, - clearedSlot(3) : switch operates in pass through mode upon management command, - outOfSlots(4) : switch operates in pass through because the maximum number of allowed stackable swicthes has been reached, - outOfTokens(5) : switch operates in pass through mode because no tokens are available to be assigned. - badMix (6) : switch operates in pass through mode because it's not compatible with the existing stack."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("running", 1), ("duplicateSlot", 2), ("clearedSlot", 3), ("outOfSlots", 4), ("outOfTokens", 5), ("badMix", 6))

class AlaStackMgrCommandAction(TextualConvention, Integer32):
    description = 'Identifies which of the following actions is to be performed: - notSiginificant(0) : no action, - clearSlot(1) : saved slot number will be removed from persistent database, - clearSlotImmediately : saved slot number will be cleared and change will be in effect right away causing the switch to enter in pass through mode, - reloadAny(3) : reboot an element regardless of its operational mode, - reloadPassThru(4) : reboot an element that is operating in pass thru mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notSignificant", 0), ("clearSlot", 1), ("clearSlotImmediately", 2), ("reloadAny", 3), ("reloadPassThru", 4))

class AlaStackMgrCommandStatus(TextualConvention, Integer32):
    description = 'Identifies the current status of the last action command received as follows: - notSignificant(0), - clearSlotInProgress(1), - clearSlotFailed(2), - clearSlotSuccess(3), - setSlotInProgress(4), - setSlotFailed(5), - setSlotSuccess(6).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notSignificant", 0), ("clearSlotInProgress", 1), ("clearSlotFailed", 2), ("clearSlotSuccess", 3), ("setSlotInProgress", 4), ("setSlotFailed", 5), ("setSlotSuccess", 6))

class AlaStackMgrStackingMode(TextualConvention, Integer32):
    description = 'Stacking mode, which specifies the ability of a switch to be part of a set of switches or virtual chassis: - stackable(1) :the switch may be stacked with other switches in the same virtual chassis. - standalone(2) :the switch is not allowed to be stacked together with other switches.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stackable", 1), ("standalone", 2))

alaStackMgrChassisTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1), )
if mibBuilder.loadTexts: alaStackMgrChassisTable.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrChassisTable.setDescription('Maintains a list with information about all the switches that participate on the stack herein refered to as chassis.')
alaStackMgrChassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrChassisEntry.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrChassisEntry.setDescription('Each entry corresponds to a chassis and lists its role and neighbors in the stack.')
alaStackMgrSlotNINumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 1), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrSlotNINumber.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrSlotNINumber.setDescription('Numbers allocated for the stack NIs as follows: - 0: invalid slot number - 1..8: valid and assigned slot numbers corresponding to values from the entPhysicalTable - 1001..1008: swicthes operating in pass through mode - 255: unassigned slot number.')
alaStackMgrSlotCMMNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 72))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrSlotCMMNumber.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrSlotCMMNumber.setDescription('The numbers allocated for the stack CMMs are from 65..72 or 0 if not present')
alaStackMgrChasRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 3), AlaStackMgrSlotRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrChasRole.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrChasRole.setDescription('The current role of the chassis as follows: - unassigned(0), - primary(1), - secondary(2), - idle(3), - standalone(4), - passthrough(5).')
alaStackMgrLocalLinkStateA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 4), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrLocalLinkStateA.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrLocalLinkStateA.setDescription('1 indicates that the stacking link A is up, which means it knows its adjacent node. 2 indicates that the stacking link A is inactive and RemoteNISlotA and RemoteLinkA are not significants.')
alaStackMgrRemoteNISlotA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 5), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteNISlotA.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrRemoteNISlotA.setDescription(' This is the remote NI slot seen by the current NI through its stacking link A. The numbers allocated for the Stack NIs are 1..8, 1001..1008 or 0 if not present')
alaStackMgrRemoteLinkA = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 6), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteLinkA.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrRemoteLinkA.setDescription('This is the remote link of the remote NI slot seen through the stacking link A. The values for these ports are platform dependent. The possible values are: - 0: not present - linkA: 25, 27, 29, 31 or 51 - linkB: 26, 28, 30, 32 or 52.')
alaStackMgrLocalLinkStateB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 7), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrLocalLinkStateB.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrLocalLinkStateB.setDescription('1 indicates that the stacking link B is up, which means it knows its adjacent node. 2 indicates that the stacking link B is inactive and RemoteNISlotB and RemoteLinkB are not significants.')
alaStackMgrRemoteNISlotB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 8), AlaStackMgrNINumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteNISlotB.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrRemoteNISlotB.setDescription(' This is the remote NI slot seen by the current NI through its stacking link B. The numbers allocated for the Stack NIs are 1..8, 1001..1008 or 0 if not present')
alaStackMgrRemoteLinkB = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 9), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrRemoteLinkB.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrRemoteLinkB.setDescription('This is the remote link of the remote NI slot seen through the stacking link B. The values for these ports are platform dependent. The possible values are: - 0: not present - linkA: 25, 27, 29, 31 or 51 - linkB: 26, 28, 30, 32 or 52.')
alaStackMgrChasState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 10), AlaStackMgrSlotState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrChasState.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrChasState.setDescription('This current state of the chassis: running (1), duplicateSlot (2), clearedSlot (3), outOfSlots (4), outOfTokens (5), or badMix (6).')
alaStackMgrSavedSlotNINumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 11), AlaStackMgrNINumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrSavedSlotNINumber.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrSavedSlotNINumber.setDescription('Slot number stored in persistent memory that will be in effect if the stack element reboots. Only slot numbers in the range 1..8 are allowed.')
alaStackMgrCommandAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 12), AlaStackMgrCommandAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrCommandAction.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrCommandAction.setDescription('This object identifies which of the following Actions is to be performed: clearSlot(1), clearSlotImmediately (2) or reload (3). Whenever a new command is received, the value of the object alaStackMgrCommandStatus will be updated accordingly.')
alaStackMgrCommandStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 13), AlaStackMgrCommandStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrCommandStatus.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrCommandStatus.setDescription('This object provides the current status of last command received from the management as follows: notSignificant(0), clearSlotInProgress(1), clearSlotFailed(2), clearSlotSuccess(3), setSlotInProgress(4), setSlotFailed(5) or setSlotSuccess(6). New commands are only accepted if the value of this object is different than setSlotInProgress and clearSlotInProgress.')
alaStackMgrOperStackingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 14), AlaStackMgrStackingMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrOperStackingMode.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrOperStackingMode.setDescription('This object specifies the current running mode of the switch.')
alaStackMgrAdminStackingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 1, 1, 15), AlaStackMgrStackingMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrAdminStackingMode.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrAdminStackingMode.setDescription('This object specifies the stack mode atained on reload.')
alaStackMgrStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2), )
if mibBuilder.loadTexts: alaStackMgrStatsTable.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStatsTable.setDescription('Stack port statistics table.')
alaStackMgrStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStatLinkNumber"))
if mibBuilder.loadTexts: alaStackMgrStatsEntry.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStatsEntry.setDescription(' Stats table for stackable ports.')
alaStackMgrStatLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 1), AlaStackMgrLinkNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatLinkNumber.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStatLinkNumber.setDescription(' Local link refers to the stacking port on each slot. The values of these ports are: - linkA: 25, 27, 29, 31 or 51 - linkB: 26, 28, 30, 32 or 52.')
alaStackMgrStatPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatPktsRx.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStatPktsRx.setDescription('The total number of packets recieved on this port.')
alaStackMgrStatPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatPktsTx.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStatPktsTx.setDescription('The total number of packets transmitted on this port.')
alaStackMgrStatErrorsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatErrorsRx.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStatErrorsRx.setDescription('The total number of packets in error - received on the port.')
alaStackMgrStatErrorsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatErrorsTx.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStatErrorsTx.setDescription('The total number of packets in error - transmitted on the port.')
alaStackMgrStatDelayFromLastMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStatDelayFromLastMsg.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStatDelayFromLastMsg.setDescription('The delay since the last message.')
alaStackMgrStackStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 3), AlaStackMgrStackStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStackStatus.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStackStatus.setDescription('Indicates whether the Stack is or not in Loop.')
alaStackMgrTokensUsed = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrTokensUsed.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrTokensUsed.setDescription('Indicates the total number of tokens that have been allocated to all the elements in the stack.')
alaStackMgrTokensAvailable = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrTokensAvailable.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrTokensAvailable.setDescription('Indicates the total number of tokens that are still available and that potentially may be allocated to elements of the stack.')
alaStackMgrStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6), )
if mibBuilder.loadTexts: alaStackMgrStaticRouteTable.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRouteTable.setDescription('Maintains a list with information about all the static routes in the stack.')
alaStackMgrStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1), ).setIndexNames((0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteSrcStartIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteSrcEndIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteDstStartIf"), (0, "ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStaticRouteDstEndIf"))
if mibBuilder.loadTexts: alaStackMgrStaticRouteEntry.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRouteEntry.setDescription('Each entry corresponds to a static route and lists its source and destination in the stack.')
alaStackMgrStaticRouteSrcStartIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: alaStackMgrStaticRouteSrcStartIf.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRouteSrcStartIf.setDescription('The physical identification number for start source range of the static route')
alaStackMgrStaticRouteSrcEndIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: alaStackMgrStaticRouteSrcEndIf.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRouteSrcEndIf.setDescription('The physical identification number for end source range of the static route')
alaStackMgrStaticRouteDstStartIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: alaStackMgrStaticRouteDstStartIf.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRouteDstStartIf.setDescription('The physical identification number for start destination range of the static route')
alaStackMgrStaticRouteDstEndIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 4), InterfaceIndex())
if mibBuilder.loadTexts: alaStackMgrStaticRouteDstEndIf.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRouteDstEndIf.setDescription('The physical identification number for end destination range of the static route')
alaStackMgrStaticRoutePort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 5), AlaStackMgrLinkNumber().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrStaticRoutePort.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRoutePort.setDescription('This is the stack link to the destination NI slot . The values for these ports are platform dependent. The possible values are: - 0: not present - linkA: 25, 27, 29, 31 or 51 - linkB: 26, 28, 30, 32 or 52. Incase of static routesthe value is either 1(STACKA) or 2(STACKB)')
alaStackMgrStaticRoutePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 6), AlaStackMgrLinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaStackMgrStaticRoutePortState.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRoutePortState.setDescription('1 indicates that the static route stacking link is up . 2 indicates that the stacking link is inactive.')
alaStackMgrStaticRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrStaticRouteStatus.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRouteStatus.setDescription('Whether this static route is enabled or disabled .')
alaStackMgrStaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 1, 6, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaStackMgrStaticRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrStaticRouteRowStatus.setDescription('The status of this table entry. ')
alaStackMgrTrapLinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 1), AlaStackMgrLinkNumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrTrapLinkNumber.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrTrapLinkNumber.setDescription('Holds the link number, when the stack is not in loop.')
alaStackMgrPrimary = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 2), AlaStackMgrNINumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrPrimary.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrPrimary.setDescription('Holds the slot number of the stack element that plays the role of Primary.')
alaStackMgrSecondary = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 3, 3), AlaStackMgrNINumber()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaStackMgrSecondary.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrSecondary.setDescription('Holds the slot number of the stack element that plays the role of Secondary.')
alaStackMgrDuplicateSlotTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrDuplicateSlotTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrDuplicateSlotTrap.setDescription('The element specified by alaStackMgrSlotNINumber has the same slot number of another element of the stack and it must relinquish its operational status because it has a higher election key (up time, slot, mac). The elements will be put in pass through mode.')
alaStackMgrNeighborChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 2)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrStackStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrTrapLinkNumber"))
if mibBuilder.loadTexts: alaStackMgrNeighborChangeTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrNeighborChangeTrap.setDescription('Indicates whether the stack is in loop or not. In case of no loop, alaStackMgrSlotNINumber and alaStackMgrTrapLinkNumber indicate where the Stack is broken')
alaStackMgrRoleChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 3)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrPrimary"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSecondary"))
if mibBuilder.loadTexts: alaStackMgrRoleChangeTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrRoleChangeTrap.setDescription(' Role Change Trap. Indicates that a new primary or secondary is elected.')
alaStackMgrDuplicateRoleTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 4)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasRole"))
if mibBuilder.loadTexts: alaStackMgrDuplicateRoleTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrDuplicateRoleTrap.setDescription('The element identified by alaStackMgrSlotNINumber detected the presence of two elements with the same primary or secondary role as specified by alaStackMgrChasRole on the stack.')
alaStackMgrClearedSlotTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 5)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrClearedSlotTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrClearedSlotTrap.setDescription('The element identified by alaStackMgrSlotNINumber will enter the pass through mode because its operational slot was cleared with immediate effect.')
alaStackMgrOutOfSlotsTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 6))
if mibBuilder.loadTexts: alaStackMgrOutOfSlotsTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrOutOfSlotsTrap.setDescription('One element of the stack will enter the pass through mode because there are no slot numbers available to be assigned to this element.')
alaStackMgrOutOfTokensTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 7)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrOutOfTokensTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrOutOfTokensTrap.setDescription('The element identified by alaStackMgrSlotNINumber will enter the pass through mode because there are no tokens available to be assigned to this element.')
alaStackMgrOutOfPassThruSlotsTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 8))
if mibBuilder.loadTexts: alaStackMgrOutOfPassThruSlotsTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrOutOfPassThruSlotsTrap.setDescription('There are no pass through slots available to be assigned to an element that is supposed to enter the pass through mode.')
alaStackMgrBadMixTrap = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 4, 0, 9)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"))
if mibBuilder.loadTexts: alaStackMgrBadMixTrap.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrBadMixTrap.setDescription('The element identified by alaStackMgrSlotNINumber will enter the pass through mode because it is not compatible with the existing stack.')
alcatelIND1StackMgrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1))
alcatelIND1StackMgrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 2))
alaStackMgrCfgMgrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSlotCMMNumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasRole"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrLocalLinkStateA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteNISlotA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteLinkA"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrLocalLinkStateB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteNISlotB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRemoteLinkB"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrChasState"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrSavedSlotNINumber"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCommandAction"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCommandStatus"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOperStackingMode"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrAdminStackingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrCfgMgrGroup = alaStackMgrCfgMgrGroup.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrCfgMgrGroup.setDescription('A collection of objects providing information about the topology of the stack .')
alaStackMgrNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrDuplicateSlotTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrNeighborChangeTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrRoleChangeTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrDuplicateRoleTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrClearedSlotTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfSlotsTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfTokensTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrOutOfPassThruSlotsTrap"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrBadMixTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaStackMgrNotificationGroup = alaStackMgrNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: alaStackMgrNotificationGroup.setDescription('A collection of notifications for signaling Stack manager events.')
alcatelIND1StackMgrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 24, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrCfgMgrGroup"), ("ALCATEL-IND1-STACK-MANAGER-MIB", "alaStackMgrNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1StackMgrMIBCompliance = alcatelIND1StackMgrMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1StackMgrMIBCompliance.setDescription('The compliance statement for device support of Stack Manager.')
mibBuilder.exportSymbols("ALCATEL-IND1-STACK-MANAGER-MIB", alaStackMgrStatPktsTx=alaStackMgrStatPktsTx, alaStackMgrNeighborChangeTrap=alaStackMgrNeighborChangeTrap, AlaStackMgrNINumber=AlaStackMgrNINumber, alaStackMgrStaticRoutePortState=alaStackMgrStaticRoutePortState, alaStackMgrDuplicateRoleTrap=alaStackMgrDuplicateRoleTrap, alaStackMgrTrapLinkNumber=alaStackMgrTrapLinkNumber, alaStackMgrOutOfSlotsTrap=alaStackMgrOutOfSlotsTrap, alaStackMgrOutOfPassThruSlotsTrap=alaStackMgrOutOfPassThruSlotsTrap, alaStackMgrDuplicateSlotTrap=alaStackMgrDuplicateSlotTrap, alaStackMgrRoleChangeTrap=alaStackMgrRoleChangeTrap, alaStackMgrLocalLinkStateA=alaStackMgrLocalLinkStateA, alaStackMgrCfgMgrGroup=alaStackMgrCfgMgrGroup, alcatelIND1StackMgrMIBObjects=alcatelIND1StackMgrMIBObjects, alaStackMgrStatPktsRx=alaStackMgrStatPktsRx, alaStackMgrStaticRouteRowStatus=alaStackMgrStaticRouteRowStatus, alcatelIND1StackMgrMIBCompliance=alcatelIND1StackMgrMIBCompliance, alaStackMgrSecondary=alaStackMgrSecondary, alaStackMgrAdminStackingMode=alaStackMgrAdminStackingMode, alaStackMgrStatDelayFromLastMsg=alaStackMgrStatDelayFromLastMsg, AlaStackMgrSlotState=AlaStackMgrSlotState, alaStackMgrChassisEntry=alaStackMgrChassisEntry, alaStackMgrStaticRouteDstStartIf=alaStackMgrStaticRouteDstStartIf, PYSNMP_MODULE_ID=alcatelIND1StackMgrMIB, alaStackMgrStaticRouteStatus=alaStackMgrStaticRouteStatus, AlaStackMgrSlotRole=AlaStackMgrSlotRole, alaStackMgrNotificationGroup=alaStackMgrNotificationGroup, alaStackMgrStatErrorsTx=alaStackMgrStatErrorsTx, alaStackMgrStatLinkNumber=alaStackMgrStatLinkNumber, alcatelIND1StackMgrMIB=alcatelIND1StackMgrMIB, alaStackMgrRemoteNISlotB=alaStackMgrRemoteNISlotB, alaStackMgrStackStatus=alaStackMgrStackStatus, alaStackMgrStaticRoutePort=alaStackMgrStaticRoutePort, AlaStackMgrCommandStatus=AlaStackMgrCommandStatus, alaStackMgrStatsEntry=alaStackMgrStatsEntry, AlaStackMgrCommandAction=AlaStackMgrCommandAction, AlaStackMgrLinkStatus=AlaStackMgrLinkStatus, alaStackMgrStaticRouteDstEndIf=alaStackMgrStaticRouteDstEndIf, alaStackMgrRemoteNISlotA=alaStackMgrRemoteNISlotA, alaStackMgrStaticRouteSrcStartIf=alaStackMgrStaticRouteSrcStartIf, alaStackMgrCommandStatus=alaStackMgrCommandStatus, alaStackMgrStatsTable=alaStackMgrStatsTable, alaStackMgrTraps=alaStackMgrTraps, alaStackMgrTokensUsed=alaStackMgrTokensUsed, alaStackMgrTokensAvailable=alaStackMgrTokensAvailable, alaStackMgrPrimary=alaStackMgrPrimary, alaStackMgrCommandAction=alaStackMgrCommandAction, alaStackMgrSlotNINumber=alaStackMgrSlotNINumber, AlaStackMgrLinkNumber=AlaStackMgrLinkNumber, alaStackMgrStaticRouteSrcEndIf=alaStackMgrStaticRouteSrcEndIf, alcatelIND1StackMgrTrapObjects=alcatelIND1StackMgrTrapObjects, alaStackMgrRemoteLinkB=alaStackMgrRemoteLinkB, AlaStackMgrStackingMode=AlaStackMgrStackingMode, alaStackMgrChasRole=alaStackMgrChasRole, alaStackMgrSavedSlotNINumber=alaStackMgrSavedSlotNINumber, alaStackMgrOutOfTokensTrap=alaStackMgrOutOfTokensTrap, alaStackMgrStaticRouteTable=alaStackMgrStaticRouteTable, alaStackMgrOperStackingMode=alaStackMgrOperStackingMode, alaStackMgrStaticRouteEntry=alaStackMgrStaticRouteEntry, alaStackMgrStatErrorsRx=alaStackMgrStatErrorsRx, alaStackMgrBadMixTrap=alaStackMgrBadMixTrap, alcatelIND1StackMgrMIBCompliances=alcatelIND1StackMgrMIBCompliances, AlaStackMgrStackStatus=AlaStackMgrStackStatus, alcatelIND1StackMgrMIBGroups=alcatelIND1StackMgrMIBGroups, alaStackMgrChasState=alaStackMgrChasState, alaStackMgrChassisTable=alaStackMgrChassisTable, alaStackMgrSlotCMMNumber=alaStackMgrSlotCMMNumber, alaStackMgrRemoteLinkA=alaStackMgrRemoteLinkA, alaStackMgrLocalLinkStateB=alaStackMgrLocalLinkStateB, alaStackMgrClearedSlotTrap=alaStackMgrClearedSlotTrap, alcatelIND1StackMgrMIBConformance=alcatelIND1StackMgrMIBConformance)
