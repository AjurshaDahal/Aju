import './css/styles.css';
import Navbar from './components/navbar';
import star from './images/star.png';
import anuja from './images/anuja.png';
import yajursa from './images/yajursa.png';
import sophiya from './images/sophiya.png';
import yunika from './images/yunika.png';
import aarati from './images/aarati.png';
function AboutPage() {
    return (
        <div className="about-page">
            <Navbar/>
            
            <main className="content">
                <section className="mission">
                    <img src={star}/> 
                    <h2>Our mission is to simplify voting process making accessible to everyone with just a few clicks!</h2>
                </section>
                
                <section className="how-it-works">
                    <h3>How it works?</h3>
                    <ol>
                        <li>Register: Login using your credentials and face recognition.</li>
                        <li>Explore Elections: Get information about ongoing, past, and upcoming elections.</li>
                        <li>Vote Casting: Choose candidate and submit vote with confidence.</li>
                        <li>View Results: After election closes, check the results to see outcome.</li>
                        <li>Manifesto reading: Click in the vote now in the election section to view candidates' manifesto.</li>
                        <li>Manifesto editing: Verify with face recognition to enable editing.</li>
                    </ol>
                </section>
                
                <section className="security">
                    <h3>Security First</h3>
                    <ul>
                        <li>Data Encryption: Your personal information and voting choices are securely encrypted.</li>
                        <li>Face Recognition Technology: Ensures only you can access your account.</li>
                        <li>Privacy Assurance: We are committed to maintaining your privacy.</li>
                    </ul>
                </section>
                
                <section className="team">
                    <div className='team-heading'>
                    <h3>Our Team</h3>
                    <img src={star} width='40px' alt='star'/>

                    </div>
                   
                    <div className="team-members">
                        <div className='team'>
                            <img src={aarati} alt="Aarati" />
                            <p>
                                Aarati
                            </p>
                        </div>
                        <div className='team'>
                        <img src={yunika} alt="Yunika" />
                            <p>
                                Yunika
                            </p>
                        </div>
                        <div className='team'>
                        <img src={sophiya} alt="Sophiya" />
                            <p>
                               Sophiya
                            </p>
                        </div>
                        <div className='team'>
                        <img src={yajursa} alt="Yajursa" />
                            <p>
                              Yajursa
                            </p>
                        </div>
                        <div className='team'>
                        <img src={anuja} alt="Anuja" />
                            <p>
                              Anuja
                            </p>
                        </div>
                       
                    </div>
                </section>
                
                <footer className="contact">
                    <p>Contact us</p>
                    <p>Email: commonemail@gmail.com</p>
                    <p>We aim to respond to all inquiries within 24 hours.</p>
                </footer>
            </main>
        </div>
    );
}

export default AboutPage;