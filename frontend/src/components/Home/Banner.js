import React, { useState } from "react";
import logo from "../../imgs/logo.png";
import Search from "./Search";
const Banner = () => {
  const [hidden, setHidden] = useState(true);
  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img className="img-fluid" src={logo} alt="banner" />
        <div>
          <span>A place to </span>
          <span
            id="get-part"
            onClick={() => {
              setHidden(false);
            }}
          >
            {"\u00a0"}
            get
            {"\u00a0"}
          </span>
          <span hidden={hidden}>
            <Search />
          </span>
          <span> the cool stuff.</span>
        </div>
      </div>
    </div>
  );
};

export default Banner;
