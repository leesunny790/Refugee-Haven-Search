'use client';

import React, { useState } from 'react';
import {
  Progress,
  Box,
  ButtonGroup,
  Button,
  Heading,
  Flex,
  FormControl,
  GridItem,
  FormLabel,
  Input,
  Select,
  SimpleGrid,
  InputLeftAddon,
  InputGroup,
  Textarea,
  FormHelperText,
  InputRightElement,
  Image,
  Text,
  Checkbox,
  CheckboxGroup,
} from '@chakra-ui/react';

import { useToast } from '@chakra-ui/react';
import { Helmet } from 'react-helmet';
import { Link } from 'react-router-dom';

interface FormProps {
    formData: {
      originCountry: string;
      age: string;
      // languages: string[];
      gender: string;
      sexuality: string;
      partySize: string;
      highestEducationLevel: string;
      democracyDesire: string;
      cultureDesire: string;
    };
    setFormData: React.Dispatch<React.SetStateAction<{
      originCountry: string;
      age: string;
      // languages: string[];
      gender: string;
      sexuality: string;
      partySize: string;
      highestEducationLevel: string;
      democracyDesire: string;
      cultureDesire: string;
    }>>;
}

const Form1: React.FC<FormProps> = ({ formData, setFormData }) => {

  const [show, setShow] = useState(false);
  const handleClick = () => setShow(!show);
  const toast = useToast();

  const [originCountry, setOriginCountry] = React.useState('')
  const [age, setAge] = React.useState('');
  // const [languages, setLanguages] = React.useState<string[]>([]);
  const [gender, setGender] = React.useState('');
  const [sexuality, setSexuality] = React.useState('');

  const countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo',
    'Costa Rica',
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czechia',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kosovo',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Timor-Leste',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
  ];
  
  const genders = ['Male', 'Female', 'Nonbinary'];
  const sexualities = ['Heterosexual', 'Non-heterosexual'];

  const handleCountrySelect = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setFormData({
      ...formData,
      originCountry: event.target.value,
    });
  };

  const handleAge = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      age: event.target.value,
    });
  };

