import React from 'react';

class ShoeForm extends React.Component{
    constructor(props) {
        super(props)
        this.state = {
            manufacturer:"",
            name:"",
            color:"",
            picture_url:"",
            bin:"",
            bins:[]
        };

        this.handleManufacturerChange = this.handleManufacturerChange.bind(this);
        this.handleNameChange = this.handleNameChange.bind(this);
        this.handleColorChange = this.handleColorChange.bind(this);
        this.handlePictureUrlChange = this.handlePictureUrlChange.bind(this);
        this.handleBinChange = this.handleBinChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    async handleSubmit(event) {
        event.preventDefault();
        const data = {...this.state};
        console.log(data);
        delete data.bins
        

        const shoeUrl = 'http://localhost:8080/api/shoes_rest/';
        
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };
        
        
        const response = await fetch(shoeUrl, fetchConfig);
        if (response.ok) {
            const newShoe = await response.json();
            console.log(newShoe);

        const cleared = {
            manufacturer:"",
            name:"",
            color:"",
            picture_url:"",
            bin:"",

          };
        this.setState(cleared);

    }
}

handleManufacturerChange(event) {
    const value = event.target.value;
    this.setState({manufacturer: value})
}

handleNameChange(event) {
    const value = event.target.value;
    this.setState({name: value})
}

handleColorChange(event) {
    const value = event.target.value;
    this.setState({color: value})
}

handlePictureUrlChange(event) {
    const value = event.target.value;
    this.setState({picture_url: value})
}

handleBinChange(event) {
    const value = event.target.value;
    this.setState({bin: value})
}

async componentDidMount(){
    const url = 'http://localhost:8100/api/bins/';
    const response = await fetch(url);
    if (response.ok) {
        const data = await response.json();
        this.setState({bins: data.bins});
       

    }}

    render(){
        return(

            <div className="row">
            <div className="offset-3 col-6">
              <div className="shadow p-4 mt-4">
                <h1>New Shoes</h1>
                <form onSubmit={this.handleSubmit} id="create-hat-form">
                  <div className="form-floating mb-3">
                    <input onChange={this.handleManufacturerChange} value={this.state.manufacturer} placeholder="Manufacturer" required type="text" name="manufacturer" id="manufacturer" className="form-control"/>
                    <label htmlFor="name">Manufacturer</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handleNameChange} value={this.state.name} placeholder="Name" required type="text" name="name" id="name" className="form-control"/>
                    <label htmlFor="color">Name</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handleColorChange} value={this.state.color} placeholder="Color" required type="text" name="color" id="color" className="form-control"/>
                    <label htmlFor="fabric">Color</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handlePictureUrlChange} value={this.state.picture_url} placeholder="Picture_url" required type="text" name="picture_url" id="picture_url" className="form-control"/>
                    <label htmlFor="picture_url">Picture url</label>
                  </div>
                  <div className="mb-3">
                    <select onChange={this.handleBinChange} value={this.state.bin} required id="bin" name="bin" className="form-select">
                      <option value="">Choose a bin</option>
                      {this.state.bins.map(bin => {
                            return (
                            <option key={bin.href} value={bin.href}>
                                {bin.closet_name}
                            </option>
                            );
                        })}

                    </select>
                  </div>
                  <button className="btn btn-primary">Create</button>
                </form>
              </div>
            </div>
          </div>
        )
    }

}

export default ShoeForm;