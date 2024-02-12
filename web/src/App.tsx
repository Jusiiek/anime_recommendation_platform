import React from 'react';
import {useSelector, useDispatch} from "react-redux";
import {ThemeState} from "./store/themes_reducer";
import "./styles/main.scss"

import {
    Box,
    Container

} from "@mui/material";


function App() {
    const themeState = useSelector((state: ThemeState) => state);
    const dispatch = useDispatch();
    return (
        <Container className={`app ${themeState.theme}`}>
            <Box>
                xx
            </Box>
        </Container>
    );
}

export default App;
