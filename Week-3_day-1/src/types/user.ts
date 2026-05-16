export interface User{
    id: number;
    name:string;
    email:string;
    age:number;

}

export type CreateUserInput={
    name:string;
    email:string;
    age:number;
}

export type UpdateUserInput={
    name?:string;
    email?:string;
    age?:number;
}