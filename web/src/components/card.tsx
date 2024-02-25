import React, { ReactNode } from "react";

import {Box} from "@mui/material";


interface CardProps {
    children: ReactNode;
}

export const Card:React.FC<CardProps> = ({ children }) => {
    return (
        <Box className={'w-100 p-4 rounded-3xl'} sx={{bgcolor: 'primary.main'}}>
            {children}
        </Box>
    )
}
