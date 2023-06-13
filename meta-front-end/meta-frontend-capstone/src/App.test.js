import { render, screen } from '@testing-library/react';
import App from './App';
import Header from './components/Header';
import Hero from './components/Hero';
import Highlights from './components/Highlights';
import Testimonials from './components/Testimonials';
import About from './components/About';
import Footer from './components/Footer';

test('title is little leamon', () => {
  render(<App />);
  const linkElement = screen.getByText(/little leamon/i);
  expect(linkElement).toBeInTheDocument();
});

test('Header', () => {
  render(<Header />);
  ['Home', 'About', 'Menu', 'Reservations', 'Order Online', 'Login'].forEach(
    (item) => {
      const navElements = screen.getByText(RegExp('home', 'i'));
      expect(navElements).toBeInTheDocument();
    }
  );
});

test('Hero', () => {
  render(<Hero />);
  const heroElementsArray = [
    'Little Lemon',
    'Chicago',
    "If you can't explain it simply, you don't understand it well enough. - Albert Einstein",
    'Reserve a Table',
  ];
  heroElementsArray.forEach((item) => {
    const highLightElements = screen.getAllByText(RegExp(item, 'i'));
    expect(highLightElements).toBeTruthy();
  });
});

test('Highlights', () => {
  render(<Highlights />);
  const highLightElementsArray = [
    'This weeks specials!',
    'Online Menu',
    'Greek salad',
    'Mind is everything: muscle, pieces of rubber. All that I am, I am because of my mind. - Paavo Nurmi',
    'Order a delivery',
    'Bruchetta',
    'No pessimist ever discovered the secrets of the stars, or sailed to an uncharted land, or opened a new heaven to the human spirit. - Helen Keller',
    'Order a delivery',
    'Lemon Dessert',
    'The first duty of a human being is to assume the right functional relationship to society - more briefly, to find your real job, and do it. - Charlotte Perkins Gilman',
    'Order a delivery',
  ];
  highLightElementsArray.forEach((item) => {
    const highLightElements = screen.getAllByText(RegExp(item, 'i'));
    expect(highLightElements).toBeTruthy();
  });
});

test('Testimonials', () => {
  render(<Testimonials />);
  const testimonialsElementsArray = [
    'Testimonials',
    'Testimonial 1',
    'Testimonial 2',
    'Testimonial 3',
  ];
  testimonialsElementsArray.forEach((item) => {
    const testimonialsElements = screen.getAllByText(RegExp(item, 'i'));
    expect(testimonialsElements).toBeTruthy();
  });
});

test('About', () => {
  render(<About />);
  const aboutElementsArray = [
    'Little Leamon',
    'Chicago, IL',
    'The only person who never makes mistakes is the person who never does anything. - Denis Waitley Imagination disposes of everything; it creates beauty, justice, and happiness, which are everything in this world. - Blaise Pascal When you learn, teach. When you get, give. - Maya Angelou',
  ];
  aboutElementsArray.forEach((item) => {
    const aboutElements = screen.getAllByText(RegExp(item, 'i'));
    expect(aboutElements).toBeTruthy();
  });
});

test('Footer', () => {
  render(<Footer />);
  const footerElementsArray = [
    'Doormat Nav',
    'Home',
    'About',
    'Testimonials',
    'Blah',
    'Contact',
    'Social Media Link',
    'Address',
    'Phone Number',
    'Email',
  ];
  footerElementsArray.forEach((item) => {
    const footerElements = screen.getAllByText(RegExp(item, 'i'));
    expect(footerElements).toBeTruthy();
  });
});
