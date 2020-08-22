import React from 'react';
import {Link} from 'react-router-dom'

function Navbar(){
    return(
        <nav>
            <h1>GIF-MACHINE</h1>
            <ul>
                <Link style={{textDecoration: "none"}} to ="/home">
                    <li>Home</li>
                </Link>
                <Link style={{textDecoration: "none"}} to ="/about">
                    <li>About</li>
                </Link>
                <Link style={{textDecoration: "none"}} to ="/contact">
                    <li>Contact Us</li>
                </Link>
            </ul>
        </nav>
    )
}

export default Navbar;