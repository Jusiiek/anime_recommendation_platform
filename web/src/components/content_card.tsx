import React, {ReactNode } from "react";
import {Box} from "@mui/material";


interface CardProps {
  children: ReactNode;
}


const ContentCard:React.FC<CardProps> = ({ children }) => {
    return (
        <Box>
            { children }
        </Box>
    )
}

export default ContentCard;
