class Stopbutton :
        def __init__(self,time_label):
            self.time_label = time_label
    
        def stop_function(self,count_id):
            if count_id:
                self.time_label.after_cancel(count_id)
                count_id = None