import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  useEffect(() => {
    const codespaceName = process.env.CODESPACE_NAME;
    const baseUrl = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev/api/teams/`
      : 'http://localhost:8000/api/teams/';
    fetch(baseUrl)
      .then((res) => res.json())
      .then((data) => setTeams(data))
      .catch((err) => console.error('Error fetching teams:', err));
  }, []);
  return (
    <div className="container mt-4">
      <h2>Teams</h2>
      <ul className="list-group">
        {teams.map((team) => (
          <li key={team.id || team._id} className="list-group-item">
            {team.name} - Members: {team.members?.length || 0}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;
