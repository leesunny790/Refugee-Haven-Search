import Logo from "@/assets/logo.png";
import LandingPage from "@/components/LandingPage/LandingPage";
import FormPage from "@/components/FormPage/FormPage";
import ResultsPage from "@/components/ResultsPage/ResultsPage";

import styles from "./App.module.css";

import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/userform" element={<FormPage />} />
        <Route path="/results" element={<ResultsPage />} />
      </Routes>
    </Router>
  );
}