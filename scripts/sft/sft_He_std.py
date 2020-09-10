#===============================================================================
# EXTRACTION SCRIPT sft_He_std.py
#===============================================================================
'''
eqtime: 60
'''
#Set prep line for He/Ne Air Stnd
def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Test Air Standard Run')
    info('Setting cryo to 120 Kelvin')
    set_cryo(120)
    
    info('Filling 100ul pipette')
    open('V5')
    info('Equilibrating | 1 minute')
    sleep_minutes(1)
    
    pressure = store_manometer_pressure()
    info('Baraton pressure={}'.format(pressure))
    close('V5')
    
    #Close V8; Close V1-12
    close('V8')
    close('V112')
    sleep(10)
    
    #Open V6
    open('V6')
    info('Equilibrating | 1 minute')
    sleep_minutes(1)
    #Close V6
    close('V6')
    #acquire(Convec_Gauge_Value) #not critical, this is just a check.
    
    info('Freezing condensables - N2, O2, Ar, CO2, etc')
    #open V8
    open('V8')
    info('Equilibrating | 6 minutes')
    sleep_minutes(6)
    #close V11; Close V12
    close('V11')
    close('V12')
    sleep(3)
    
    info('Gettering')
    #Open V10
    open('V10')
    info('Equilibrating | 6 minutes')
    sleep_minutes(6)
    
    #Close V15; Open V14
    close('V15')
    open('V14')
    sleep(3)
    #Open V13
    open('V13')
    
    #Freezing_Helium
    setpoint = 5
    
    info('Freezing Helium onto Cryo | 12 minutes')
    set_cryo(setpoint)
    sleep_minutes(12)
    #Check to ensure temp is reached
    
    info('Confirming setpoint reached')
    while True:
        v = get_cryo_temp('b')
        if v > 8:
            # cryo temp is greater than setpoint. wait 1 second then check again
            sleep(1)
        else:
            info('Cryo Temp setpoint reached. setpoint={}, current={}'.format(setpoint, v))
            # setpoint reached. the current cryo temp is now less than the setpoint
            break
    
    info('Setpoint reached - Cleaning Cryo Pump | 1 minute')
    #Close V13; Open V15
    close('V13')
    open('V15')
    sleep(2)
    
    info('Cleaning line')
    #Close V10, Open V12, Open V11, Open V1-12
    close('V10')
    open('V12')
    open('V11')
    open('V112')
    sleep_minutes(1)
    
    info('Releasing Helium from Cryo | 5 minutes')
    #Releasing_Helium
    #Close V14
    close('V14')
    sleep(1)
    set_cryo(30)
    sleep_minutes(5)
    
    #Close V15
    close('V15')
    sleep(3)
    #Open V14
    open('V14')
    sleep_minutes(1)     
#===============================================================================
# POST EQUILIBRATION SCRIPT sft_post_eq_he.py
#===============================================================================

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Post eq script')
    # stuff to do after equilibration with the ms is enter here
    # Clean out S.9 + Cryo
    open('V15')
    
    
# ========== EOF ==========

    
#===============================================================================
# POST MEASUREMENT SCRIPT sft_he_post_meas.py
#===============================================================================

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Post measurement script | Pumping SFT')
    # stuff to do post measurement
                
    open('A')
    
# ========== EOF ==========
 