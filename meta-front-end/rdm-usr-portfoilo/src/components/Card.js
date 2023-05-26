import { Heading, HStack, Image, Text, VStack } from "@chakra-ui/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import React from "react";

const Card = ({ title, description, imageSrc }) => {
  // Implement the UI for the Card component according to the instructions.
  // You should be able to implement the component with the elements imported above.
  // Feel free to import other UI components from Chakra UI if you wish to.
  return (
    <VStack
      spacing={4}
      align="stretch"
      maxW="xl"
      shadow="md"
      borderRadius="lg"
      overflow="hidden"
      backgroundColor="white"
    >
      <Image src={imageSrc} alt={title} />
      <VStack spacing={0} align="stretch" p={4}>
        <Heading as="h3" size="md" color="black">
          {title}
        </Heading>
        <Text color="black">{description}</Text>
      </VStack>
      <a href="/#projects-section">
        <HStack justifyContent="flex-start" p={4} color="black">
          <Text>See more</Text>
          <FontAwesomeIcon icon={faArrowRight} />
        </HStack>
      </a>
    </VStack>
  );
};

export default Card;
