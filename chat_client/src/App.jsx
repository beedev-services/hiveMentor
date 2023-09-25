import React, { useEffect, useState } from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css'
import { ChatEngine, ChatList } from 'react-chat-engine';
import { useMultiChatLogic, MultiChatSocket, MultiChatWindow } from "react-chat-engine-advanced";
import MultiChat from './components/MultiChat';
import SingleChat from './components/SingleChat'
import Main from './components/Main'


function App() {


  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Main />} path="/" default />
        <Route element={<MultiChat />} path="/multi/" />
        <Route element={<SingleChat />} path="/single/" />
      </Routes>
    </BrowserRouter>
  )
}

export default App