// filename -App.js

import React from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import {
	BrowserRouter as Router,
	Routes,
	Route,
} from "react-router-dom";

import About from "./components/AboutUs";
import Service from "./components/Services";
import Review from './components/Reviews'
import SignUp from "./components/SignUp";
import LandingPage from "./components/landing";
import Contact from "./components/Contact";

function App() {
	return (
		<Router>
			<Navbar />
			<Routes>
				<Route path="/" element={<LandingPage />} />
				<Route path="/about" element={<About />} />
				<Route
					path="/events"
					element={<Service />}
				/>
				<Route path="/annual" element={<Review />}/>
				<Route path="/team" element={<Contact />} />
				<Route
					path="/sign-up"
					element={<SignUp />}
				/>
			</Routes>
		</Router>
	);
}

export default App;
