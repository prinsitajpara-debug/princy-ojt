export default function users({params}){
    return(
        <div>
            <h1>USER PAGE</h1>
            <p>USER ID : {params.id}</p>
        </div>
    )
}