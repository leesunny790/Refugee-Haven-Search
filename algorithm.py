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
        preferenceFactor = 0
        if (preferVal == 3):
            preferenceFactor = 3
        elif(preferVal == 2):
            preferenceFactor = 2
        else:
            preferenceFactor = 1
        userInputWeighIn = CalculateWeighInTimesBaseVal(country, user, varName)
        
        
#Input
def CalculateWeighInTimesBaseVal(country, user, varName):
    if(varName == "asylumRate"):
        #Arbitrary added at end
    elif(varName == "hdi"):
        #Arbitrary added at end
    elif(varName == )
    
    if(varName == "youthPreferred"):
        if 18 <= user.age <= 45 :
            if country.youthPreferred == 'yes' :
                # Match_Value['country'] +=1
    

    
        #Do logic


#Input:
# - Origin country of the user by name
#Output:
# - None. Sets asylum rate of each country in CountryList
def setAsylumRates(origin):
    #lookup refugee database for each country from the user's data
    #popuplate CountryData information
    for i in range(0, len(CountryList)):
        CountryList[i].asylumRate = 0 #get from database

