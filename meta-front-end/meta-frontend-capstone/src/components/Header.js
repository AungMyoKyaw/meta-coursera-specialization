import './Header.css';
import logo from '../assets/Logo.svg';
import { Outlet, Link } from 'react-router-dom';

function Header() {
  return (
    <div>
      <nav>
        <ul className="headerList">
          <li>
            <img src={logo} alt="logo" />
          </li>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/">About</Link>
          </li>
          <li>
            <Link to="/">Menu</Link>
          </li>
          <li>
            <Link to="/">Reservations</Link>
          </li>
          <li>
            <Link to="/">Order Online</Link>
          </li>
          <li>
            <Link to="/">Login</Link>
          </li>
        </ul>
      </nav>
      <Outlet />
    </div>
  );
}

export default Header;
