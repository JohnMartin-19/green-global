import {React} from "react";
import './landing.css'
import { Link } from "react-router-dom";
function LandingPage(){
    return(
        <div>
            <div className='hero-img'>
                <div className='heading'>
                    <h1 className="text-right mt-5">Green<span>Global</span></h1>
                    <p className="text-right lead">Connecting Your Local Farmer With The Far-end Buyer!</p>
                    <br />
                    <br />
                    <br />
                    <br />
                    <Link to='/sign-up'className="btn" >REGISTER</Link>
                    
                </div>  
            </div>
            <div className="container-fluid">
                <h1 className="head">Our Mission!</h1>
                <div className="row">
                    <div className="column">
                        <h1 className="head">What We Do?</h1>
                        <p>Green Global is a platform that connects local farmers with the far end buyers, enabling them to sell their products directly to consumers worldwide.</p>
                        <p>We are a platform that connects local farmers with the far-end buyers, enabling them to sell their products directly to consumers all over the world.</p>
                    </div>
                    <div className="column">
                        <h1 className="head">Why It Matters?</h1>
                        <p>According to research, 40% of the farm produce is lost before even it gets consumed. This is largely fueled by limited access to ready market for farm produce.</p>
                    </div>
                </div>
            </div>

        </div>
        
    )
}
export default LandingPage