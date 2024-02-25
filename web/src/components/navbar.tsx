import React from "react";
import {useSelector, useDispatch} from "react-redux";
import {
    AppBar,
    Box,
    Typography,
    Button,
    IconButton,
    Menu,
    MenuItem,
    Grid,
    Tooltip
} from "@mui/material";
import MenuIcon from '@mui/icons-material/Menu';

import {UserPanel} from "./user_panel";


const Navbar = () => {
    const [anchorElNav, setAnchorElNav] = React.useState<null | HTMLElement>(null);
    const isMobile = false;
    const pages = [
        {
            text: 'List',
            to: '/list'
        },
        {
            text: 'About',
            to: '/about'
        }
    ]

    const handleOpenMenu = (event: React.MouseEvent<HTMLElement>): void => {
        setAnchorElNav(event.currentTarget);
    }
    const handleCloseMenu = (): void => {
        setAnchorElNav(null);
    }

    return (
        <AppBar position="static" color={'primary'} className={'p-3 rounded-br-3xl rounded-bl-3xl'}>
            <Grid container>
                <Grid item xs={8}>
                    {
                        isMobile
                            ?
                            <Box>
                                <Tooltip title={"Open menu"}>
                                    <IconButton
                                        size={'large'}
                                        aria-label="menu"
                                        onClick={handleOpenMenu}
                                        sx={{mr: 2}}
                                        color={'inherit'}>
                                        <MenuIcon/>
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
                                    {pages.map((page) => (
                                        <MenuItem key={page.text} onClick={handleCloseMenu}>
                                            <Typography textAlign="center">{page.text}</Typography>
                                        </MenuItem>
                                    ))}
                                </Menu>
                            </Box>
                            :
                            <Box className={'d-block'}>
                                <Grid container>
                                    <Grid xs={2}/>
                                    {pages.map(page => (
                                        <Grid key={page.text} xs={1}>
                                            <Button color={'inherit'}>
                                                <Typography variant="h6" component={'span'}
                                                            sx={{flexGrow: 1}}>
                                                    {page.text}
                                                </Typography>
                                            </Button>
                                        </Grid>
                                    ))
                                    }
                                </Grid>
                            </Box>
                    }
                </Grid>
                <Grid item xs={4} className={'text-right'}>
                    <div className={'mr-4'}>
                        <UserPanel/>
                    </div>
                </Grid>
            </Grid>
        </AppBar>
    );
}

export default Navbar;
