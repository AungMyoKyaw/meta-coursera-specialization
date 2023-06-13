import './Testimonials.css';

function Testimonials() {
  return (
    <div className="testimonialsGrid">
      <div className="testimonialsGridItem">
        <div className="testimonialsHeader">
          <h1>Testimonials</h1>
        </div>
        <div className="testimonialsBody">
          <div className="testimonialsBodyItem">
            <h2>Testimonial 1</h2>
            <div className="imgandtext">
              <img src="https://picsum.photos/300?random=1" alt="placeholder" />
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Quisquam, voluptatum.
              </p>
            </div>
          </div>
          <div className="testimonialsBodyItem">
            <h2>Testimonial 2</h2>
            <div className="imgandtext">
              <img src="https://picsum.photos/300?random=2" alt="placeholder" />
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Quisquam, voluptatum.
              </p>
            </div>
          </div>
          <div className="testimonialsBodyItem">
            <h2>Testimonial 3</h2>
            <div className="imgandtext">
              <img src="https://picsum.photos/300?random=3" alt="placeholder" />
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Quisquam, voluptatum.
              </p>
            </div>
          </div>
          <div className="testimonialsBodyItem">
            <h2>Testimonial 4</h2>
            <div className="imgandtext">
              <img src="https://picsum.photos/300?random=4" alt="placeholder" />
              <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Quisquam, voluptatum.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Testimonials;
