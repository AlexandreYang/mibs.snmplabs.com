#
# PySNMP MIB module HP-ICF-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-TC
# Produced by pysmi-0.3.4 at Wed May  1 12:26:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hpicfAdmin, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfAdmin")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, ObjectIdentity, Counter32, iso, Integer32, Bits, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "ObjectIdentity", "Counter32", "iso", "Integer32", "Bits", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 4))
hpicfTextualConventions.setRevisions(('2017-03-22 08:00', '2016-12-07 08:00', '2015-01-30 08:00', '2014-12-09 08:00', '2014-09-06 08:00', '2014-02-04 08:00', '2012-02-22 08:00', '2012-02-17 00:00', '2010-10-12 08:00', '2009-02-10 18:00', '2008-08-19 09:05', '2008-02-04 15:36', '2004-02-18 23:05', '2000-11-03 07:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfTextualConventions.setRevisionsDescriptions(('Added 5GbE-T Type', 'Added qSFP-PLUS-BIDI Type', 'Added fortyGbE-GEN Type', 'Added HpSwitchIfMauTypeListBits for 2.5/5G ports, HpSwitchIfMauAutoNegCapabilityBits, HpSwitchIfMauAutoNegCapAdvertisedBits, HpSwitchIfMauAutoNegCapReceivedBits for 2.5/5/40G ports.', 'Added qSFP-PLUS-SR4, qSFP-PLUS-LR4, qSFP-PLUS-DA1, qSFP-PLUS-eSR4, qSFP-PLUS-DA3, qSFP-PLUS-DA5, qSFP-PLUS-SPLIT-sFP-PLUS-DA1,qSFP-PLUS-SPLIT-sFP-PLUS-DA3, qSFP-PLUS-SPLIT-sFP-PLUS-DA5,sFP-PLUS-AO1, sFP-PLUS-AO2, sFP-PLUS-AO3, sFP-PLUS-AO5,sFP-PLUS-AO7, sFP-PLUS-AO10, sFP-PLUS-AO15, qSFP-PLUS-AO1,qSFP-PLUS-AO2, qSFP-PLUS-AO3, qSFP-PLUS-AO5, qSFP-PLUS-AO7, qSFP-PLUS-AO10,qSFP-PLUS-AO15,qSFP-PLUS-AO20, qSFP-PLUS-SPLIT-sFP-PLUS-AO1, qSFP-PLUS-SPLIT-sFP-PLUS-AO2, qSFP-PLUS-SPLIT-sFP-PLUS-AO3, qSFP-PLUS-SPLIT-sFP-PLUS-AO5, qSFP-PLUS-SPLIT-sFP-PLUS-AO7, qSFP-PLUS-SPLIT-sFP-PLUS-AO10, qSFP-PLUS-SPLIT-sFP-PLUS-AO15 types', 'Added fortyGbE-GEN type', 'Added HpInetCidrRouteState type', 'Added tenGigabitEthernetESP.', 'Added VidList type', 'Added 10GbE-K for 802.3ap (clauses 69-74)', 'Added XFP-SFP+ DAC types for HpSwitchPortType.', 'Added multiple transceiver types.', 'Added gigabitEthernetESP and tenGigabitEthernetCX type for HpSwitchPortType.', 'Initial revision.',))
if mibBuilder.loadTexts: hpicfTextualConventions.setLastUpdated('201703220800Z')
if mibBuilder.loadTexts: hpicfTextualConventions.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfTextualConventions.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfTextualConventions.setDescription('This module contains common textual convention definitions used by various HP ICF MIB modules.')
class ConfigStatus(TextualConvention, Integer32):
    description = "Used to indicate the configuration status for a group of objects. 'active' means that the values of the related objects are currently in use by the device. 'notInService' indicates that the objects have been reconfigured in such a way that the values cannot take effect until after the next reboot of the device. 'notReady' indicates that the objects are not consistent with each other."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3))

