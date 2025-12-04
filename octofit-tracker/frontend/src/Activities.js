import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  useEffect(() => {
    const codespaceName = process.env.CODESPACE_NAME;
    const baseUrl = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev/api/activities/`
      : 'http://localhost:8000/api/activities/';
    fetch(baseUrl)
      .then((res) => res.json())
      .then((data) => setActivities(data))
      .catch((err) => console.error('Error fetching activities:', err));
  }, []);
  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <ul className="list-group">
        {activities.map((activity) => (
          <li key={activity.id || activity._id} className="list-group-item">
            {activity.name} - {activity.type} - {activity.points}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;
