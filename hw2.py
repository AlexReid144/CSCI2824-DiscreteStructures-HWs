#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD

class LogicProgramming():
    def classDirectory(self,instructor, student, teaches):
        prof = ""
        stud = "" 
        p = 0 
        s = 0 
        for key in teaches:
            prof = key 
            stud = teaches.values() 
        for item in instructor:
            if prof == key:
                p = item
        for item in student: 
            if stud == key:
                s = item 
        if p != 0 and s != 0: 
            vals = list(s.values())
            for x in vals:
                if  x == p.values(): 
                    return True 
        return False