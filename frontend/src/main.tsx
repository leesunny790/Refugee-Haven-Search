import "./main.css";

import { ChakraProvider } from '@chakra-ui/react'
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import App from "./App";

const container = document.getElementById("root");
const root = createRoot(container as HTMLDivElement);

root.render(
  <StrictMode>
    <ChakraProvider>
      <App />
    </ChakraProvider>
  </StrictMode>
);
