import React, { useState } from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css'
import './chat.css'
import MultiWrapper from './components/MultiWrapper';
import SingleWrapper from './components/SingleWrapper'
import Main from './components/Main'

function App() {
  const [theUser, setTheUser] = useState('')


  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Main setTheUser={setTheUser} />} path="/" />
        {/* <Route element={<MultiChat  />} path="/multi" /> */}
        {/* <Route element={<SingleChat />} path="/single/" /> */}
        <Route element={<MultiWrapper theUser = {theUser} />} path="/multi" />
        {/* <Route element={<SingleWrapper />} path="/single" /> */}
        {/* <Route path="/" exact render={(props) => <Main {...props} setTheUser={setTheUser} />} />
        <Route path="/multi" render={(props) => <MultiWrapper {...props} username={theUser} />} /> */}
      </Routes>
    </BrowserRouter>
  )
}

export default App