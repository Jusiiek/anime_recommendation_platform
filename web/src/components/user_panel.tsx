import React from "react";

import {
    Box,
    Typography,
    IconButton,
    Menu,
    MenuItem,
    Avatar,
    Tooltip,
    Button
} from "@mui/material";

import {useSelector, useDispatch} from "react-redux";

import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';

import {ThemeState} from "../store/themes_reducer";
import {light, dark} from "../store/actions";


export const UserPanel = () => {
    const [anchorElNav, setAnchorElNav] = React.useState<null | HTMLElement>(null);
    const activeUser = false;
    const paths = [
        {
            text: 'Liked anime',
            to: '/liked_anime'
        },
        {
            text: 'Profile',
            to: '/profile'
        },
        {
            text: 'Account',
            to: '/account'
        }
    ]

    const themeState = useSelector((state: ThemeState) => state);
    const dispatch = useDispatch();

    const toggleTheme = () => {
        if (themeState.theme === 'light') {
            dispatch(dark());
        } else {
            dispatch(light());
        }
    }

    const handleOpenMenu = (event: React.MouseEvent<HTMLElement>): void => {
        setAnchorElNav(event.currentTarget);
    }
    const handleCloseMenu = (): void => {
        setAnchorElNav(null);
    }

    return (
        <div>
            {activeUser
                ?
                <Box>
                    <IconButton
                        size={'large'}
                        aria-label="menu"
                        sx={{mr: 2}}
                        color={'inherit'}
                        onClick={toggleTheme}
                    >
                        {themeState.theme === 'light' ? <Brightness7Icon/> : <Brightness4Icon/>}
                    </IconButton>
                    <Tooltip title={"Profile settings"}>
                        <IconButton onClick={handleOpenMenu} sx={{p: 0}}>
                            <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg"/>
                        </IconButton>
                    </Tooltip>
                    <Menu
                        id={'menu-appbar'}
                        anchorOrigin={{
                            vertical: 'bottom',
                            horizontal: 'left',
                        }}
                        keepMounted
                        anchorEl={anchorElNav}
                        open={Boolean(anchorElNav)}
                        onClose={handleCloseMenu}
                    >
                        {paths.map((path) => (
                            <MenuItem key={path.text} onClick={handleCloseMenu}>
                                <Typography textAlign="center">{path.text}</Typography>
                            </MenuItem>
                        ))}
                    </Menu>
                </Box>
                :
                <Box>
                    <IconButton
                        size={'large'}
                        aria-label="menu"
                        sx={{mr: 2}}
                        color={'inherit'}
                        onClick={toggleTheme}
                    >
                        {themeState.theme === 'light' ? <Brightness7Icon/> : <Brightness4Icon/>}
                    </IconButton>
                    <Button color="inherit">
                        <Typography variant="subtitle1" component={'span'}>
                            Login
                        </Typography>
                    </Button>
                    <Button color="inherit">
                        <Typography variant="subtitle1" component={'span'}>
                            Register
                        </Typography>
                    </Button>
                </Box>
            }
        </div>
    )
}
