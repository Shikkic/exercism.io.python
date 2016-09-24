
class Clock():

    # Set initial Clock state
    def __init__(self, hours, minutes):
        timeDic = self.calculateMinutes(minutes) 
        self.minutes = timeDic['minutes'] 
        self.hours = self.calculateHour(hours + timeDic['hours'])
        self.time = self.generateTimeString()

    # Add minutes to the clock (Can be positive or subtracting)
    def add(self, numMinutes=0):
        timeDic = self.calculateMinutes(self.minutes + numMinutes)
        self.setMinutes(timeDic['minutes']) 

        hours = self.calculateHour(self.hours + timeDic['hours']) 
        self.setHours(hours)

        self.time = self.generateTimeString()

        return self.time 
         
    # Calculate Clock Hour in '24' from num of hours (Positive or Negative)
    def calculateHour(self, numHours=0):
        if numHours >= 0 and numHours < 24:
            return numHours

        hours = abs(numHours % 24)

        return hours

    # Caluclate Clock Minutes from num of minutes (Positive or Negative)
    # returns a dict of hours and minutes
    def calculateMinutes(self, numMinutes=0):
        if numMinutes >= 0 and numMinutes < 60:
            return { 'hours': 0, 'minutes': numMinutes }  

        hours = (numMinutes / 60)
        minutes = (numMinutes % 60)
        if minutes == 60:
            minutes = 0
            hours = hours + 1

        return { 'hours': hours, 'minutes': minutes }
  
    # Generates time string from hours and minutes        
    def generateTimeString(self):
        hourDigit = str(self.hours)
        if len(hourDigit) < 2:
            hourDigit = '%d%s' % (0, hourDigit)
       
        minuteDigit = str(self.minutes) 
        if len(minuteDigit) < 2:
            minuteDigit = '%d%s' % (0, minuteDigit)

        return '%s:%s' % (hourDigit, minuteDigit)

    # ToString overide for instance
    def __str__(self):
        return self.time

    # Equality overide for instance
    def __eq__(self, other): 
        return self.time == other.time

    # Setter for hours
    def setHours(self, hours):
        self.hours = hours

    # Setter for minutes
    def setMinutes(self, minutes):
        self.minutes = minutes

    
