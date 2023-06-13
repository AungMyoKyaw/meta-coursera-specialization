import { Routes, Route } from 'react-router-dom';

import './App.css';
import Header from './components/Header';
import Hero from './components/Hero';
import Highlights from './components/Highlights';
import Testimonials from './components/Testimonials';
import About from './components/About';
import Footer from './components/Footer';
import Form from './components/Form';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Header />}>
        <Route index element={<Home />} />
        <Route path="reserve-table" element={<Form />} />
      </Route>
    </Routes>
  );
}

function Home() {
  return (
    <div className="app">
      <Hero />
      <Highlights />
      <Testimonials />
      <About />
      <Footer />
    </div>
  );
}

export default App;
