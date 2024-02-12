import Actions from "./actions";
import {THEMES} from "./actions";

export interface ThemeState {
    theme: string
}

export const initialTheme: ThemeState = {
    theme: 'dark'
}

export const ThemeReducer = (state: ThemeState = initialTheme, action: Actions): ThemeState => {
    switch (action.type) {
        case THEMES.DARK:
            return { ...state, theme: 'dark' };
        case THEMES.LIGHT:
            return { ...state, theme: 'light' };
        default:
            return state
    }
}
