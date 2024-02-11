import {React} from "react";
import './landing.css'
import { Link } from "react-router-dom";
function LandingPage(){
    return(
        <div>
            <div className='hero-img'>
                <div className='heading'>
                    <h1 className="text-right mt-5"><span>GREEN</span>GLOBAL</h1>
                    <p className="text-right lead">Connecting Your Local Farmer With The Far-end Buyer!</p>
                    <br />
                    <br />
                    <br />
                    <br />
                    <Link to='/sign-up'className="btn" >REGISTER</Link>
                    
                </div>  
            </div>
            <div className="container-fluid">
                <h1 className="head"><span>OUR MISSION!</span></h1>
                <div className="row">
                    <div className="column">
                        <h3 className="head">What We Do?</h3>
                        <ol className="purpose">
                            <li><span>Connecting Farmers with Buyers:</span> We provide a digital marketplace where local farmers can showcase their produce directly to buyers and consumers. This eliminates the need for intermediaries, ensuring fair prices for farmers and fresh, quality products for buyers.</li>
                            <li><span>Farmers Marketplace:</span> Connect with local farmers and buy fresh produce directly from them.</li>
                            <li><span>Supporting Local Agriculture:</span> By promoting local farming communities, we contribute to sustainable agricultural practices and support local economies. Our platform empowers farmers to expand their reach beyond traditional markets and connect with a wider audience of consumers.</li>
                            <li><span>Transparent Transactions:</span> We prioritize transparency in every transaction. Buyers can learn about the farmers behind the products they purchase, including their farming practices and values. This fosters trust and strengthens the bond between farmers and consumers.</li>
                            <li><span>Empowering Farmers:</span> We empower farmers with the tools and resources they need to thrive in today's digital age. From digital marketing support to logistics assistance, we're committed to helping farmers succeed in the online marketplace. </li>
                            <li><span>Community Engagement:</span> We foster a sense of community among farmers, buyers, and consumers. Through educational initiatives, events, and forums, we encourage collaboration and knowledge-sharing, strengthening the local food ecosystem.</li>
                        </ol>
                    </div>
                    <div className="column">
                        <h3 className="head">Why It Matters?</h3>
                        <p>From the Ministry of Agriculture, according to their research, 40% of the farm produce is lost before  it even gets consumed.
                            This is largely fueled by limited access to ready market for farm produce as we as poor harvesting practices.In the year 2022,
                            approximately 4 million Kenya citizens faced food shortage.Is it because we do not produce enough food? I don't think so.On top of that, 
                            agriculture accounts for about 31.5% of Kenya's GDP annualy.However, the sector is highly vulnerable to climate change and 
                            other economical & environmental factors which can negatively impact the output of farmers.Over 75% of the produce comes from 
                            small scale farmers, whom are our main target for this platform.They are the backbone of our economy and they are often overlooked. 
                            By using Green Global, we can help them reach out to not only local but also a global marketplace.
                            Coming up with such a system was majorly to curb the perennial post-harvest food loss, especially by the small-scale farmers. On top of that, we want to bridge the 
                            gap between local farmers and the buyers/consumers. 
                        </p>
                    </div>
                </div>
            </div>

        </div>
        
    )
}
export default LandingPage