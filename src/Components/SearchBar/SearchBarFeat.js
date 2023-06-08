import React from "react";

function SearchBarFeat() {
  return (
    <form className="d-flex search_bar">
      <input
        className="form-control me-2"
        type="search"
        placeholder="Search"
        aria-label="Search"
      />
      <button className="btn btn-outline-success" type="submit">
        Search
      </button>
    </form>
  );
}

export default SearchBarFeat;