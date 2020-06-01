REFDET = 'Cup'
REFISO = 'Ne20'

def main():
    
    
    set_spectrometer_configuration('ne_200')
    info('Debug measurement script')
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
    
    peak_hop(hops=hops, ncycles=6)
    
# ========== EOF ==========
    
    