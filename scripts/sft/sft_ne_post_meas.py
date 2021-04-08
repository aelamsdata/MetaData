
def sleep_minutes(x):
    sleep(x*60)
    
def main():
    info('Post measurement script | Pumping SFT')
    # stuff to do post measurement
    open('A')
    open('V13')
    set_cryo(140)
    sleep_minutes(10)
    close('V13')
    open('V15')
    
# ========== EOF ==========