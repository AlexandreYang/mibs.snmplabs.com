#
# PySNMP MIB module FASTPATH-BOXSERVICES-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-BOXSERVICES-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:57:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, ModuleIdentity, Gauge32, MibIdentifier, Integer32, Bits, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "ModuleIdentity", "Gauge32", "MibIdentifier", "Integer32", "Bits", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fastPathBoxServices = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43))
fastPathBoxServices.setRevisions(('2008-02-22 00:00',))
if mibBuilder.loadTexts: fastPathBoxServices.setLastUpdated('200802220000Z')
if mibBuilder.loadTexts: fastPathBoxServices.setOrganization('Broadcom Corporation')
boxServicesGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1))
boxServicesNormalTempRangeMin = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesNormalTempRangeMin.setStatus('current')
boxServicesNormalTempRangeMax = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, 100)).clone(45)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesNormalTempRangeMax.setStatus('current')
boxServicesTemperatureTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesTemperatureTrapEnable.setStatus('current')
boxServicesPSMStateTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesPSMStateTrapEnable.setStatus('current')
boxServicesFanStateTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boxServicesFanStateTrapEnable.setStatus('current')
boxServicesFansTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6), )
if mibBuilder.loadTexts: boxServicesFansTable.setStatus('current')
boxServicesFansEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1), ).setIndexNames((0, "FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"))
if mibBuilder.loadTexts: boxServicesFansEntry.setStatus('current')
boxServicesFansIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFansIndex.setStatus('current')
boxServicesFanItemType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanItemType.setStatus('current')
boxServicesFanItemState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notpresent", 1), ("operational", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanItemState.setStatus('current')
boxServicesFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanSpeed.setStatus('current')
boxServicesFanDutyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 6, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesFanDutyLevel.setStatus('current')
boxServicesPowSuppliesTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7), )
if mibBuilder.loadTexts: boxServicesPowSuppliesTable.setStatus('current')
boxServicesPowSuppliesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1), ).setIndexNames((0, "FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"))
if mibBuilder.loadTexts: boxServicesPowSuppliesEntry.setStatus('current')
boxServicesPowSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyIndex.setStatus('current')
boxServicesPowSupplyItemType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyItemType.setStatus('current')
boxServicesPowSupplyItemState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notpresent", 1), ("operational", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesPowSupplyItemState.setStatus('current')
boxServicesTempSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8), )
if mibBuilder.loadTexts: boxServicesTempSensorsTable.setStatus('obsolete')
boxServicesTempSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1), ).setIndexNames((0, "FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"))
if mibBuilder.loadTexts: boxServicesTempSensorsEntry.setStatus('current')
boxServicesTempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorIndex.setStatus('current')
boxServicesTempSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorType.setStatus('current')
boxServicesTempSensorState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notpresent", 5), ("notoperational", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorState.setStatus('current')
boxServicesTempSensorTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesTempSensorTemperature.setStatus('current')
boxServicesStackTempSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9), )
if mibBuilder.loadTexts: boxServicesStackTempSensorsTable.setStatus('current')
boxServicesStackTempSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1), ).setIndexNames((0, "FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesUnitIndex"), (0, "FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesStackTempSensorIndex"))
if mibBuilder.loadTexts: boxServicesStackTempSensorsEntry.setStatus('current')
boxServicesUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesUnitIndex.setStatus('current')
boxServicesStackTempSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesStackTempSensorIndex.setStatus('current')
boxServicesStackTempSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fixed", 1), ("removable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesStackTempSensorType.setStatus('current')
boxServicesStackTempSensorState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notpresent", 5), ("notoperational", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesStackTempSensorState.setStatus('current')
boxServicesStackTempSensorTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 1, 9, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxServicesStackTempSensorTemperature.setStatus('current')
boxServicesNotificationsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2))
boxsItemStateChangeEvent = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("insertion", 1), ("removal", 2), ("becomeoperational", 3), ("failure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxsItemStateChangeEvent.setStatus('current')
boxsTemperatureChangeEvent = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("abovethreshold", 1), ("belowthreshold", 2), ("withinnormalrange", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boxsTemperatureChangeEvent.setStatus('current')
fastPathBoxServicesTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0))
boxsFanStateChange = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 1)).setObjects(("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesFansIndex"), ("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
if mibBuilder.loadTexts: boxsFanStateChange.setStatus('current')
boxsPowSupplyStateChange = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 2)).setObjects(("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesPowSupplyIndex"), ("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxsItemStateChangeEvent"))
if mibBuilder.loadTexts: boxsPowSupplyStateChange.setStatus('current')
boxsTemperatureChange = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 43, 0, 3)).setObjects(("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxServicesTempSensorIndex"), ("FASTPATH-BOXSERVICES-PRIVATE-MIB", "boxsTemperatureChangeEvent"))
if mibBuilder.loadTexts: boxsTemperatureChange.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-BOXSERVICES-PRIVATE-MIB", boxServicesFanSpeed=boxServicesFanSpeed, boxServicesTempSensorsTable=boxServicesTempSensorsTable, boxsItemStateChangeEvent=boxsItemStateChangeEvent, boxServicesFanItemState=boxServicesFanItemState, boxServicesFansEntry=boxServicesFansEntry, boxServicesStackTempSensorIndex=boxServicesStackTempSensorIndex, boxServicesFanStateTrapEnable=boxServicesFanStateTrapEnable, boxServicesPowSuppliesTable=boxServicesPowSuppliesTable, boxServicesFansTable=boxServicesFansTable, boxServicesPowSuppliesEntry=boxServicesPowSuppliesEntry, boxServicesStackTempSensorState=boxServicesStackTempSensorState, boxServicesNotificationsGroup=boxServicesNotificationsGroup, boxServicesTemperatureTrapEnable=boxServicesTemperatureTrapEnable, boxServicesTempSensorState=boxServicesTempSensorState, boxServicesGroup=boxServicesGroup, fastPathBoxServicesTraps=fastPathBoxServicesTraps, boxServicesStackTempSensorTemperature=boxServicesStackTempSensorTemperature, boxServicesFansIndex=boxServicesFansIndex, boxServicesStackTempSensorType=boxServicesStackTempSensorType, boxsTemperatureChange=boxsTemperatureChange, boxServicesPSMStateTrapEnable=boxServicesPSMStateTrapEnable, boxServicesTempSensorTemperature=boxServicesTempSensorTemperature, boxServicesPowSupplyItemType=boxServicesPowSupplyItemType, boxServicesTempSensorsEntry=boxServicesTempSensorsEntry, boxsTemperatureChangeEvent=boxsTemperatureChangeEvent, PYSNMP_MODULE_ID=fastPathBoxServices, boxServicesTempSensorType=boxServicesTempSensorType, boxServicesStackTempSensorsEntry=boxServicesStackTempSensorsEntry, boxServicesFanItemType=boxServicesFanItemType, boxServicesFanDutyLevel=boxServicesFanDutyLevel, boxServicesTempSensorIndex=boxServicesTempSensorIndex, boxServicesStackTempSensorsTable=boxServicesStackTempSensorsTable, boxsPowSupplyStateChange=boxsPowSupplyStateChange, boxServicesPowSupplyIndex=boxServicesPowSupplyIndex, fastPathBoxServices=fastPathBoxServices, boxServicesUnitIndex=boxServicesUnitIndex, boxServicesPowSupplyItemState=boxServicesPowSupplyItemState, boxServicesNormalTempRangeMax=boxServicesNormalTempRangeMax, boxServicesNormalTempRangeMin=boxServicesNormalTempRangeMin, boxsFanStateChange=boxsFanStateChange)
