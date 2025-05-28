import datetime

def run(ecl_state, schedule, report_step, summary_state, actionx_callback):

    current_time = schedule.start + datetime.timedelta(seconds=summary_state.elapsed())
    
    BHP_TOP_C1 = summary_state.well_var("C-1H","WBHP")
    BHP_BOT_C1 = summary_state.well_var("C-1L","WBP")
    DeltaP_C1 = BHP_BOT_C1 - BHP_TOP_C1
    WIR_C1 = summary_state.well_var("C-1L","WWIR")
    
    BHP_TOP_C2 = summary_state.well_var("C-2H","WBHP")
    BHP_BOT_C2 = summary_state.well_var("C-2L","WBP")
    DeltaP_C2 = BHP_BOT_C2 - BHP_TOP_C2
    WIR_C2 = summary_state.well_var("C-2L","WWIR")
    
    BHP_TOP_C3 = summary_state.well_var("C-3H","WBHP")
    BHP_BOT_C3 = summary_state.well_var("C-3L","WBP")
    DeltaP_C3 = BHP_BOT_C3 - BHP_TOP_C3
    WIR_C3 = summary_state.well_var("C-3L","WWIR")
    
    BHP_TOP_C4 = summary_state.well_var("C-4H","WBHP")
    BHP_BOT_C4 = summary_state.well_var("C-4L","WBP")
    DeltaP_C4 = BHP_BOT_C4 - BHP_TOP_C4
    WIR_C4 = summary_state.well_var("C-4L","WWIR")
    
    BHP_TOP_F1 = summary_state.well_var("F-1H","WBHP")
    BHP_BOT_F1 = summary_state.well_var("F-1L","WBP")
    DeltaP_F1 = BHP_BOT_F1 - BHP_TOP_F1
    WIR_F1 = summary_state.well_var("F-1L","WWIR")
    
    BHP_TOP_F2 = summary_state.well_var("F-2H","WBHP")
    BHP_BOT_F2 = summary_state.well_var("F-2L","WBP")
    DeltaP_F2 = BHP_BOT_F2 - BHP_TOP_F2
    WIR_F2 = summary_state.well_var("F-2L","WWIR")
    
    BHP_TOP_F3 = summary_state.well_var("F-3H","WBHP")
    BHP_BOT_F3 = summary_state.well_var("F-3L","WBP")
    DeltaP_F3 = BHP_BOT_F3 - BHP_TOP_F3
    WIR_F3 = summary_state.well_var("F-3L","WWIR")
    
    #initial hydrostatic difference
    limit_C1 = 20 # 10.91
    limit_C2 = 18.97
    limit_C3 = 21.58
    limit_C4 = 17.89
    limit_F1 = 29.23
    limit_F2 = 53.32
    limit_F3 = 17.47
     
    
    if (BHP_TOP_C1 < 310):
        schedule.open_well("C-1H",report_step)
    
    if (BHP_TOP_C2 < 310):
        schedule.open_well("C-2H",report_step)
        
    if (BHP_TOP_C3 < 310):
        schedule.open_well("C-3H",report_step)
    
    if (BHP_TOP_C4 < 310):
        schedule.open_well("C-4H",report_step)
    
    if (BHP_TOP_F1 < 310):
        schedule.open_well("F-1H",report_step)
    
    if (BHP_TOP_F2 < 310):
        schedule.open_well("F-2H",report_step)
        
    if (BHP_TOP_F3 < 310):
        schedule.open_well("F-3H",report_step)

    #SHUT = no cross flow
    #STOP = cross flow 
    
    if (WIR_C1 > 0):
        schedule.shut_well("C-1C",report_step)
    elif (DeltaP_C1 <= limit_C1):
        schedule.shut_well("C-1C",report_step)
    else:
        schedule.stop_well("C-1C",report_step)
    
    if (WIR_C2 > 10):
        schedule.shut_well("C-2C",report_step)
    elif(DeltaP_C2 <= limit_C2):
        schedule.shut_well("C-2C",report_step)
    else:
        schedule.stop_well("C-2C",report_step)
    
    if (WIR_C3 > 10):
        schedule.shut_well("C-3C",report_step)
    elif(DeltaP_C3 <= limit_C3):
        schedule.shut_well("C-3C",report_step)
    else:
        schedule.stop_well("C-3C",report_step)
    
    if (WIR_C4 > 10):
        schedule.shut_well("C-4C",report_step)
    elif (DeltaP_C4 <= limit_C4):
        schedule.shut_well("C-4C",report_step)
    else:
        schedule.stop_well("C-4C",report_step)
    
    if (WIR_F1 > 10):
        schedule.shut_well("F-1C",report_step)
    elif (DeltaP_F1 <= limit_F1):
        schedule.shut_well("F-1C",report_step)
    else:
        schedule.stop_well("F-1C",report_step)
    
    if (WIR_F2 > 10): 
        schedule.shut_well("F-2C",report_step)
    elif (DeltaP_F2 <= limit_F2):
        schedule.shut_well("F-2C",report_step)
    else:
        schedule.stop_well("F-2C",report_step)
    
    if (WIR_F3 > 10): 
        schedule.shut_well("F-3C",report_step)
    elif (DeltaP_F3 <= limit_F3):
        schedule.shut_well("F-3C",report_step)
    else:
        schedule.stop_well("F-3C",report_step)
        
        

   