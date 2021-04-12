#===============================================================================
# EXTRACTION SCRIPT sft_debug.py
#===============================================================================

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Debug extraction script')
    
    pressure = store_manometer_pressure()
    info('Baraton pressure={}'.format(pressure))
    
    sleep(5)
    
# ========== EOF ==========

    
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
# POST MEASUREMENT SCRIPT sft_post_meas_DEBUG.py
#===============================================================================
def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Debug')
    # stuff to do post measurement
   
    
# ========== EOF ==========
 