//   const handleLanguageSelect = (event: React.ChangeEvent<HTMLSelectElement>) => {
//     const selectedOptions = Array.from(event.target.selectedOptions).map(option => option.value);
//     setFormData({
//       ...formData,
//       languages: selectedOptions,
//     });
//   };

  const handleGender = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setFormData({
      ...formData,
      gender: event.target.value,
    });
  };

  const handleSexuality = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setFormData({
      ...formData,
      sexuality: event.target.value,
    });
  };


  return (
    <>
      <Heading w="100%" textAlign={'center'} fontWeight="bold" mb="2%">
        Basic Information
      </Heading>
      <Flex>
        <FormControl mr="5%">
          <FormLabel htmlFor="origin-country" fontWeight={'bold'}>
            Origin Country
          </FormLabel>
          <Select id="origin-country" placeholder="Select country"
            value={originCountry}
            onChange={handleCountrySelect}
            >
            {countries.map((country, index) => (
              <option key={index}>{country}</option>
            ))}
          </Select>
        </FormControl>

        <FormControl>
          <FormLabel htmlFor="age" fontWeight={'bold'}>
            Age
          </FormLabel>
          <Input id="age" type="number" placeholder="Enter age" 
            value={age}
            onChange={handleAge}
          />
        </FormControl>
      </Flex>

      <FormControl mt="2%">
        <FormLabel htmlFor="languages" fontWeight={'bold'}>
          Languages (Press shift to select multiple languages)
        </FormLabel>
        <Select id="languages" placeholder="Select languages" 
            // value={languages}
            // onChange={handleLanguageSelect}
        multiple>
            <option>English</option>
            <option>Spanish</option>
            <option>French</option>
            <option>German</option>
            <option>Chinese</option>
            <option>Arabic</option>
            <option>Bengali</option>
            <option>Russian</option>
            <option>Portuguese</option>
            <option>Hindi</option>
            <option>Japanese</option>
            <option>Punjabi</option>
            <option>Burmese</option>
            <option>Turkish</option>
            <option>Vietnamese</option>
            <option>Korean</option>
            <option>Italian</option>
            <option>Thai</option>
            <option>Persian</option>
            <option>Polish</option>
            <option>Urdu</option>
            <option>Malay</option>
            <option>Ukrainian</option>
            <option>Romanian</option>
            <option>Dutch</option>
            <option>Hungarian</option>
            <option>Czech</option>
            <option>Greek</option>
            <option>Swedish</option>
            <option>Danish</option>
            <option>Finnish</option>
            <option>Norwegian</option>
            <option>Hebrew</option>
            <option>Slovak</option>
            <option>Croatian</option>
            <option>Catalan</option>
            <option>Lithuanian</option>
            <option>Latvian</option>
            <option>Estonian</option>
            <option>Slovenian</option>
            <option>Icelandic</option>
            <option>Albanian</option>
            <option>Georgian</option>
            <option>Serbian</option>
            <option>Mongolian</option>
            <option>Swahili</option>
            <option>Bulgarian</option>
            <option>Macedonian</option>
            <option>Azerbaijani</option>
            <option>Kazakh</option>
            <option>Maltese</option>
            <option>Irish</option>
            <option>Tamil</option>
            <option>Telugu</option>
            <option>Bosnian</option>
            <option>Marathi</option>
            <option>Uzbek</option>
            <option>Pashto</option>
            <option>Sinhala</option>
            <option>Nepali</option>
            <option>Belarusian</option>
            <option>Kurdish</option>
            <option>Tajik</option>
            <option>Luxembourgish</option>
            <option>Armenian</option>
            <option>Corsican</option>
            <option>Basque</option>
            <option>Gujarati</option>
            <option>Haitian Creole</option>
            <option>Hmong</option>
            <option>Laotian</option>
            <option>Kyrgyz</option>
            <option>Kannada</option>
            <option>Bislama</option>
            <option>Chichewa</option>
            <option>Fijian</option>
            <option>Malagasy</option>
            <option>Marshallese</option>
            <option>Maori</option>
            <option>Nauru</option>
            <option>Oriya</option>
            <option>Palauan</option>
            <option>Papiamento</option>
            <option>Punjabi</option>
            <option>Samoan</option>
            <option>Sindhi</option>
            <option>Somali</option>
            <option>Tahitian</option>
            <option>Tatar</option>
            <option>Tok Pisin</option>
            <option>Tongan</option>
            <option>Tswana</option>
            <option>Turkmen</option>
            <option>Twi</option>
            <option>Uighur</option>
            <option>Xhosa</option>
            <option>Yoruba</option>
            <option>Zulu</option>
        </Select>
      </FormControl>

      <FormControl mt="2%">
        <FormLabel htmlFor="gender" fontWeight={'bold'}>
          Gender
        </FormLabel>
        <Select id="gender" placeholder="Select gender"
            value={gender}
            onChange={handleGender}>
          {genders.map((gender, index) => (
            <option key={index}>{gender}</option>
          ))}
        </Select>
      </FormControl>

      <FormControl mt="2%">
        <FormLabel htmlFor="sexuality" fontWeight={'bold'}>
          Sexuality
        </FormLabel>
        <Select id="sexuality" placeholder="Select sexuality"
            value={sexuality}
            onChange={handleSexuality}>
          {sexualities.map((sexuality, index) => (
            <option key={index}>{sexuality}</option>
          ))}
        </Select>
      </FormControl>
    </>
  );
};

const Form2 = () => {
    
  const [partySize, setPartySize] = React.useState('');
  const [highestEducationLevel, setHighestEducationLevel] = React.useState('');
  const [democracyDesire, setDemocracyDesire] = React.useState('');
  const [cultureDesire, setCultureDesire] = React.useState('');
  
  const partySizes = ['Individual', 'Travelling with dependants'];
  const educationLevels = [
    'Some Schooling/High School',
    "Bachelor's Degree",
    'Graduate Degree',
  ];
  const democracyOptions = ['Yes', 'No'];
  const cultureOptions = ['Collectivist', 'Individualistic'];

  const handlePartySize = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setPartySize(event.target.value);
  };

  const handleHighestEducationLevel = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setHighestEducationLevel(event.target.value);
  };

  const handleDemocracyDesire = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setDemocracyDesire(event.target.value);
  };

  const handleCultureDesire = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setCultureDesire(event.target.value);
  };

  return (
    <>
      <Heading w="100%" textAlign={'center'} fontWeight="bold" mb="2%">
        Additional Details
      </Heading>
      <FormControl mt="2%">
        <FormLabel htmlFor="party-size" fontWeight={'bold'}>
          Party Size
        </FormLabel>
        <Select id="party-size" placeholder="Select option"
            value={partySize}
            onChange={handlePartySize}>
          {partySizes.map((size, index) => (
            <option key={index}>{size}</option>
          ))}
        </Select>
      </FormControl>

      <FormControl mt="2%">
        <FormLabel htmlFor="education-level" fontWeight={'bold'}>
          Highest Educational Level
        </FormLabel>
        <Select id="education-level" placeholder="Select option"
            value={highestEducationLevel}
            onChange={handleHighestEducationLevel}>
          {educationLevels.map((level, index) => (
            <option key={index}>{level}</option>
          ))}
        </Select>
      </FormControl>

      <FormControl mt="2%">
        <FormLabel htmlFor="democracy-desire" fontWeight={'bold'}>
          Democracy Desire
        </FormLabel>
        <Select id="democracy-desire" placeholder="Select option"
            value={democracyDesire}
            onChange={handleDemocracyDesire}>
          {democracyOptions.map((option, index) => (
            <option key={index}>{option}</option>
          ))}
        </Select>
      </FormControl>

      <FormControl mt="2%">
        <FormLabel htmlFor="culture-desire" fontWeight={'bold'}>
          Culture Desire
        </FormLabel>
        <Select id="culture-desire" placeholder="Select option"
            value={cultureDesire}
            onChange={handleCultureDesire}>
          {cultureOptions.map((option, index) => (
            <option key={index}>{option}</option>
          ))}
        </Select>
      </FormControl>
    </>
  );
};

