import './Hero.css';
import heroImage from '../assets/restauranfood.jpg';
import { Link } from 'react-router-dom';

function Hero() {
  return (
    <div className="heroSection">
      <div>
        <h1>Little Lemon</h1>
        <div>
          <p>Chicago</p>
        </div>
        <div>
          <p>
            If you can't explain it simply, you don't understand it well enough.
            - Albert Einstein
          </p>
        </div>
        <div>
          <Link to="/reserve-table">
            <button>Reserve a Table</button>
          </Link>
        </div>
      </div>
      <div>
        <img src={heroImage} alt="hero" />
      </div>
    </div>
  );
}

export default Hero;
