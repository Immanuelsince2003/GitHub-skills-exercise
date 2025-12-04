import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);
  useEffect(() => {
    const codespaceName = process.env.CODESPACE_NAME;
    const baseUrl = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev/api/leaderboard/`
      : 'http://localhost:8000/api/leaderboard/';
    fetch(baseUrl)
      .then((res) => res.json())
      .then((data) => setLeaders(data))
      .catch((err) => console.error('Error fetching leaderboard:', err));
  }, []);
  return (
    <div className="container mt-4">
      <h2>Leaderboard</h2>
      <ul className="list-group">
        {leaders.map((leader) => (
          <li key={leader.id || leader._id} className="list-group-item">
            {leader.name} - {leader.points} pts
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;
