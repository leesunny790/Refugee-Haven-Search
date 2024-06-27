'use client';

import {
  Box,
  Flex,
  Heading,
  Container,
  Text,
  Button,
  Stack,
  Grid,
  GridItem,
  Image,
} from '@chakra-ui/react';

import { Link } from 'react-router-dom';
import React from 'react';

export default function SearchResultsPage() {
  // Top 5 countries based on previous analysis
  const countries = [
    
  ];

  return (
    <>
      <Container maxW={'3xl'}>
        <Stack
          as={Box}
          textAlign={'center'}
          spacing={{ base: 8, md: 14 }}
          py={{ base: 20, md: 36 }}
        >
          <Heading
            fontWeight={600}
            fontSize={{ base: '2xl', sm: '4xl', md: '6xl' }}
            lineHeight={'110%'}
          >
            Country Results
          </Heading>

          <Grid templateColumns="repeat(auto-fit, minmax(250px, 1fr))" gap={6}>
            {countries.map((country, index) => (
              <GridItem key={index}>
                <Box p={5} shadow="md" borderWidth="1px" borderRadius="md">
                  <Image
                    src={country.flagUrl}
                    alt={`Flag of ${country.name}`}
                    boxSize="50px"
                    objectFit="cover"
                    borderRadius="full"
                    mb={4}
                  />
                  <Text fontSize="xl" fontWeight="bold" mt={4}>
                    {country.name}
                  </Text>
                  <Text color="gray.600" fontSize="md" mt={2}>
                    HDI: {country.hdi}
                  </Text>
                  <Text color="gray.600" fontSize="md" mt={2}>
                    Collectivism Index: {country.collectivismIndex}
                  </Text>
                  <Text color="gray.600" fontSize="md" mt={2}>
                    Democracy: {country.democracy}
                  </Text>
                  <Text color="gray.600" fontSize="md" mt={2}>
                    Cost of Living: {country.costOfLiving}
                  </Text>
                  <Text color="gray.600" fontSize="md" mt={2}>
                    Males to 100 Females: {country.malesToFemales}
                  </Text>
                </Box>
              </GridItem>
            ))}
          </Grid>

          <Flex justify="center" mt={8}>
            <Link to="/userform">
              <Button
                colorScheme="blue"
                bg="blue.400"
                rounded="full"
                px={6}
                _hover={{
                  bg: 'blue.500',
                }}
              >
                Search for another profile!
              </Button>
            </Link>
          </Flex>
        </Stack>
      </Container>
    </>
  );
}
