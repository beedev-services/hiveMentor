import React, { useEffect, useState } from 'react'
import './App.css'
import { ChatEngine } from 'react-chat-engine';
import axios from 'axios'

function App() {
  const [theUser, setTheUser] = useState("")
  const [theName, setTheName] = useState("")
  const [theSecret, setTheSecret] = useState("")
  const secret = 'BeeDevServices'
  const proj = '34e251b1-74c5-4888-b1b1-e56e45673e6e'

  // useEffect(() => {
    
  // },[])
  window.addEventListener('message', function(event) {
    const userId = event.data;
    setTheUser(userId)
    setTheName(userId)
    setTheSecret(userId+secret)
    console.log('please work', userId)
  })
  console.log('starting to work', theUser, theName, theSecret, secret, proj)
  const username = theName
  const pass = theSecret

  // const link = `http://127.0.0.1:8000/chat/authenticate/${theUser}`
  // console.log('testing the api url', link)

  return (
    <>
        <ChatEngine
          projectID={proj}
          userName={username}
          userSecret={pass}
        />
    </>
  )
}

export default App