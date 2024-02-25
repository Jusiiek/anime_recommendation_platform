import {createTheme} from "@mui/material";
import {red, yellow, green} from '@mui/material/colors';

export const lightTheme = createTheme({
    palette: {
        primary: {
            main: 'rgb(25, 118, 210)'
        },
        secondary: {
            main: '#ff0000',
        },
        error: {
            main: red[500],
        },
        warning: {
            main: yellow[500],
        },
        info: {
            main: '#0000ff',
        },
        success: {
            main: green[500],
        },
    }
})

export const darkTheme = createTheme({
    palette: {
        primary: {
            main: '#202023'
        },
        secondary: {
            main: '#ff8800',
        },
        error: {
            main: red[500],
        },
        warning: {
            main: yellow[500],
        },
        info: {
            main: '#0099cc',
        },
        success: {
            main: green[500],
        },
    }
})
