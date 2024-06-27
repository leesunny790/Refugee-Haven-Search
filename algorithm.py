import numpy as numpy

class UserData:
    #name, coo, etc..
    name = ""
    originCountry = ""
    age = 0
    userLanguages = np.empty() #main language, other languages
    gender = 0 #0 is male, 1 female, 2 is other
    sexuality = 0 #0 is hetero, 1 is other
    partySize = 0 
    educationLevel = 0 #0 for none, 1 for secondary, 2 for bachelor's, 3 for beyond
    def __init__ (self, n, oC, a, uL, g, s, p, eL, cD, dP):
        self.name = n
        self.originCountry = oC
        self.age = a
        self.userLanguages = uL
        self.gender = g
        self.sexuality = s
        self.partySize = p
        self.educationLevel = eL
        self.cultureDesire = cD #0 for more individualistic, 1 for more collectivist
        self.democracyPreference = dP #Is democracy important to you 1 yes 0 no


class CountryData:
    #CountryName, etc...
    name = ""
    asylumRate = 0.0
    countryLanguages = np.empty() #main language
    genderRatio = 0.0 #closer to 1 for more males, closer to 0 for more females
    unemploymentRate = 0.0
    collectivismValue = 0.0 #smaller is more individualistic, larger is more collectivist
    personalFreedomValue = 0.0 #explains how authoritarian governments are
    hdi = 0.0 #accounts for popuplation-wide education, economy, social development
    youthPreferred = 0 #1 if popuplation is biased old, 0 if not
    supportsDependents = 0 #float or bool?

CountryList = np.empty() # a list of CountryData objects

MatchValues = {} #Dictionary storing [country_name, match_value]

class CountryVariablePreference:
    # asylumRatePrefer = 0
    # countryLanguagesPrefer = 0
    # genderRatioPrefer = 0
    # unemploymentRatePrefer = 0
    # collectivismValuePrefer = 0
    # personalFreedomValuePrefer = 0
    # hdiPrefer = 0
    # youthPreferredPrefer = 0
    # supportsDependentsPrefer = 0
    VariablePreferences = {}
    

#Input:
# - Country information as csv or whatever file format
#Output:
# - No output. It fills the global CountryList array
#Purpose: populate CountryList to be used in the main algorithm
def FillCountryList(countries):
    for i in range(0, len(countries)):
        newCountry = CountryData()
        #do countryData variable assignment here



#Input: 
# - 3xN numpy array containing the ranked lists for each category of importance by name
# - Name (as primary key) of user to do matching on
#Returns: Ranked list of countries that best match the user's preferences and bio
def MainAlgorithm(preferences, name, originCountry, age, 
    userLanguages, gender, sexuality, partySize, educationLevel):
    #1. Go through each item in the ranked lists and assign them an
    #   an importance value based on ranking in bucket and bucket factor
    #2. Match each item with variables in CountryData
    #3. Generate a total match value for each country in CountryList
    #4. Return the best x countries
    
    #Assign preference rating:
    variablePreferences = CountryVariablePreferences()
    for i in range(0, len(preferences[0])):
        myWeight = StupidFunction(len(preferences[0]), i, 5)
        assignPreferences(variablePreferences, preferences[0][i], myWeight)
    for j in range(0, len(preferences[1])):
        myWeight = StupidFunction(len(preferences[0]), i, 3)
        assignPreferences(variablePreferences, preferences[0][j], myWeight)
    for k in range(0, len(preferences[2])):
        myWeight = StupidFunction(len(preferences[0]), i, 1)
        assignPreferences(variablePreferences, preferences[0][k], myWeight)

    variablePreferences.VariablePreferences = dict(sorted(variablePreferences.VariablePreferences.items(), key = lambda item: item[1], reverse=True))
    maxWeight = variablePreference.VariablePreferences.values()[len(variablePreferences.VariablePreferences) - 1]
    minWeight = variablePreference.VariablePreferences.values()[0]
    for i in range(0,len(variablePreferences.VariablePreferences)):
        newVal = (variablePreferences.VariablePreferences.values()[i] - minWeight) / (maxWeight - minWeight)
        variablePreferences.VariablePreferences.values()[i] = newVal

    #REMEMBER THAT THESE PREFERENCE VALUES WILL BE LESS THAN OR EQUAL 1
    #Create user and set asylum rates
    user = UserData(name, originCountry, age, 
            userLanguages, gender, sexuality, partySize, educationLevel)
    setAsylumRates(user.originCountry)

    #Do the actual weightings for each country
    for i in range(0, len(CountryList)):
        SetMatchValues(CountryList[i], user, variablePreferences)
    #By this point MatchValues dictionary is populated

    #Sort countries by match value and return top x
    MatchValues = dict(sorted(MatchValues.items(), key = lambda item: item[1], reverse=True))

    return MatchValues