export default function Multistep() {
  const [step, setStep] = useState(1);
  const [progress, setProgress] = useState(0); // Adjust initial progress

  const [formData, setFormData] = useState({
    // Initialize an object to store form data
    originCountry: '',
    age: '',
    // languages: [],
    gender: '',
    sexuality: '',
    partySize: '',
    highestEducationLevel: '',
    democracyDesire: '',
    cultureDesire: '',
  });

  // Function to handle moving to the next step
  const nextStep = () => {
    setStep(step + 1);
    setProgress(progress + 50); // Adjust progress increment based on number of forms
  };

  // Function to handle going back to the previous step
  const prevStep = () => {
    setStep(step - 1);
    setProgress(progress - 50); // Adjust progress decrement based on number of forms
  };

  return (
    <>
      <Helmet bodyAttributes={{ style: 'background-color : #4b92db' }} />
      {/* Wrap everything in a container for positioning */}
      <div style={{ position: 'relative' }}>
        <Flex
          as="nav"
          align="center"
          justify="space-between"
          wrap="wrap"
          padding="1.5rem"
          bg="#ffffff" // Navbar background color
          color="#4b92db" // Text color
          boxShadow="0 4px 6px -1px rgba(0, 0, 0, 0.1)"
          position="fixed" // Fixed position to stick at the top
          top="0" // Stick to the top
          left="0"
          right="0"
          zIndex="999" // Ensure it's above other content
          width="100%" // Full width
        >
          <Flex align="center" mr={5}>
            <Image
              boxSize="40px" // Adjust size as needed
              src="/unhcr logo.svg" // Path to your logo file
              alt="UNHCR logo"
            />
            <Text ml={2} fontWeight="bold" fontSize={20}>
              Refugee Haven Search
            </Text>
          </Flex>
        </Flex>

        <Box
          rounded="lg"
          bg="white" // so forms are not transparent and do not blend into the background
          shadow="1px 1px 3px rgba(0,0,0,0.3)"
          maxWidth={800}
          p={6}
          m="10px auto"
          as="form"
          mt="100px" // Adjust top margin to position below the navbar
        >
          <Progress hasStripe value={progress} mb="5%" mx="5%" isAnimated></Progress>
          {step === 1 ? <Form1 formData={formData} setFormData={setFormData} /> : <Form2 />}
          <ButtonGroup mt="5%" w="100%">
            <Flex w="100%" justifyContent="space-between">
              <Flex>
                <Button
                  onClick={prevStep}
                  isDisabled={step === 1}
                  colorScheme="teal"
                  variant="solid"
                  w="7rem"
                  mr="5%"
                >
                  Back
                </Button>
                <Button
                  onClick={nextStep}
                  isDisabled={step === 2} // Adjust condition based on number of forms
                  colorScheme="teal"
                  variant="outline"
                  w="7rem"
                >
                  Next
                </Button>
              </Flex>
              {step === 2 ? (
                <Link to= "/results">
                    <Button
                    colorScheme="red"
                    variant="solid"
                    w="7rem"
                    >
                    Submit
                    </Button>
                </Link>
              ) : null}
            </Flex>
          </ButtonGroup>
        </Box>
      </div>
    </>
  );
}
