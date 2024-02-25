import React, { useState, useEffect } from "react";
import {Typography} from "@mui/material";

import {Card} from "../components/card"


export const NewAnime = () => {
    const [animeList, setAnimeList] = useState([]);

    useEffect(() => {
        console.log("NEW ANIME MOUNTED")
    }, []);

    return (
        <Card>
            <Typography variant={'subtitle1'}>
                new anime card
            </Typography>
            <Typography variant={'subtitle1'}>
                new anime card
            </Typography>
            <Typography variant={'subtitle1'}>
                new anime card
            </Typography>
        </Card>
    )
}
