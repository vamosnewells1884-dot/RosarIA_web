import { useState } from 'react'

function App() {
  const [mensaje, setMensaje] = useState('Hola desde RosarIA 🚀')

  return (
    <div style={{padding: '20px', textAlign: 'center', fontFamily: 'Arial'}}>
      <h1 style={{color: '#ff0000'}}>RosarIA Web</h1>
      <p>{mensaje}</p>
      <button onClick={() => setMensaje('Ya funciona el frontend! 🔴⚫')}>
        Probar
      </button>
    </div>
  )
}

export default App
