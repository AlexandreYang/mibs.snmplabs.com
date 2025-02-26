#
# PySNMP MIB module HPN-ICF-DOT11-SA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DOT11-SA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
HpnicfDot11RadioScopeType, HpnicfDot11ObjectIDType, hpnicfDot11, HpnicfDot11ChannelScopeType, HpnicfDot11SaIntfDevType = mibBuilder.importSymbols("HPN-ICF-DOT11-REF-MIB", "HpnicfDot11RadioScopeType", "HpnicfDot11ObjectIDType", "hpnicfDot11", "HpnicfDot11ChannelScopeType", "HpnicfDot11SaIntfDevType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, Gauge32, Counter32, MibIdentifier, Counter64, iso, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Gauge32", "Counter32", "MibIdentifier", "Counter64", "iso", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Unsigned32", "IpAddress")
TruthValue, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention")
hpnicfDot11Sa = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13))
hpnicfDot11Sa.setRevisions(('2011-08-26 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfDot11Sa.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfDot11Sa.setLastUpdated('201108262000Z')
if mibBuilder.loadTexts: hpnicfDot11Sa.setOrganization('')
if mibBuilder.loadTexts: hpnicfDot11Sa.setContactInfo('')
if mibBuilder.loadTexts: hpnicfDot11Sa.setDescription('This MIB module provides spectrum analysis information. The initial revision of this MIB module. The spectrum analysis module on APs is able to examine the radio frequency (RF) environment in which the Wi-Fi network is operating, identify interference and classify its sources. An analysis of the results can then be used to quickly isolate issues with packet transmission, channel quality, and traffic congestion caused by contention with other devices operating in the same band or channel.')
hpnicfDot11SaCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1))
hpnicfDot11SaStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2))
hpnicfDot11SaNotifyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3))
hpnicfDot11SaCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1), )
if mibBuilder.loadTexts: hpnicfDot11SaCfgTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaCfgTable.setDescription('This table is used to configure spectrum analysis.')
hpnicfDot11SaCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaCfgRadioType"))
if mibBuilder.loadTexts: hpnicfDot11SaCfgEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaCfgEntry.setDescription('This entry contains the spectrum analysis configuration.')
hpnicfDot11SaCfgRadioType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dot11bg", 1), ("dot11a", 2))))
if mibBuilder.loadTexts: hpnicfDot11SaCfgRadioType.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaCfgRadioType.setDescription('Represents the radio type of the configuration.')
hpnicfDot11SaEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11SaEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaEnable.setDescription('Represents whether spectrum analysis is enabled globally.')
hpnicfDot11SaRptDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 3), Bits().clone(namedValues=NamedValues(("microwave", 0), ("microwaveInverter", 1), ("bluetooth", 2), ("fixedFreqOthers", 3), ("fixedFreqCordlessPhone", 4), ("fixedFreqVideo", 5), ("fixedFreqAudio", 6), ("freqHopperOthers", 7), ("freqHopperCordlessBase", 8), ("freqHopperCordlessNetwork", 9), ("freqHopperXbox", 10), ("genericInterferer", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11SaRptDevType.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRptDevType.setDescription('Represents which types of interference devices should be reported.')
hpnicfDot11SaTrapDevEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11SaTrapDevEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapDevEnable.setDescription('Represents whether the interference device trap is enabled.')
hpnicfDot11SaTrapDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 5), Bits().clone(namedValues=NamedValues(("microwave", 0), ("microwaveInverter", 1), ("bluetooth", 2), ("fixedFreqOthers", 3), ("fixedFreqCordlessPhone", 4), ("fixedFreqVideo", 5), ("fixedFreqAudio", 6), ("freqHopperOthers", 7), ("freqHopperCordlessBase", 8), ("freqHopperCordlessNetwork", 9), ("freqHopperXbox", 10), ("genericInterferer", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11SaTrapDevType.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapDevType.setDescription('Represents which types of interference device will send traps when the interference device trap is enabled.')
hpnicfDot11SaTrapAQEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11SaTrapAQEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapAQEnable.setDescription('Represents whether the air quality trap is enabled.')
hpnicfDot11SaTrapAQThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11SaTrapAQThreshold.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapAQThreshold.setDescription('Represents the air quality trap threshold. When the air quality is below this value, the air quality trap will be sent.')
hpnicfDot11SaDrivenRRMEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11SaDrivenRRMEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDrivenRRMEnable.setDescription('Configure whether to trigger RRM to run when an access point detects a certain level of interference.')
hpnicfDot11SaDrivenRRMSnt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("low", 1), ("medium", 2), ("high", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11SaDrivenRRMSnt.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDrivenRRMSnt.setDescription('Configure the threshold at which RRM will be triggered. When the interference level for the access point rises above the threshold level, RRM initiates a local dynamic channel assignment (DCA) run and changes the channel of the affected access point radio if possible to improve network performance. Low represents a decreased sensitivity to changes in the environment while high represents an increased sensitivity.')
hpnicfDot11SaRtFFTDataTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1), )
if mibBuilder.loadTexts: hpnicfDot11SaRtFFTDataTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRtFFTDataTable.setDescription('This table contains the real-time FFT data for spectrum analysis.')
hpnicfDot11SaRtFFTDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaAPID"), (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaRadioID"), (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaRtDataGroupID"), (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaFrequency"))
if mibBuilder.loadTexts: hpnicfDot11SaRtFFTDataEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRtFFTDataEntry.setDescription('This entry contains the real-time FFT data for spectrum analysis.')
hpnicfDot11SaAPID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 1), HpnicfDot11ObjectIDType())
if mibBuilder.loadTexts: hpnicfDot11SaAPID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaAPID.setDescription('Represents the serial ID of the AP.')
hpnicfDot11SaRadioID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 2), HpnicfDot11RadioScopeType())
if mibBuilder.loadTexts: hpnicfDot11SaRadioID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRadioID.setDescription('Represents the ID of the radio.')
hpnicfDot11SaRtDataGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 3), Integer32())
if mibBuilder.loadTexts: hpnicfDot11SaRtDataGroupID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRtDataGroupID.setDescription('Represents group ID of the collected data. Maybe the device collects multiple groups of data at the collected interval.')
hpnicfDot11SaFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: hpnicfDot11SaFrequency.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaFrequency.setDescription('Represents the frequency number in 100 Hz.')
hpnicfDot11SaRtFreqPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaRtFreqPower.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRtFreqPower.setDescription('Represents the power of the frequency point.')
hpnicfDot11SaRtFreqMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaRtFreqMaxPower.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRtFreqMaxPower.setDescription('Represents the max power of the frequency point.')
hpnicfDot11SaRtFreqDutyCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaRtFreqDutyCycle.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRtFreqDutyCycle.setDescription('Represents the duty cycle of the frequency point.')
hpnicfDot11SaRtFreqDataSeqNo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaRtFreqDataSeqNo.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaRtFreqDataSeqNo.setDescription('Represents the sequence number of the data.')
hpnicfDot11SaIntfDevTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2), )
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevTable.setDescription('This table contains the information of the interfering devices.')
hpnicfDot11SaIntfDevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaAPID"), (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaRadioID"), (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaDevID"))
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevEntry.setDescription('This entry contains the information of the interfering devices.')
hpnicfDot11SaDevID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfDot11SaDevID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDevID.setDescription('Represents the device identification number that uniquely identified the interfering device.')
hpnicfDot11SaDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 2), HpnicfDot11SaIntfDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaDevType.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDevType.setDescription('Represents type of the interferer.')
hpnicfDot11SaDevSI = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaDevSI.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDevSI.setDescription('Represents severity index of the interfering device. Severity index is calculated, a positive integer between 0 and 100(with 100 being the most severe).')
hpnicfDot11SaDevRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaDevRSSI.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDevRSSI.setDescription('Represents receive signal strength indicator (RSSI) of interfering device.')
hpnicfDot11SaDevDutyCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaDevDutyCycle.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDevDutyCycle.setDescription('Represents proportion of time in percentage during which the interfering device was active.')
hpnicfDot11SaDevAffectedChls = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaDevAffectedChls.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDevAffectedChls.setDescription('Represents channels that the interfering device affects.')
hpnicfDot11SaDevDetectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaDevDetectedTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaDevDetectedTime.setDescription('Represents time at which the interference was detected.')
hpnicfDot11SaAirQualityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3), )
if mibBuilder.loadTexts: hpnicfDot11SaAirQualityTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaAirQualityTable.setDescription('This table contains the air quality of the channels.')
hpnicfDot11SaAirQualityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaAPID"), (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaRadioID"), (0, "HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaChlNum"))
if mibBuilder.loadTexts: hpnicfDot11SaAirQualityEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaAirQualityEntry.setDescription('This entry contains the air quality of the channels.')
hpnicfDot11SaChlNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 1), HpnicfDot11ChannelScopeType())
if mibBuilder.loadTexts: hpnicfDot11SaChlNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaChlNum.setDescription('Represents the radio channel where the air quality is monitored.')
hpnicfDot11SaAvgQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaAvgQuality.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaAvgQuality.setDescription('Represents the average air quality for this radio channel.')
hpnicfDot11SaMinQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaMinQuality.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaMinQuality.setDescription('Represents the minimum air quality for this radio channel.')
hpnicfDot11SaIntfDevNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevNum.setDescription('Represents the number of interferers detected by the radios on the 802.11a/n or 802.11b/g/n radio band.')
hpnicfDot11SaWiFiUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaWiFiUtil.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaWiFiUtil.setDescription('Represents the percentage of the channel currently being used by Wi-Fi devices.')
hpnicfDot11SaNonWiFiUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaNonWiFiUtil.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaNonWiFiUtil.setDescription('Represents the percentage of the channel currently being used by non-Wi-Fi interference.')
hpnicfDot11SaNoiseFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11SaNoiseFloor.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaNoiseFloor.setDescription('Represents current noise floor recorded on the channel.')
hpnicfDot11SaTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0))
hpnicfDot11SaIntfDevDetected = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0, 1)).setObjects(("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapAPID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapRadioID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapDevID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapIntfDevType"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11APTrapDevSI"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapDevRSSI"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11APTrapDevDC"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11APTrapDevChls"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11APTrapDevDctTime"))
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevDetected.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevDetected.setDescription('Interfering device is detected.')
hpnicfDot11SaIntfDevDisappear = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0, 2)).setObjects(("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapAPID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapRadioID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapDevID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapIntfDevType"))
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevDisappear.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaIntfDevDisappear.setDescription('Interfering device disappeared.')
hpnicfDot11SaChlQltLow = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0, 3)).setObjects(("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapAPID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapRadioID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlNum"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlQlt"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlIntfNum"))
if mibBuilder.loadTexts: hpnicfDot11SaChlQltLow.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaChlQltLow.setDescription('The quality of the channel is below the specified threshold.')
hpnicfDot11SaChlQltRecover = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 0, 4)).setObjects(("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapAPID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapRadioID"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlNum"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlQlt"), ("HPN-ICF-DOT11-SA-MIB", "hpnicfDot11SaTrapChlIntfNum"))
if mibBuilder.loadTexts: hpnicfDot11SaChlQltRecover.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaChlQltRecover.setDescription('The quality of the channel recovered from low status.')
hpnicfDot11SaTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1))
hpnicfDot11SaTrapAPID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 1), HpnicfDot11ObjectIDType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11SaTrapAPID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapAPID.setDescription('Represents the identifier of the AP.')
hpnicfDot11SaTrapRadioID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 2), HpnicfDot11RadioScopeType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11SaTrapRadioID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapRadioID.setDescription('Represents the identifier of the radio.')
hpnicfDot11SaTrapDevID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 3), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11SaTrapDevID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapDevID.setDescription('Represents the device identification number that uniquely identified the interfering device.')
hpnicfDot11SaTrapIntfDevType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 4), HpnicfDot11SaIntfDevType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11SaTrapIntfDevType.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapIntfDevType.setDescription('Represents type of the interferer.')
hpnicfDot11APTrapDevSI = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11APTrapDevSI.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APTrapDevSI.setDescription('Represents severity index of the interfering device. Severity index is calculated, a positive integer between 0 and 100(with 100 being the most severe).')
hpnicfDot11SaTrapDevRSSI = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 6), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11SaTrapDevRSSI.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapDevRSSI.setDescription('Represents receive signal strength indicator (RSSI) of interfering device.')
hpnicfDot11APTrapDevDC = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 7), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11APTrapDevDC.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APTrapDevDC.setDescription('Represents proportion of time in percentage during which the interfering device was active.')
hpnicfDot11APTrapDevChls = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 8), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11APTrapDevChls.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APTrapDevChls.setDescription('Represents channels that the interfering device affects.')
hpnicfDot11APTrapDevDctTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 9), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11APTrapDevDctTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11APTrapDevDctTime.setDescription('Represents time at which the interference was detected.')
hpnicfDot11SaTrapChlNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 10), HpnicfDot11ChannelScopeType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11SaTrapChlNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapChlNum.setDescription('Represents the radio channel where the air quality is monitored.')
hpnicfDot11SaTrapChlQlt = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11SaTrapChlQlt.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapChlQlt.setDescription('Represents the quality for this radio channel.')
hpnicfDot11SaTrapChlIntfNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 13, 3, 1, 12), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfDot11SaTrapChlIntfNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfDot11SaTrapChlIntfNum.setDescription('Represents the number of interferers detected by the radios on the 802.11a/n or 802.11b/g/n radio band.')
mibBuilder.exportSymbols("HPN-ICF-DOT11-SA-MIB", hpnicfDot11SaRtFreqPower=hpnicfDot11SaRtFreqPower, hpnicfDot11SaTrapChlNum=hpnicfDot11SaTrapChlNum, hpnicfDot11SaTrapChlIntfNum=hpnicfDot11SaTrapChlIntfNum, hpnicfDot11SaTrapIntfDevType=hpnicfDot11SaTrapIntfDevType, hpnicfDot11SaFrequency=hpnicfDot11SaFrequency, hpnicfDot11SaTrapDevID=hpnicfDot11SaTrapDevID, hpnicfDot11SaRtFFTDataTable=hpnicfDot11SaRtFFTDataTable, hpnicfDot11SaEnable=hpnicfDot11SaEnable, hpnicfDot11SaCfgRadioType=hpnicfDot11SaCfgRadioType, hpnicfDot11SaRtDataGroupID=hpnicfDot11SaRtDataGroupID, hpnicfDot11SaChlQltRecover=hpnicfDot11SaChlQltRecover, hpnicfDot11SaCfgGroup=hpnicfDot11SaCfgGroup, hpnicfDot11SaIntfDevTable=hpnicfDot11SaIntfDevTable, hpnicfDot11SaWiFiUtil=hpnicfDot11SaWiFiUtil, PYSNMP_MODULE_ID=hpnicfDot11Sa, hpnicfDot11SaIntfDevDetected=hpnicfDot11SaIntfDevDetected, hpnicfDot11SaDevSI=hpnicfDot11SaDevSI, hpnicfDot11SaTrapVars=hpnicfDot11SaTrapVars, hpnicfDot11SaTrapAQThreshold=hpnicfDot11SaTrapAQThreshold, hpnicfDot11SaTrapAPID=hpnicfDot11SaTrapAPID, hpnicfDot11SaTrapDevType=hpnicfDot11SaTrapDevType, hpnicfDot11SaDevType=hpnicfDot11SaDevType, hpnicfDot11SaDevID=hpnicfDot11SaDevID, hpnicfDot11SaAPID=hpnicfDot11SaAPID, hpnicfDot11SaDevDetectedTime=hpnicfDot11SaDevDetectedTime, hpnicfDot11SaTrapAQEnable=hpnicfDot11SaTrapAQEnable, hpnicfDot11SaMinQuality=hpnicfDot11SaMinQuality, hpnicfDot11SaAirQualityEntry=hpnicfDot11SaAirQualityEntry, hpnicfDot11APTrapDevChls=hpnicfDot11APTrapDevChls, hpnicfDot11SaTrapChlQlt=hpnicfDot11SaTrapChlQlt, hpnicfDot11SaIntfDevNum=hpnicfDot11SaIntfDevNum, hpnicfDot11SaChlNum=hpnicfDot11SaChlNum, hpnicfDot11SaStatusGroup=hpnicfDot11SaStatusGroup, hpnicfDot11SaTraps=hpnicfDot11SaTraps, hpnicfDot11SaDevRSSI=hpnicfDot11SaDevRSSI, hpnicfDot11SaChlQltLow=hpnicfDot11SaChlQltLow, hpnicfDot11SaNonWiFiUtil=hpnicfDot11SaNonWiFiUtil, hpnicfDot11SaRtFreqMaxPower=hpnicfDot11SaRtFreqMaxPower, hpnicfDot11SaRtFFTDataEntry=hpnicfDot11SaRtFFTDataEntry, hpnicfDot11SaRptDevType=hpnicfDot11SaRptDevType, hpnicfDot11SaRtFreqDataSeqNo=hpnicfDot11SaRtFreqDataSeqNo, hpnicfDot11SaIntfDevEntry=hpnicfDot11SaIntfDevEntry, hpnicfDot11SaDrivenRRMEnable=hpnicfDot11SaDrivenRRMEnable, hpnicfDot11SaRtFreqDutyCycle=hpnicfDot11SaRtFreqDutyCycle, hpnicfDot11SaCfgEntry=hpnicfDot11SaCfgEntry, hpnicfDot11SaTrapDevRSSI=hpnicfDot11SaTrapDevRSSI, hpnicfDot11APTrapDevDC=hpnicfDot11APTrapDevDC, hpnicfDot11SaRadioID=hpnicfDot11SaRadioID, hpnicfDot11SaAvgQuality=hpnicfDot11SaAvgQuality, hpnicfDot11SaTrapDevEnable=hpnicfDot11SaTrapDevEnable, hpnicfDot11SaNoiseFloor=hpnicfDot11SaNoiseFloor, hpnicfDot11SaTrapRadioID=hpnicfDot11SaTrapRadioID, hpnicfDot11SaDevDutyCycle=hpnicfDot11SaDevDutyCycle, hpnicfDot11Sa=hpnicfDot11Sa, hpnicfDot11SaIntfDevDisappear=hpnicfDot11SaIntfDevDisappear, hpnicfDot11SaAirQualityTable=hpnicfDot11SaAirQualityTable, hpnicfDot11APTrapDevSI=hpnicfDot11APTrapDevSI, hpnicfDot11SaNotifyGroup=hpnicfDot11SaNotifyGroup, hpnicfDot11SaDevAffectedChls=hpnicfDot11SaDevAffectedChls, hpnicfDot11SaDrivenRRMSnt=hpnicfDot11SaDrivenRRMSnt, hpnicfDot11APTrapDevDctTime=hpnicfDot11APTrapDevDctTime, hpnicfDot11SaCfgTable=hpnicfDot11SaCfgTable)
