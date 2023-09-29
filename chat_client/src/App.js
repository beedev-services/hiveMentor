import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css'
import MultiChat from './components/MultiChat';
import SingleChat from './components/SingleChat'
import Main from './components/Main'


function App() {


  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Main />} path="/" />
        <Route element={<MultiChat />} path="/multi/" default />
        <Route element={<SingleChat />} path="/single/" />
      </Routes>
    </BrowserRouter>
  )
}

export default App