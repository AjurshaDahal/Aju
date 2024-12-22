import React from 'react';
import '../css/navbar.css';

function Navbar() {
    return (
        <div className="navbar">
            <div className="nav-links">
                <button className="nav-button active">Home</button>
                <button className="nav-button">About</button>
                <button className="nav-button">Elections</button>
                <button className="nav-button">Results</button>
                <button className="nav-button">Log out</button>
            </div>
        </div>
    );
}

export default Navbar;
