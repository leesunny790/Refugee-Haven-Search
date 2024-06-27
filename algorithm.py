import numpy as np

def main():
    print("Hello world")

class UserData:
    #name, coo, etc..
    # name = ""
    # originCountry = ""
    # age = 0
    # userLanguages = np.empty() #main language, other languages
    # gender = 0 #0 is male, 1 female, 2 is other
    # sexuality = 0 #0 is hetero, 1 is other
    # partySize = 0 
    # educationLevel = 0 
    def __init__ (self, n, oC, a, uL, g, s, p, eL, cD, dP):
        self.name = n
        self.originCountry = oC
        self.age = a
        self.userLanguages = uL
        self.gender = g
        self.sexuality = s
        self.partySize = p
        self.educationLevel = eL #0 for none, 1 for secondary, 2 for bachelor's, 3 for beyond
        self.cultureDesire = cD #0 for more individualistic, 1 for more collectivist
        self.democracyPreference = dP #Is democracy important to you 1 yes 0 no


class CountryData:
    #CountryName, etc...
    def __init__ (self, n, aR, cL, gR, uR, cV, pFV, hdi, yP, sD):
        self.name = n
        self.asylumRate = aR
        self.countryLanguages = cL #main language
        self.genderRatio = gR #closer to 1 for more males, closer to 0 for more females
        self.unemploymentRate = uR
        self.collectivismValue = cV #1 is collectivist, 0 is individualistic
        self.personalFreedomValue = pFV #explains how authoritarian governments are
        self.hdi = hdi #accounts for popuplation-wide education, economy, social development
        self.youthPreferred = yP#1 if popuplation is biased old, 0 if not
        self.supportsDependents = sD #float or bool?
    

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
def FillCountryList():
    #given origin country fill ar
    AusLang = ["english","mandarin", "arabic"]
    Ausasylum = 0.0
    Aus = CountryData("australia", Ausasylum, AusLang, 98.6, 4, 0, 1, 0.951, 0,0)
    CountryList = np.append(CountryList, Aus)
    BrzLang = ["portuguese", "spanish", "english"]
    Brzasylum = 0.0
    Brz = CountryData("brazil", Brzasylum, BrzLang, 96.6, 7.5, 1, 1, 0.754, 1, 1)
    CountryList = np.append(CountryList, Brz)
    CanLang = ["english", "french", "punjabi"]
    Canasylum = 0.0
    Can = CountryData("canada", Canasylum, CanLang, 98.8, 6.2, 0, 1, 0.929, 1, 1)
    CountryList = np.append(CountryList, Can)
    ChiLang = ["mandarin", "cantonese", "shanghainese"]
    Chiasylum = 0.0
    Chi = CountryData("china", Chiasylum, ChiLang, 104.3, 5.0, 0, 0, 0.768, 0, 1)
    CountryList = np.append(CountryList, Chi)
    FraLang = ["french", "arabic", "portuguese"]
    Fraasylum = 0.0
    Fra = CountryData("france", Fraasylum, FraLang, 93.6, 7.5, 0, 1, 0.901, 1, 1)
    CountryList = np.append(CountryList, Fra)
    GerLang = ["german", "turkish", "arabic"]
    Gerasylum = 0.0
    Ger = CountryData("germany", Gerasylum, GerLang, 97.4, 5.9, 0, 1, 0.95, 1, 1)
    CountryList = np.append(CountryList, Ger)
    ItaLang = ["italian", "english", "german"]
    Itaasylum = 0.0
    Ita = CountryData("italian", Itaasylum, ItaLang, 95.1, 8.2, 1, 1, 0.892, 1, 1)
    CountryList = np.append(CountryList, Ita)
    JapaLang = ["japanese", "ryukyuan", "ainu"]
    Japaasylum = 0.0
    Japa = CountryData("japan", Japaasylum, JapaLang, 94.6, 2.6, 0, 1, 0.915, 1, 0)
    CountryList = np.append(CountryList, Jap)
    NetLang = ["dutch", "frisian", "turkish"]
    Netasylum = 0.0
    Net = CountryData("netherlands", Netasylum, NetLang, 98.8, 3.6, 0, 1, 0.944, 1, 1)
    CountryList = np.append(CountryList, Net)
    NZLang = ["english", "maori", "samoan"]
    NZasylum = 0.0
    NZ = CountryData("new_zealand", NZasylum, NZLang, 98.3, 4.3, 0, 1, 0.931, 0, 1)
    CountryList = np.append(CountryList, NZ)
    RusLang = ["russian", "tatar", "ukrainian"]
    Rusasylum = 0.0
    Rus = CountryData("russia", Rusasylum, RusLang, 86.7, 2.7, 1, 0, 0.822, 0, 0)
    CountryList = np.append(CountryList, Rus)
    SALang = ["arabic", "english", "urdu"]
    SAasylum = 0.0
    SA = CountryData("saudi_arabia", SAasylum, SALang, 136.8, 4.4, 1, 0, 0.854, 0, 0)
    CountryList = np.append(CountryList, SA)
    SinLang = ["english", "mandarin", "malay"]
    Sinasylum = 0.0
    Sin = CountryData("singapore", Sinasylum, SinLang, 109.7, 2.1, 1, 1, 0.939, 1, 1)
    CountryList = np.append(CountryList, Sin)
    UsaLang = ["english","spanish",'chinese']
    Usaasylum = 0.0
    Usa = CountryData("united_states", Usaasylum, UsaLang, 98.2,4,0,1,0.927,0,1)
    CountryList = np.append(CountryList, Usa)
    UkLang = ["english","polish","punjabi"]
    Ukasylum = 0.0
    Uk = CountryData("united_kingdom", Ukasylum, UkLang, 97.6,4.4,0,1,0.932,1,1)
    CountryList = np.append(CountryList, Uk)
    UaeLang = ["arabic","english","Hindi"]
    Uaeasuylum = 0.0
    Uae = CountryData("united_arab_emirates", Uaeasuylum, UaeLang, 228.2,4.4,1,0,0.89,0,0)
    CountryList = np.append(CountryList, Uae)
    TurLang = ["turkish","kurdish","arabic"]
    Turasylum = 0.0
    Tur = CountryData("turkey", Turasylum, TurLang, 100.5,8.5,1,1,0.838,0,1)
    CountryList = np.append(CountryList, Tur)
    SwiLang = ["german","french","italian"]
    Swiasylum = 0.0
    Swi = CountryData("switzerland", Swiasylum, SwiLang, 101.5,2.3,0,1,0.955,0,1)
    CountryList = np.append(CountryList, Swi)
    SweLang = ["swedish","finnish","arabic"]
    Sweasylum = 0.0
    Swe = CountryData("sweden", Sweasylum, SweLang, 98.6,7.8,0,1,0.945,1,1)
    CountryList = np.append(CountryList, Swe)
    SpaLang = ["spanish","catalan","galician"]
    Spaasylum = 0.0
    Spa = CountryData("spain", Spaasylum, SpaLang, 96.1,12.29,1,1,0.904,1,1)
    CountryList = np.append(CountryList, Spa)
    SokLang = ["korean","english","chinese"]
    Sokasylum = 0.0
    Sok = CountryData("south_korea", Sokasylum, SokLang, 99.8,2.8,1,1,0.925,0,0)
    CountryList = np.append(CountryList, Sok)
    SoA = ["zulu","xhosa","afrikaans"]
    Soasylum = 0.0
    So = CountryData("south_africa", Soasylum, SoA, 94.70,32.9,1,1,0.713,0,0)
    CountryList = np.append(CountryList, So)



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
    FillCountryList() #Lol
    #Assign preference rating:
    variablePreferences = CountryVariablePreference()
    for i in range(0, len(preferences[0])):
        myWeight = StupidFunction(len(preferences[0]), i, 5)
        assignPreference(variablePreferences, preferences[0][i], myWeight)
    for j in range(0, len(preferences[1])):
        myWeight = StupidFunction(len(preferences[0]), i, 3)
        assignPreference(variablePreferences, preferences[0][j], myWeight)
    for k in range(0, len(preferences[2])):
        myWeight = StupidFunction(len(preferences[0]), i, 1)
        assignPreference(variablePreferences, preferences[0][k], myWeight)

    variablePreferences.VariablePreferences = dict(sorted(variablePreferences.VariablePreferences.items(), key = lambda item: item[1], reverse=True))
    maxWeight = variablePreferences.VariablePreferences.values()[len(variablePreferences.VariablePreferences) - 1]
    minWeight = variablePreferences.VariablePreferences.values()[0]
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
            return baseBucketValue - 0.25
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
    myMatchVal = 0.0
    for i in range(0, len(preferences.VariablePreferences)):
        currKey = preferences.VariablePreferences.keys()[i]
        preferVal = preferences.VariablePreferences.values()[i]
        
        myMatchVal += CalculateWeighInTimesBaseVal(country, user, currKey)

        #Do some math here to factor preferVal into CalculateWeighInTimesBaseVal
    MatchValues[country.name] = myMatchVal
        
        
