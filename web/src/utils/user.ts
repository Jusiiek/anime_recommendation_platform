interface LoginResponse {
    user_data: Object;
    token_data: Object;
}


class ActiveUser {
    user_data: Object = {}
    token_data: Object = {}

    constructor(response_data: LoginResponse) {
        this.user_data = response_data['user_data'];
        this.user_data = response_data['token_data'];
    }

    public getUserData(): Object {
        return this.token_data
    }

    public getTokenData(): Object {
        return this.token_data
    }

}

export default ActiveUser
