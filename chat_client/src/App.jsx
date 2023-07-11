import React, { useEffect, useState } from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css'
import ChatPage from './components/ChatPage'

function App() {




  return (
    <>
      <Router>
        <Route path="/chat/frame/:userId" component={ChatPage} />
      </Router>
    </>
  )
}

export default App