import './Footer.css';

function Footer() {
  return (
    <div className="footerGrid">
      <div className="footerGridItem">
        <div className="footerFlexContainer">
          <div className="footerFlexItem">
            <img
              src="https://picsum.photos/300/600?random=1"
              alt="placeholder"
            />
          </div>
          <div className="footerFlexItem">
            <h2>Doormat Nav</h2>
            <ul>
              <li>Home</li>
              <li>About</li>
              <li>Testimonials</li>
              <li>Blah</li>
            </ul>
          </div>
          <div className="footerFlexItem">
            <h2>Contact</h2>
            <ul>
              <li>Address</li>
              <li>Phone Number</li>
              <li>Email</li>
            </ul>
          </div>
          <div className="footerFlexItem">
            <h2>Social Media Link</h2>
            <ul>
              <li>Address</li>
              <li>Phone Number</li>
              <li>Email</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Footer;
