import React, { useEffect, useState } from 'react'
import './App.css'
import { ChatEngine } from 'react-chat-engine';
import axios from 'axios'

function App() {
  const [theUser, setTheUser] = useState()
  const [theName, setTheName] = useState("")
  const [theSecret, setTheSecret] = useState("")
  const secret = 'BeeDevServices'
  const proj = '34e251b1-74c5-4888-b1b1-e56e45673e6e'

  useEffect(() => {
    window.addEventListener('message', function(event) {
      console.log('i am in event listener function inside useEffect')
      const userId = event.data;
      console.log('event.data = userId', userId)
      setTheName(userId)
      setTheSecret(userId+secret)
    })
  },[])
  console.log('after useeffect', theName)

  if (!theName || !theSecret) {
    return <div>Loading...</div>; // or any loading indicator
  }

  return (
    <>
      
        <ChatEngine
          projectID={proj}
          userName={theName}
          userSecret={theSecret}
        />
        {console.log('theName', theName)}
    </>
  )
}

export default App