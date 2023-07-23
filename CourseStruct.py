class CourseStruct:
    def __init__(self, CRN, Start_Time, End_Time, Section_Letter, Status, Subject, Title, Credits, Schedule, Prereqs, Restrictions, Full_Session_Info, Instructor):
        self.CRN = CRN
        self.Start_Time = Start_Time
        self.End_Time = End_Time
        self.Section_Letter = Section_Letter
        self.Status = Status		
        self.Subject = Subject	
        self.Title = Title
        self.Credits = Credits	
        self.Schedule = Schedule	
        self.Prereqs = Prereqs
        self.Restrictions = Restrictions	
        self.Full_Session_Info = Full_Session_Info
        self.Instructor = Instructor

    def __str__(self):
        return f"CRN: {self.CRN}, " \
               f"Start Time: {self.Start_Time}, " \
               f"End Time: {self.End_Time}, " \
               f"Section: {self.Section_Letter}, " \
               f"Status: {self.Status}, " \
               f"Subject: {self.Subject}, " \
               f"Title: {self.Title}, " \
               f"Credits: {self.Credits}, " \
               f"Schedule: {self.Schedule}, " \
               f"Prerequisites: {self.Prereqs}, " \
               f"Restrictions: {self.Restrictions}, " \
               f"Full Session Info: {self.Full_Session_Info}, " \
               f"Instructor: {self.Instructor}"


