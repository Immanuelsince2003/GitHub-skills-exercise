import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  useEffect(() => {
    const codespaceName = process.env.CODESPACE_NAME;
    const baseUrl = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev/api/workouts/`
      : 'http://localhost:8000/api/workouts/';
    fetch(baseUrl)
      .then((res) => res.json())
      .then((data) => setWorkouts(data))
      .catch((err) => console.error('Error fetching workouts:', err));
  }, []);
  return (
    <div className="container mt-4">
      <h2>Workouts</h2>
      <ul className="list-group">
        {workouts.map((workout) => (
          <li key={workout.id || workout._id} className="list-group-item">
            {workout.name} - {workout.type} - {workout.duration} min
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Workouts;
