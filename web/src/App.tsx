import React from 'react';
import {useSelector, useDispatch} from "react-redux";
import {ThemeState} from "./store/themes_reducer";
import "./styles/index.scss"

import {
    Box,
    Container,
    ThemeProvider

} from "@mui/material";

import Home from "./views/home/home"
import {lightTheme, darkTheme} from "./assets/themes";


function App() {
    const themeState = useSelector((state: ThemeState) => state);
    const dispatch = useDispatch();

    return (
        <ThemeProvider theme={themeState.theme === 'light' ? lightTheme : darkTheme}>
            <Container className={`app ${themeState.theme}`}>
                <Box>
                    <Home/>
                </Box>
            </Container>
        </ThemeProvider>
    );
}

export default App;
