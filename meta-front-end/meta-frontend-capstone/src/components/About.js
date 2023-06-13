import './About.css';

function About() {
  return (
    <div className="aboutGrid">
      <div className="aboutGridItem">
        <div className="aboutFlexContainer">
          <div className="aboutFlexItem">
            <div className="titleAndText">
              <h1>Little Leamon</h1>
              <p>Chicago, IL</p>
              <p>
                The only person who never makes mistakes is the person who never
                does anything. - Denis Waitley Imagination disposes of
                everything; it creates beauty, justice, and happiness, which are
                everything in this world. - Blaise Pascal When you learn, teach.
                When you get, give. - Maya Angelou
              </p>
            </div>
          </div>
          <div className="aboutFlexItem imgFlexItem">
            <img
              className="img1"
              src="https://picsum.photos/600?random=1"
              alt="placeholder"
            />
            <img
              className="img2"
              src="https://picsum.photos/600?random=2"
              alt="placeholder"
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default About;
