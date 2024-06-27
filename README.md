# Refugee Haven Search

## Introduction :

Refugee Haven Search is a resource that helps refugees find a home across the globe.

This is a working prototype of matching the refugees to a host country based on their needs, background and preferences to a safer home in future.

**Homes powered by Data** :

This is a standard workflow of the product supported by a TypeScript Dashboard – Flask Backend framework :

1. The website requests for preferences as input from a refugee.
2. The refugee-match algorithm requests the refugee for their order of preference for the above variables by dividing them in three categories : Very Important, Somewhat Important, Not Important.
3. Next, the algorithm makes use of our Final_hacks.csv dataset for the host countries (i.e. countries that migrants most likely migrate to) which acts like a lookup table consisting following variables of interest :

- AsylumRate based on refugee’s country of origin
- Languages based on refugee’s preferred languages and the ones spoken in host countries.
- Gender Ratio considering the female to male population quotient in host countries
- Unemployment rate and Youth Preferred (considering labor shortages) in host countries which conveys their willingness to hire employable young refugees.
- Culture Desire value to match refugees with collectivist or individualistic societies.
- Personal Freedom preferred by the refugees by considering the democracy index of host countries.
- Willingness of host countries to accept refugees with dependents based on their foreign policies.
- Human Development Index of host countries to vouch for the overall standard of living.

4. The algorithm tries to normalize the refugee preferences and assign match values for every host country based on Final_Hacks.csv and refugee input.
5. Lastly, the algorithm suggests host countries with relatively high probability to accept the refugees.