#Input
def CalculateWeighInTimesBaseVal(country, user, varName, prefVal):
    if varName == "asylumRate":
        #Arbitrary added at end
        #count positive if good asylum rate, count negative if not
        #split down middle once calculated
        return 0
    elif varName == "hdi":
        #Arbitrary added at end
        #count very minimally see asylum rate
        return country.hdi * prefVal
    elif varName == "countryLanguages":
        #from dataset, countryLanguages will be a Dict with key value pair showing percentage pop speaking said langauge
        #userLanguages will just be from the array      
        totalPopularLanguageMatch = 0.0
        for k in country.countryLanguages:
            #key value pairs
            if k in user.userLanguages:
                #weigh by v or the percentage pop
                totalPopularLanguageMatch += 0.5 #CHANGE THIS

        if totalPopularLanguageMatch == 0.0:
            #count as net negative as the user speaks no languages from this country
            return -0.5 * prefVal
        else:
            return totalPopularLanguageMatch * prefVal
                
    elif varName == "genderRatio":
        #if applicant is female, negative if male dominant
        
        #don't weigh this too high due to uncertainty
        if (user.gender == 1 and country.genderRatio > 100):
            return -1 * prefVal
    elif varName == "unemploymentRate":
        #High unemployment is bad
        #if applicant is well educated, decrease detriment due to higher unemployment
        if (country.unemploymentRate >= 4.5):
            #consider high unemployment
            if (user.educationLevel >= 2):
                return -0.5 * prefVal
            else:
                return -1 * prefVal
    elif varName == "collectivismValue":
        #set anchor point of collectivism/individualism at origin country
        #Look at difference between GCI of country we are looking at and GCI of origin country
        #count as positive if more in line with desire
        #count as negative if it goes in the opposite direction
        if (country.collectivismValue == user.cultureDesire):
            return 1 * prefVal
        else:
            return -0.5 * prefVal

    elif varName == "personalFreedomValue":
        #Mount anchor of GCI at origin country
        #if the country we are looking at is more in line with value count as positive
        #if the country is less in line with the value count as negative
        #Ex: origin country: russia, current country is France, individual desires more democracy = france's personalFreedomValue is positive
        #ex: origin country Germany, current country is Saudi Arabia, individual desires more democracy = SA's personalFreedomValue is negative
        if (country.personalFreedomValue == user.democracyPreference):
            return 1 * prefVal 
        else:
            return -0.5 * prefVal
    
    elif varName == "youthPreferred":
        if 18 <= user.age <= 45 :
            if country.youthPreferred == 'yes' :
                #count positively
                return 1 * preferVal
        
        return 0
        #count neutrally otherwise
    
    else:
        #supports dependents
        #All we do for this userinput is check if it's greater than one
        if user.partySize > 1: 
            if country.supportsDependents:
                #count positively
                return 1 * prefVal
            else:
                #count negatively
                return -0.5 * prefVal
        else:
            #doesn't matter if traveling alone so count neutrally
            return 0


#Input:
# - Origin country of the user by name
#Output:
# - None. Sets asylum rate of each country in CountryList
# def setAsylumRates(origin, destination):
#     #lookup refugee database for each country from the user'ss data
#     #popuplate CountryData information
#     for i in range(0, len(CountryList)):
#         CountryList[i].asylumRate = 0 #get from database

