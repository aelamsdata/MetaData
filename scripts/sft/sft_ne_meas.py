REFDET = 'Cup'
REFISO = 'Ne20'

def main():
    
    #Source Settings. Trap current remains in ne_200.cfg
    raw_spectrometer_command('SetParameter Ion Repeller Set, -4.92')
    raw_spectrometer_command('SetParameter Electron Energy Set, 93.43')
    
    #Source Optics. Y-symmetry is assumed to be horizontal symmetry.
    raw_spectrometer_command('SetParameter Y-Symmetry Set, -6.99')
    raw_spectrometer_command('SetParameter Z-Symmetry Set, -2.96')
    raw_spectrometer_command('SetParameter Z-Focus Set, 36.16')
    raw_spectrometer_command('SetParameter Extraction Lens Set, 38.37')
    
    #Protect SEM
    raw_spectrometer_command('SetParameter ESA pos. Set, 0')
    raw_spectrometer_command('SetParameter ESA neg. Set, 0')
    raw_spectrometer_command('SetParameter CDD Supply Set, 0')
    
    set_spectrometer_configuration('ne_200')
    info('Ne Counting')
    activate_detectors('Cup')
    # position_magnet(REFISO, REFDET)
    
    
    hops = load_hops('hops/ne.yaml')
    define_hops(hops)
    
    
    # lets gas into ms.  doesn't block, returns immediately after inlet valve opens
    equilibrate(eqtime, inlet='V16', outlet='A', delay=3)
    set_time_zero()
    
    # record the gas being inlet
    # eqtime is a special variable, when the analysis is running pychron will set eqtime to the value set by the extraction script
    #sniff(eqtime)
    # potentially a bug doing a sniff with peak hop. just sleep for eqtime instead for now
    sleep(eqtime)
    
    peak_center(detector=REFDET, isotope=REFISO)
    
    set_fits()
    
    peak_hop(hops=hops, ncycles=8)
    
    position_magnet('Ne22', detector='Cup', for_collection=False)
    
# ========== EOF ==========