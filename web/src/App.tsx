import React from 'react';
import {useSelector, useDispatch} from "react-redux";
import {ThemeState} from "./store/themes_reducer";
import "./styles/index.scss"

import {
    Box,
    Container

} from "@mui/material";

import Home from "./views/home/home"


function App() {
    const themeState = useSelector((state: ThemeState) => state);
    const dispatch = useDispatch();
    return (
        <Container className={`app ${themeState.theme}`}>
            <Box>
                <Home />
            </Box>
        </Container>
    );
}

export default App;
