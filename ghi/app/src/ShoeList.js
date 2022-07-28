import React from 'react'

function ShoeList(props) {
    return(
        <table className="table table-striped">
            <thead>
            <tr>
                <th>Manufacturer</th>
                <th>Model Name</th>
            </tr>
            </thead>
            <tbody>
            {props.shoes_rest.map(shoes_rest => {
                return (
                <tr key={shoes_rest.manufacturer}>
                    <td>{ shoes_rest.name }</td>
                    <td>{ shoes_rest.color }</td>
                </tr>
                );
            })}
            </tbody>
        </table>
    );
}

export default ShoeList;
