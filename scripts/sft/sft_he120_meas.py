REFDET = 'Cup'
REFISO = 'He4'
NCOUNTS = 100
#changed 960 to 100 for testing

def main():
    
    #Enable SEM
    raw_spectrometer_command('SetParameter ESA pos. Set, 528.6')
    raw_spectrometer_command('SetParameter ESA neg. Set, 528.6')
    raw_spectrometer_command('SetParameter CDD Supply Set, 1950.6')
    
    set_spectrometer_configuration('he_400')
    info('Debug measurement script')
    activate_detectors('Cup', 'SEM')
    position_magnet(REFISO, REFDET)
    
    # lets gas into ms.  doesn't block, returns immediately after inlet valve opens. delay 3 seconds after ion pump valve is told to close before opening inlet
    equilibrate(eqtime, inlet='V16', outlet='A', delay=3)
    set_time_zero()
    
    # record the gas being inlet
    # eqtime is a special variable, when the analysis is running pychron will set eqtime to the value set by the extraction script
    sniff(eqtime)
    
    peak_center(detector=REFDET, isotope=REFISO)
    
    set_fits()
    multicollect(ncounts=NCOUNTS)
    
    #Protect SEM
    raw_spectrometer_command('SetParameter ESA pos. Set, 0')
    raw_spectrometer_command('SetParameter ESA neg. Set, 0')
    raw_spectrometer_command('SetParameter CDD Supply Set, 0')
    position_magnet('Ne22', detector='Cup', for_collection=False)

# ========== EOF ==========
    
    