class HpSwitchPortType(TextualConvention, Integer32):
    description = 'Used to indicate the type of port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 6, 7, 15, 37, 54, 55, 62, 69, 70, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204))
    namedValues = NamedValues(("other", 1), ("none", 2), ("unknown", 3), ("ethernetCsmacd", 6), ("iso88023Csmacd", 7), ("fddi", 15), ("atm", 37), ("propMultiplexor", 54), ("ieee80212", 55), ("fastEther", 62), ("fastEtherFX", 69), ("fastEtherFX-sfp", 70), ("tenGSFP-SR", 112), ("tenGSFP-LR", 113), ("tenGSFP-ER", 114), ("tenGSFP-LRM", 115), ("tenGSFP-LX4", 116), ("gigabitEthernetSX", 117), ("gigabitEthernetLX", 118), ("gigabitEthernetT", 119), ("gigabitEthernetStk", 120), ("gigabitEthernetLH", 121), ("tenGbE-CX4", 122), ("gigabitEthernetESP", 123), ("tenGbE-SR", 124), ("tenGbE-ER", 125), ("tenGbE-LR", 126), ("gigabitEthernetT-sfp", 127), ("fastEtherGEN", 128), ("gigabitEthernetGEN", 129), ("tenGbE-GEN", 130), ("fastEtherBX-D", 131), ("fastEtherBX-U", 132), ("gigabitEthernetBX-D", 133), ("gigabitEthernetBX-U", 134), ("tenGbE-LRM", 135), ("sFP-PLUS-SR", 136), ("sFP-PLUS-LR", 137), ("sFP-PLUS-LRM", 138), ("sFP-PLUS-DAC", 139), ("sFP-PLUS-DA1", 140), ("sFP-PLUS-DA2", 141), ("sFP-PLUS-DA3", 142), ("sFP-PLUS-DA5", 143), ("sFP-PLUS-DA7", 144), ("sFP-PLUS-DA10", 145), ("sFP-PLUS-DA15", 146), ("sFP-PLUS-DA20", 147), ("tenGbE-T", 148), ("tenGbE-TSH", 149), ("tenGbE-TLH", 150), ("tenGbE-STK", 151), ("xFP-SFP-PLUS-DAC", 152), ("xFP-SFP-PLUS-DA1", 153), ("xFP-SFP-PLUS-DA3", 154), ("xFP-SFP-PLUS-DA5", 155), ("xFP-SFP-PLUS-DA7", 156), ("xFP-SFP-PLUS-DA10", 157), ("tenGbE-K", 158), ("sFP-PLUS-ER", 160), ("sFP-CWDM1470", 161), ("sFP-CWDM1490", 162), ("sFP-CWDM1510", 163), ("sFP-CWDM1530", 164), ("sFP-CWDM1550", 165), ("sFP-CWDM1570", 166), ("sFP-CWDM1590", 167), ("sFP-CWDM1610", 168), ("tenGigabitEthernetESP", 169), ("fourGbE-GEN", 170), ("fortyGbE-GEN", 171), ("qSFP-PLUS-SR4", 172), ("qSFP-PLUS-eSR4", 173), ("qSFP-PLUS-LR4", 174), ("qSFP-PLUS-DA1", 175), ("qSFP-PLUS-DA3", 176), ("qSFP-PLUS-DA5", 177), ("qSFP-PLUS-SPLIT-sFP-PLUS-DA1", 178), ("qSFP-PLUS-SPLIT-sFP-PLUS-DA3", 179), ("qSFP-PLUS-SPLIT-sFP-PLUS-DA5", 180), ("sFP-PLUS-AO1", 181), ("sFP-PLUS-AO2", 182), ("sFP-PLUS-AO3", 183), ("sFP-PLUS-AO5", 184), ("sFP-PLUS-AO7", 185), ("sFP-PLUS-AO10", 186), ("sFP-PLUS-AO15", 187), ("qSFP-PLUS-AO1", 188), ("qSFP-PLUS-AO2", 189), ("qSFP-PLUS-AO3", 190), ("qSFP-PLUS-AO5", 191), ("qSFP-PLUS-AO7", 192), ("qSFP-PLUS-AO10", 193), ("qSFP-PLUS-AO15", 194), ("qSFP-PLUS-AO20", 195), ("qSFP-PLUS-SPLIT-sFP-PLUS-AO1", 196), ("qSFP-PLUS-SPLIT-sFP-PLUS-AO2", 197), ("qSFP-PLUS-SPLIT-sFP-PLUS-AO3", 198), ("qSFP-PLUS-SPLIT-sFP-PLUS-AO5", 199), ("qSFP-PLUS-SPLIT-sFP-PLUS-AO7", 200), ("qSFP-PLUS-SPLIT-sFP-PLUS-AO10", 201), ("qSFP-PLUS-SPLIT-sFP-PLUS-AO15", 202), ("qSFP-PLUS-BIDI", 203), ("fiveGbE-T", 204))

