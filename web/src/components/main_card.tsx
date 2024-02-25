import React from "react";

import {
    Grid,
    Typography
} from "@mui/material";

import {Card} from "../components/card"


export const MainCard = () => {
    return (
        <Card>
            <Grid container>
                <Grid xs={12}>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                </Grid>
                <Grid xs={12}>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                </Grid>
                <Grid xs={12}>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                    <Typography variant={'subtitle1'}>
                        some news
                    </Typography>
                </Grid>
            </Grid>
        </Card>
    )
}
