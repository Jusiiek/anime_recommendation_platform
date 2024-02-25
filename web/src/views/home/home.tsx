import React from "react";

import {
    Box,
    Grid
} from "@mui/material";

import Navbar from "../../components/navbar";
import {MainCard} from "../../components/main_card";
import {HotAnime} from "../../components/hot_anime";
import {NewAnime} from "../../components/new_anime";


const Home = () => {
    return (
        <Box className={'w-100'}>
            <Grid container>
                <Grid xs={12} className={'mb-10'}>
                    <Navbar />
                </Grid>
                <Grid xs={12} className={'mb-10'}>
                    <NewAnime />
                </Grid>
                <Grid xs={7}>
                    <MainCard />
                </Grid>
                <Grid xs={1} />
                <Grid xs={4}>
                    <HotAnime />
                </Grid>
            </Grid>
        </Box>
    )
}

export default Home
