import React from "react";
import {
	Box,
	FooterContainer,
	Row,
	Column,
	FooterLink,
	Heading,
} from "./FooterStyles";

function Footer(){
	return (
		<Box>
			<h1
				style={{
					color: "#294B29",
					textAlign: "center",
					marginTop: "10px",
				}}
			>
				    GREENGLOBAL
			</h1>
            <br />
            <br />
			<FooterContainer>
				<Row>
					<Column>
						<Heading>About Us</Heading>
						<FooterLink href="#">
							Aim
						</FooterLink>
						<FooterLink href="#">
							Mision
						</FooterLink>
						<FooterLink href="#">
							Testimonials
						</FooterLink>
					</Column>
					<Column>
						<Heading>Services</Heading>
						<FooterLink href="#">
							Empowering Farmers
						</FooterLink>
						<FooterLink href="#">
							Supporting Local Agriculture
						</FooterLink>
						<FooterLink href="#">
							Farmers Market Place
						</FooterLink>
						
					</Column>
					<Column>
						<Heading>Contact Us</Heading>
						<FooterLink href="#">
							Mburu-CEO
						</FooterLink>
						<FooterLink href="#">
							Ezra-DATA ANALYST
						</FooterLink>
						<FooterLink href="#">
							Kimani-Co-Founder
						</FooterLink>
						<FooterLink href="#">
							Adrine-LEGAL
						</FooterLink>
					</Column>
					<Column>
						<Heading>Social Media</Heading>
						<FooterLink href="#">
							<i className="fab fa-facebook-f">
								<span
									style={{
										marginLeft: "10px",
									}}
								>
									Facebook
								</span>
							</i>
						</FooterLink>
						<FooterLink href="#">
							<i className="fab fa-instagram">
								<span
									style={{
										marginLeft: "10px",
									}}
								>
									Instagram
								</span>
							</i>
						</FooterLink>
						<FooterLink href="#">
							<i className="fab fa-twitter">
								<span
									style={{
										marginLeft: "10px",
									}}
								>
									Twitter
								</span>
							</i>
						</FooterLink>
						<FooterLink href="#">
							<i className="fab fa-youtube">
								<span
									style={{
										marginLeft: "10px",
									}}
								>
									Youtube
								</span>
							</i>
						</FooterLink>
					</Column>
				</Row>
			</FooterContainer>
            <div className="cc" style={{color:'#294B29',textAlign: "center",
					marginTop: "20px"}}>&copy;-GREENGLOBAL-2024</div>
		</Box>
	);
};
export default Footer;
