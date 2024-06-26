import Logo from "@/assets/logo.png";
import LandingPage from "@/components/LandingPage/LandingPage";

import styles from "./App.module.css";

import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
      </Routes>
    </Router>
  );
}