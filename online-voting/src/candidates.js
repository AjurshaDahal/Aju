import './css/styles.css';
import Navbar from './components/navbar';

import candidate from './images/candidate.png';

function Candidates(){
    const candidates = [
        { name: 'ABC', party: 'Party A', imageUrl: candidate },
        { name: 'XYZ', party: 'Party B', imageUrl: candidate },
        { name: 'DEF', party: 'Party C', imageUrl: candidate },
        { name: 'RRR', party: 'Party D', imageUrl: candidate },
    ];

    return(
        <div>
            <Navbar/>
            <main className="content">
                <h2>Candidate List</h2>
                <div className="candidate-list">
                    {candidates.map((candidate, index) => (
                        <div className="candidate" key={index}>
                            <img src={candidate.imageUrl} alt="Candidate" className="candidate-image" />
                            <div className="candidate-info">
                                <p><strong>{candidate.name}</strong></p>
                                <p>{candidate.party}</p>
                            </div>
                            <button className="vote-button">Vote</button>
                            <button className="manifesto-button">Manifesto</button>
                        </div>
                    ))}
                </div>
            </main>
        </div>
    );
}

export default Candidates;