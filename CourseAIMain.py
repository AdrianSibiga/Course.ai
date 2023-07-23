import CourseStruct
import requests
import BeautifulSoup


def Main():
    #semester = get_user_semester()
    #courseList = get_user_desired_courses()
    WebSesison = login_to_website()


def login_to_website():
    # Implement the login functionality here using 'requests' library
    # For example:
    login_url = 'https://cufed.carleton.ca/adfs/ls/?wa=wsignin1.0&wtrealm=urn:cas:cas5prod'
    data = {'username': 'adriansibiga', 'password': 'ADRIAN PASSWORD'}  # TO DO: adrian to insert his password for testing
    session = requests.Session()
    response = session.post(login_url, data=data)
    print(response)
    return session


def get_user_semester():
    print("For which semester are you building? ") 
    userSelectedSemeter = input("Summer, Fall, or Winter: ")
    return userSelectedSemeter

def get_user_desired_courses():
    ProvidedCoursesList = []
    
    while len(ProvidedCoursesList) < 1:
        # Create an instance of an course object called aCourse from the course class and 
        # update its attriubtes with the provided user inputs
        userCRN = input("Provide the CRN of you class you wish to take: ")
        userStartTime = input("Start time for CRN " + userCRN + ": ")
        userEndTime = input("End time for CRN " + userCRN + ": ")
        userSectionLetter = input("Section Letter for CRN " + userCRN + ": ")

        # Call constructor
        aCourse = CourseStruct.CourseStruct(userCRN, userStartTime, userEndTime, userSectionLetter)

        # Add to list
        ProvidedCoursesList.append(aCourse)
    return ProvidedCoursesList



Main()
    


