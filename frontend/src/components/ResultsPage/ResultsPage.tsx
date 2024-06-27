'use client'

import {
  Box,
  Flex,
  Heading,
  Container,
  Text,
  Button,
  Stack,
  Icon,
  useColorModeValue,
  createIcon,
  Input,
  InputGroup,
  InputLeftElement,
  InputRightElement,
  Image,
  Center,
  Select,
  RangeSlider,
  RangeSliderFilledTrack,
  RangeSliderThumb,
  RangeSliderTrack,
  Grid,
  GridItem,
} from '@chakra-ui/react'

import { useParams, Link, useLocation } from 'react-router-dom';
import React, { useEffect, useState, useMemo } from 'react';

export default function SearchResultsPage() {
  
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
              <GridItem>
                <Box p={5} shadow="md" borderWidth="1px" borderRadius="md">
                  <Text fontSize="xl" fontWeight="bold" mt={4}>
                    title
                  </Text>
                  <Text color="gray.600" fontSize="md" mt={2}>
                    description
                  </Text>
                  <Flex justify="space-between" mt={4}>
                    <Text fontSize="lg" fontWeight="bold">
                      price
                    </Text>
                    <Text fontSize="lg">store</Text>
                  </Flex>
                </Box>
              </GridItem>
          </Grid>

          <Flex justify="center" mt={8}>
            <Link to="/">
              <Button
                colorScheme="green"
                bg="green.400"
                rounded="full"
                px={6}
                _hover={{
                  bg: 'green.500',
                }}
              >
                Search For Another Item!
              </Button>
            </Link>
          </Flex>

        </Stack>
      </Container>
    </>
  );
}