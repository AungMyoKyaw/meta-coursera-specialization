import React from "react";
import { Avatar, Heading, VStack } from "@chakra-ui/react";
import FullScreenSection from "./FullScreenSection";

const greeting = "Hello, I am Pete!";
const bio1 = "A frontend developer";
const bio2 = "specialised in React";

// Implement the UI for the LandingSection component according to the instructions.
// Use a combination of Avatar, Heading and VStack components.
// https://i.pravatar.cc/150?img=7
const LandingSection = () => (
  <FullScreenSection
    justifyContent="center"
    alignItems="center"
    isDarkBackground
    backgroundColor="#2A4365"
  >
    <VStack color="white" spacing={2}>
      <Avatar src="https://i.pravatar.cc/600" size="2xl"></Avatar>
      <Heading as="h1" size="sm" color="white">
        {greeting}
      </Heading>
      <Heading as="h2" size="xl" color="white">
        {bio1}
      </Heading>
      <Heading as="h2" size="xl" color="white">
        {bio2}
      </Heading>
    </VStack>
  </FullScreenSection>
);

export default LandingSection;
