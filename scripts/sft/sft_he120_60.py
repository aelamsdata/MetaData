EQTIME = 10
REFDET = 'Cup'
REFISO = 'He4'
NCOUNTS = 120
BASELINE_NCOUNTS = 60

def main():
    info('Debug measurement script')
    activate_detectors('Cup', 'SEM')
    position_magnet(REFISO, REFDET)
    equilibrate(EQTIME, inlet='V16', outlet='A', )
    
    set_time_zero()
    sniff(EQTIME)
    set_fits()
    multicollect(ncounts=NCOUNTS)
    
    
    #baselines(ncounts=BASELINE_NCOUNTS, detector=REFDET, mass=3.1)
    
# ========== EOF ==========
    
    