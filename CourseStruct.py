class Course:
    def __init__(self, CRN, start_time, end_time, section_letter):
        self.crn = CRN
        self.start_time = start_time
        self.end_time = end_time
        self.section_letter = section_letter

    def __str__(self):
        return f"CRN: {self.crn}, Start Time: {self.start_time}, End Time: {self.end_time}, Section: {self.section_letter}"