class VidList(TextualConvention, OctetString):
    description = 'Each octet within this value specifies a set of eight VlanIndex (VID), with the first octet specifying VIDs 1 through 8, the second octet specifying VIDs 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered VID, and the least significant bit represents the highest numbered VID. Thus, each VID is represented by a single bit within the value of this object. If that bit has a value of 1 then that VID is included in the set of VIDs; the VID is not included if its bit has a value of 0. This list represents the entire range of VlanIndex values defined in the scope of IEEE 802.1Q.'
    status = 'current'
    displayHint = '512x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(512, 512)
    fixedLength = 512

class HpInetCidrRouteState(TextualConvention, Bits):
    description = 'used for the bitmap for getting the state of the route.'
    status = 'current'
    namedValues = NamedValues(("remote", 0), ("notInstall", 1), ("noAdvise", 2), ("interior", 3), ("exterior", 4), ("delete", 5), ("hidden", 6), ("initial", 7), ("release", 8), ("unused", 9), ("unused2", 10), ("retain", 11), ("unused3", 12), ("gateway", 13), ("reject", 14), ("static", 15), ("blackHole", 16), ("ifSubnetMask", 17), ("unused4", 18), ("suppressed", 19), ("eligibleUnicast", 21), ("eligibleMulticast", 22), ("activeUnicast", 23), ("activeMulticast", 24), ("pendingUnicast", 25), ("pendingMulticast", 26), ("inferiorMed", 27), ("split", 28), ("aggr", 29), ("bgpAggr", 30), ("recurse", 31))

class StpPortRole(TextualConvention, Integer32):
    description = 'Identifies the role played by the port in a given spanning tree. - disabled(1) This port has no role in the spanning-tree topology. - root(2) This port provides the minimum cost path from this bridge to the Root Bridge. - designated(3) This port provides the least cost path from the attached LAN through this bridge to the root bridge. - alternate(4) This port provides connectivity to the root bridge if the current root port failed. - backup(5) This port provides connectivity from the attached LAN to the root bridge if the current designated port failed. - boundary(6) This role is only applicable for MSTP. This port provides connectivity from the MSTP Region to the CIST Root that lies outside the Region.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("disabled", 1), ("root", 2), ("designated", 3), ("alternate", 4), ("backup", 5), ("boundary", 6))

class HpSwitchIfMauTypeListBits(TextualConvention, Bits):
    description = 'MauType for 2.5G, 5G and 40G port speed.'
    status = 'current'
    namedValues = NamedValues(("b2500baseTFD", 79), ("b5000baseTFD", 80), ("b40GbaseeSR4", 81))

class HpSwitchIfMauAutoNegCapabilityBits(TextualConvention, Bits):
    description = 'AutoNegCapBits for 2.5G, 5G and 40G port speeds.'
    status = 'current'
    namedValues = NamedValues(("b40GbaseSR4", 23), ("b40GbaseLR4", 24), ("b2500baseTFD", 25), ("b5000baseTFD", 26), ("b40GbaseeSR4", 27))

class HpSwitchIfMauAutoNegCapAdvertisedBits(TextualConvention, Bits):
    description = 'AutoNegCapBits for 2.5G, 5G and 40G port speeds.'
    status = 'current'
    namedValues = NamedValues(("b40GbaseSR4", 23), ("b40GbaseLR4", 24), ("b2500baseTFD", 25), ("b5000baseTFD", 26), ("b40GbaseeSR4", 27))

class HpSwitchIfMauAutoNegCapReceivedBits(TextualConvention, Bits):
    description = 'AutoNegCapBits for 2.5G, 5G and 40G port speeds.'
    status = 'current'
    namedValues = NamedValues(("b40GbaseSR4", 23), ("b40GbaseLR4", 24), ("b2500baseTFD", 25), ("b5000baseTFD", 26), ("b40GbaseeSR4", 27))

mibBuilder.exportSymbols("HP-ICF-TC", HpSwitchIfMauAutoNegCapAdvertisedBits=HpSwitchIfMauAutoNegCapAdvertisedBits, HpSwitchIfMauAutoNegCapabilityBits=HpSwitchIfMauAutoNegCapabilityBits, VidList=VidList, HpSwitchIfMauAutoNegCapReceivedBits=HpSwitchIfMauAutoNegCapReceivedBits, HpInetCidrRouteState=HpInetCidrRouteState, StpPortRole=StpPortRole, HpSwitchPortType=HpSwitchPortType, PYSNMP_MODULE_ID=hpicfTextualConventions, HpSwitchIfMauTypeListBits=HpSwitchIfMauTypeListBits, hpicfTextualConventions=hpicfTextualConventions, ConfigStatus=ConfigStatus)
