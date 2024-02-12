import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';


import {ThemeReducer} from "./store/themes_reducer";
import {createStore} from "redux";
import {Provider} from 'react-redux';


const store = createStore(ThemeReducer);

const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);
root.render(
    <React.StrictMode>
        <Provider store={store}>
            <App/>
        </Provider>
    </React.StrictMode>
);