def StupidFunction(numItems, idx, baseBucketValue):
    if (numItems == 1):
        return baseBucketValue
    elif(numItems == 2):
        if (idx == 0):
            return baseBucketValue + 0.25
        else:
            return baseBucketValue - 0.25
    elif(numItems == 3):
        if (idx == 0):
            return baseBucketValue + 0.25
        elif(idx==1):
            return baseBucketValue
        else:
            return baseBucketValue - 0.25
    elif(numItems == 4):
        if (idx == 0):
            return baseBucketValue + 0.5
        elif(idx == 1):
            return baseBucketValue + 0.25
        elif(idx == 2):
            return basebucketValue - 0.25
        else:
            return baseBucketValue - 0.5
    elif(numItems == 5):
        if (idx == 0):
            return baseBucketValue + 0.5
        elif(idx == 1):
            return baseBucketValue + 0.25
        elif(idx == 2):
            return baseBucketValue
        elif(idx == 3):
            return baseBucketValue - 0.25
        else:
            return baseBucketValue - 0.5
    elif(numItems == 6):
        if (idx == 0):
            return baseBucketValue + 0.75
        elif(idx == 1):
            return baseBucketValue + 0.5
        elif(idx == 2):
            return baseBucketValue + 0.25
        elif(idx == 3):
            return baseBucketValue - 0.25
        elif(idx == 4):
            return baseBucketValue - 0.5
        else:
            return baseBucketValue - 0.25
    else:
        if (idx == 0):
            return baseBucketValue + 0.75
        elif(idx == 1):
            return baseBucketValue + 0.5
        elif(idx == 2):
            return baseBucketValue + 0.25
        elif(idx == 3):
            return baseBucketValue
        elif(idx == 4):
            return baseBucketValue - 0.25
        elif(idx == 5):
            return baseBucketValue - 0.5
        else:
            return baseBucketValue - 0.75


def assignPreference(preferencesObject, varName, preferenceVal):
    if (varName == "asylumRate"):
        preferencesObject.VariablePreferences["asylumRate"] = preferenceVal
    elif(varName == "countryLanguages"):
        preferencesObject.VariablePreferences["countryLanguages"] = preferenceVal
    elif(varName == "genderRatio"):
        preferencesObject.VariablePreferences["genderRatio"] = preferenceVal
    elif(varName == "unemploymentRate"):
        preferencesObject.VariablePreferences["unemploymentRate"] = preferenceVal
    elif(varName == "collectivismValue"):
        preferencesObject.VariablePreferences["collectivismValue"] = preferenceVal
    elif(varName == "personalFreedomValue"):
        preferencesObject.VariablePreferences["personalFreedomValue"] = preferenceVal
    elif(varName == "hdi"):
        preferencesObject.VariablePreferences["hdi"] = preferenceVal
    elif(varName == "youthPreferred"):
        preferencesObject.VariablePreferences["youthPreferred"] = preferenceVal
    else:
        #supports dependents
        preferencesObject.VariablePreferences["supportsDependents"] = preferenceVal


def SetMatchValues(country, user, preferences):
    #Factors:
    # - Prefer value
    # - User provided input weigh-in
    # - Raw value for factor for each country
    for i in range(0, len(preferences.VariablePreferences)):
        currKey = preferences.VariablePreferences.keys()[i]
        preferVal = preferences.VariablePreferences.values()[i]
        
        userInputWeighIn = CalculateWeighInTimesBaseVal(country, user, currKey)

        #Do some math here to factor preferVal into CalculateWeighInTimesBaseVal

        
        
#Input
def CalculateWeighInTimesBaseVal(country, user, varName):
    if(varName == "asylumRate"):
        #Arbitrary added at end
        #count positive if good asylum rate, count negative if not
        #split down middle once calculated
    elif(varName == "hdi"):
        #Arbitrary added at end
        #count very minimally see asylum rate
    elif(varName == "countryLanguages"):
        #from dataset, countryLanguages will be a Dict with key value pair showing percentage pop speaking said langauge
        #userLanguages will just be from the array
        if (country.countryLanguages[0] == user.userLanguages[0]):
            #main languages match count very positively
            return 
        
        totalPopularLanguageMatch = 0.0
        for k, v in country.countryLanguages:
            #key value pairs
            if (k in user.userLanguages):
                #weigh by v or the percentage pop
                totalPopuplarLanguageMatch += 0.0 #CHANGE THIS

        if (totalPopularLanguageMatch == 0.0):
            #count as net negative as the user speaks no languages from this country
                

                
    elif(varName = "genderRatio"):
        #if applicant is male, disregard gender ratio (female dominant countries like Russia are not net positive for male immigrants)
        #if applicant is female, negative if male dominant
        
        #don't weigh this too high due to uncertainty
    elif(varName == "unemploymentRate"):
        #High unemployment is bad
        #if applicant is well educated, decrease detriment due to higher unemployment
    elif(varName == "collectivismValue"):
        #set anchor point of collectivism/individualism at origin country
        #Look at difference between GCI of country we are looking at and GCI of origin country
        #count as positive if more in line with desire
        #count as negative if it goes in the opposite direction
        

    elif(varName == "personalFreedomValue"):
        #Mount anchor of GCI at origin country
        #if the country we are looking at is more in line with value count as positive
        #if the country is less in line with the value count as negative
        #Ex: origin country: russia, current country is France, individual desires more democracy = france's personalFreedomValue is positive
        #ex: origin country Germany, current country is Saudi Arabia, individual desires more democracy = SA's personalFreedomValue is negative
    
    
    elif(varName == "youthPreferred"):
        if (18 <= user.age <= 45) :
            if country.youthPreferred == 'yes' :
                #count positively
        
        #count neutrally otherwise
    
    else:
        #supports dependents
        #All we do for this userinput is check if it's greater than one
        if (user.partySize > 1): 
            if (country.supportsDependents):
                #count positively
            else:
                #count negatively
        else:
            #doesn't matter if traveling alone so count neutrally


    


#Input:
# - Origin country of the user by name
#Output:
# - None. Sets asylum rate of each country in CountryList
def setAsylumRates(origin):
    #lookup refugee database for each country from the user'ss data
    #popuplate CountryData information
    for i in range(0, len(CountryList)):
        CountryList[i].asylumRate = 0 #get from database

