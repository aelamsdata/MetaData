#===============================================================================
# EXTRACTION SCRIPT sft_Ne_std.py
#===============================================================================
'''
eqtime: 60
'''
#Release Ne from Cryo

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Neon Release from Cryo')
        
    #Releasing_Neon
    #Close V14
    close('V14')
    info('Warming Cryo to 80 Kelvin')
    setpoint=80
    set_cryo(setpoint)
    sleep_minutes(8)
    
    info('Confirming setpoint reached')
    while True:
        v = get_cryo_temp('b')
        if v and v < setpoint:
            # cryo temp is less than setpoint. wait 1 second then check again
            sleep(1)
        else:
            info('Cryo Temp setpoint reached. setpoint={}, current={}'.format(setpoint, v))
            # setpoint reached. the current cryo temp is now less than the setpoint
            break
    
    #Close V15, Open V14, Open V16

    close('V15')
    sleep(3)
    open('V14')
#===============================================================================
# POST EQUILIBRATION SCRIPT sft_post_eq_ne.py
#===============================================================================

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Post eq script')
    # stuff to do after equilibration with the ms is enter here
    open('V15')
    
# ========== EOF ==========
   
    
#===============================================================================
# POST MEASUREMENT SCRIPT sft_ne_post_meas.py
#===============================================================================

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Post measurement script | Pumping SFT')
    # stuff to do post measurement
    open('A')
    
    
   # set_cryo(140)
    
# ========== EOF ==========