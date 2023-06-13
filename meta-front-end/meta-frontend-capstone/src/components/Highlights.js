import './Highlights.css';

function Highlights() {
  return (
    <div className="highLightsSection">
      <div className="hightTitle">
        <div>
          <h1>This weeks specials!</h1>
        </div>
        <div>
          <h1>Online Menu</h1>
        </div>
      </div>

      <div className="highLightDickSection">
        <div className="highLightDickSectionGridItem">
          <div className="highLightDickflexContainer">
            <div className="highLightDickflexItem">
              <img src="https://picsum.photos/600?random=1" alt="food" />
              <div>
                <h2>Greek salad</h2>
                <p>$12.99</p>
              </div>
              <div>
                <p>
                  Mind is everything: muscle, pieces of rubber. All that I am, I
                  am because of my mind. - Paavo Nurmi
                </p>
              </div>
              <div>
                <p>Order a delivery</p>
              </div>
            </div>
            <div className="highLightDickflexItem">
              <img src="https://picsum.photos/600?random=2" alt="food" />
              <div>
                <h2>Bruchetta</h2>
                <p>$5.99</p>
              </div>
              <div>
                <p>
                  No pessimist ever discovered the secrets of the stars, or
                  sailed to an uncharted land, or opened a new heaven to the
                  human spirit. - Helen Keller
                </p>
              </div>
              <div>
                <p>Order a delivery</p>
              </div>
            </div>
            <div className="highLightDickflexItem">
              <img src="https://picsum.photos/600?random=3" alt="food" />
              <div>
                <h2>Lemon Dessert</h2>
                <p>$3.00</p>
              </div>
              <div>
                <p>
                  The first duty of a human being is to assume the right
                  functional relationship to society - more briefly, to find
                  your real job, and do it. - Charlotte Perkins Gilman
                </p>
              </div>
              <div>
                <p>Order a delivery</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Highlights;
