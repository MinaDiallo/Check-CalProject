import React from 'react'   
import {BrowserRouter as Router, Route, Navigate, Routes} from "react-router-dom"  
import Home from '../components/Sharepages/HomePage'                                                                                                              
import Navbar from '../components/Sharepages/NavBar'                                                                                                              

export default function Navigator()  {
    return(
       <>
        <Router>
        <Navbar/>
        <Routes>
        <Route path="/" element={<Home />} />                                                                                                                                       
        </Routes>
        </Router>
       </> 

    )

}                                                                                                      