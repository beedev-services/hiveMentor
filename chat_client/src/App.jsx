import React, { useEffect, useState } from 'react'
import './App.css'
import { ChatEngine } from 'react-chat-engine';
import axios from 'axios'

function App() {
  const [theUser, setTheUser] = useState()
  const [theName, setTheName] = useState()
  const [theSecret, setTheSecret] = useState()

  window.addEventListener('message', function(event) {
    const userId = event.data;
    setTheUser(userId)
    console.log('please work', userId)
  })
  console.log('starting to work', theUser)
  const link = `http://127.0.0.1:8000/chat/authenticate/${theUser}`
  console.log('testing the api url', link)

  useEffect(() => {
    // Make the API call with the user ID
    axios.get(link)
      .then(response => {
        // Handle the API response
        console.log('the res', response)
      })
      .catch(error => {
        // Handle the error
      });
  }, []);


  return (
    <>
        <ChatEngine
          projectID='34e251b1-74c5-4888-b1b1-e56e45673e6e'
          userName='webmaster'
          userSecret='webmasterBeeDevServices'
        />
    </>
  )
}

export default App