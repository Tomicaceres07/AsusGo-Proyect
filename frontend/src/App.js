import React, { useEffect, useState } from 'react';
const axios = require('axios').default;

export const App = () => {

  const [msj, setMsj] = useState();

  useEffect(() => {
    axios.get('/api')
      .then(({data}) => {
        setMsj(data.msj);
      })
      .catch((err) => {
        setMsj(err);
      })
  }, [])
  
  return (
    <div>
      <h1>Hi, this is React</h1>
      <p>{msj}</p>
    </div>
  );
}