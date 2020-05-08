#===============================================================================
# EXTRACTION SCRIPT sft_debug.py
#===============================================================================

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Debug extraction script')

    sleep(5)
    
# ========== EOF ==========
    '''
    #Open V15
    open('V15')
    sleep_minutes(2)
    
    
    ### NEW SCRIPT ###
    #Releasing_Neon
    #Close V14
    close('V14')
    set_cryo(80)
    sleep_minutes(8)
    
    #Open_Ion_Getter_Pump
    open(description='MS Ion Pump')
    #timing needs to be checked
    sleep(1*60)
    
    #Close_Ion_Getter_Pump, Close V15, Open V14, Open V16
    close(description='MS Ion Pump')
    close('V15')
    open('V14')
    open('V16')
    sleep_minutes(1)
    #Close V16, Open V15
    close('V16')
    open('V15')
    set_cryo(140)
    
    ### NEW SCRIPTS ###
    #Data_Collection_Neon
    #Open_Ion_Getter_Pump
    
    '''
    
#===============================================================================
# POST EQUILIBRATION SCRIPT sft_post_eq_he.py
#===============================================================================

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Post eq script')
    # stuff to do after equilibration with the ms is enter here
    sleep(5)
    
# ========== EOF ==========

    
#===============================================================================
# POST MEASUREMENT SCRIPT sft_he.py
#===============================================================================

def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Post measurement script')
    # stuff to do post measurement
    open('A')
    
# ========== EOF ==========
 