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

export const UserPanel = () => {
    const [anchorElNav, setAnchorElNav] = React.useState<null | HTMLElement>(null);
    const activeUser = true;
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
