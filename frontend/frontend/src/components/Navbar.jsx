// components/Navbar/index.js

import React from "react";
import {
	Nav,
	NavLink,
	Bars,
	NavMenu,
	NavBtn,
	NavBtnLink,
} from "./NavbarElements";

const Navbar = () => {
	return (
		<>
			<Nav>
				<Bars />

				<NavMenu>
					<NavLink to="/about" >
						About
					</NavLink>
					<NavLink to="/services" activeStyle>
						Services
					</NavLink>
					<NavLink to="/Reviews" activeStyle>
						Reviews
					</NavLink>
					<NavLink to="/Contact" activeStyle>
						Contact
					</NavLink>
					<NavLink to="/sign-up" activeStyle>
						Sign Up
					</NavLink>
					{/* Second Nav */}
					{/* <NavBtnLink to='/sign-in'>Sign In</NavBtnLink> */}
				</NavMenu>
				<NavBtn>
					<NavBtnLink to="/signin">
						Sign In
					</NavBtnLink>
				</NavBtn>
			</Nav>
		</>
	);
};

export default Navbar;
