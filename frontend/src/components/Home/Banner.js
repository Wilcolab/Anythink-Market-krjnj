import React from "react";
import logo from "../../imgs/logo.png";
import Search from "./Search";
const Banner = () => {
  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img src={logo} alt="banner" height="10" />
        <div className="d-flex justify-content-center align-items-center">
          <span id="get-part">A place to get</span>
          <Search />
          <span> the cool stuff.</span>
        </div>
      </div>
    </div>
  );
};

export default Banner;
