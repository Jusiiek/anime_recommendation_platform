export const THEMES = {
    LIGHT: 'LIGHT',
    DARK: 'DARK'
};

export const dark = () => ({
    type: THEMES.DARK
})

export const light = () => ({
    type: THEMES.LIGHT
})

type Actions = ReturnType<typeof dark | typeof light>;
export default Actions;
