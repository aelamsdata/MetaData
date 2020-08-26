def main():
    
    #Open SEM
    raw_spectrometer_command('SetParameter ESA pos. Set, 528.6')
    raw_spectrometer_command('SetParameter ESA neg. Set, 528.6')
    raw_spectrometer_command('SetParameter CDD Supply Set, 1950.6')
    
    
    sleep(20)
    
    #Protect SEM
    raw_spectrometer_command('SetParameter ESA pos. Set, 0')
    raw_spectrometer_command('SetParameter ESA neg. Set, 0')
    raw_spectrometer_command('SetParameter CDD Supply Set, 0')
    
# ========== EOF ==========
    
    