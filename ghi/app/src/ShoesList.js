import React from 'react';
import { Link } from "react-router-dom";


class ShoesList extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
           shoes: [],
        }
    }
    
    async componentDidMount() {
        const url = 'http://localhost:8080/api/shoes_rest/';
        const response = await fetch(url);

        if (response.ok){
            const data = await response.json();
            this.setState({shoes: data.shoes})
        } 

        
        
    }
    render(){
    return (

    <>
      <div className="px-4 py-5 my-5 mt-0 text-center bg-green">
        <h1 className="display-5 fw-bold">Shoes List</h1>
        <div className="col-lg-6 mx-auto">
          <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
            <Link to="/shoes/new" className="btn btn-primary btn-lg px-4 gap-3">Add Shoes</Link>
          </div>
        </div>
      </div>
      

        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Manufacturer</th>
                    <th>Model Name</th>
                    <th>Color</th>
                    <th>Picture</th>
                </tr>
            </thead>
            <tbody>
                {this.state.shoes.map(shoe => {
                    return (
                        <tr key={shoe.id}>
                            <td>{ shoe.manufacturer }</td>
                            <td>{ shoe.name }</td>
                            <td>{ shoe.color }</td>
                            <td>{ shoe.picture_url }</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    </>
    );
    }
}

export default ShoesList;
