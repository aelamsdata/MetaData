def main():
    
    #Enable SEM
    raw_spectrometer_command('SetParameter ESA pos. Set, 528.6')
    raw_spectrometer_command('SetParameter ESA neg. Set, 528.6')
    raw_spectrometer_command('SetParameter CDD Supply Set, 1950.6')
    raw_spectrometer_command('SetParameter HV to ESA Factor Set, 117.5001')
    raw_spectrometer_command('SetParameter HV to ESA Offset Set, 0.002')
    
    sleep(60)
    
    #Protect SEM
    raw_spectrometer_command('SetParameter ESA pos. Set, 0')
    raw_spectrometer_command('SetParameter ESA neg. Set, 0')
    raw_spectrometer_command('SetParameter CDD Supply Set, 0')
    raw_spectrometer_command('SetParameter HV to ESA Factor Set, 117.5001')
    raw_spectrometer_command('SetParameter HV to ESA Offset Set, 0.002')
    
# ========== EOF ==========
    
    